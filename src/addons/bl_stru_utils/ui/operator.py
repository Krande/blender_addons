import bpy
import logging
import pathlib
import requests
import numpy as np
import os
import shutil
import addon_utils
import urllib.request


def get_ifc_store():
    # Assuming you already have blenderbim installed
    try:
        from blenderbim.bim.ifc import IfcStore
    except:
        raise ModuleNotFoundError("Installation of BlenderBIM not found. Please check your installation")
    return IfcStore


def download_to(destination, url):
    """
    Download file to

    :param destination: File destination
    :param url: Https file object for download
    :return:
    """

    os.makedirs(os.path.dirname(destination), exist_ok=True)

    if os.path.isfile(destination) is False:
        with urllib.request.urlopen(url) as response, open(destination, "wb") as out_file:
            shutil.copyfileobj(response, out_file)


class StruUtils_STEP_Operator(bpy.types.Operator):
    bl_idname = "view3d.stru_utils_export_to_step"
    bl_label = "Export IFC elements to STEP"
    bl_description = "Export IFC elements to STEP"

    def execute(self, context):
        # Get the current scene
        scene = context.scene
        props = scene.StruUtils_STEP_Properties

        # print(self.step_dest)
        destination_file = (pathlib.Path(props.step_dest) / props.step_name).with_suffix(".stp")
        os.makedirs(destination_file.parent, exist_ok=True)

        IfcStore = get_ifc_store()

        import ifcopenshell.geom
        from ifcopenshell.geom.occ_utils import shape_tuple
        from OCC.IFSelect import IFSelect_RetError
        from OCC.Interface import Interface_Static_SetCVal
        from OCC.STEPControl import STEPControl_AsIs, STEPControl_Writer
        from OCC.TopoDS import TopoDS_Compound, TopoDS_Shape
        from OCC import BRepTools

        assembly_mode = 1
        writer = STEPControl_Writer()
        Interface_Static_SetCVal("write.step.schema", props.step_schema)
        # Interface_Static_SetCVal('write.precision.val', '1e-5')
        Interface_Static_SetCVal("write.precision.mode", "1")
        Interface_Static_SetCVal("write.step.assembly", str(assembly_mode))

        def add_geom(geom, name):
            Interface_Static_SetCVal("write.step.product.name", name)
            status = writer.Transfer(geom, STEPControl_AsIs)
            print(status)

        fi = IfcStore.get_file()

        ifc_settings = ifcopenshell.geom.settings()
        ifc_settings.set(ifc_settings.USE_PYTHON_OPENCASCADE, True)
        ifc_settings.set(ifc_settings.SEW_SHELLS, True)
        ifc_settings.set(ifc_settings.WELD_VERTICES, True)
        # ifc_settings.set(ifc_settings.INCLUDE_CURVES, True)
        ifc_settings.set(ifc_settings.USE_WORLD_COORDS, True)
        ifc_settings.set(ifc_settings.VALIDATE_QUANTITIES, True)

        for o1 in bpy.context.selected_objects:
            ifc_elem = fi.by_id(o1.BIMObjectProperties["ifc_definition_id"])
            logging.info(ifc_elem)
            pdct_shape = ifcopenshell.geom.create_shape(ifc_settings, inst=ifc_elem)
            logging.info(type(pdct_shape))
            if type(pdct_shape) is shape_tuple:
                shape = pdct_shape[1]
            else:
                shape = pdct_shape.geometry

            if type(shape) not in (TopoDS_Compound, TopoDS_Shape):
                brep_data = pdct_shape.geometry.brep_data
                ss = BRepTools.BRepTools_ShapeSet()
                ss.ReadFromString(brep_data)
                nb_shapes = ss.NbShapes()
                occ_shape = ss.Shape(nb_shapes)
            else:
                occ_shape = shape
            add_geom(occ_shape, ifc_elem.Name)

        os.makedirs(destination_file.parent, exist_ok=True)

        status = writer.Write(str(destination_file))
        if int(status) > int(IFSelect_RetError):
            raise Exception("Error during write operation")

        print(f'step file created at "{destination_file}"')

        return {"FINISHED"}


class StruUtils_AddNameToClipBoard_Operator(bpy.types.Operator):
    bl_idname = "view3d.stru_utils_copy_name_to_clipboard"
    bl_label = "Copy Name to Clipboard"
    bl_description = "Copy Name to ClipBoard"

    def execute(self, context):
        scene = context.scene
        props = scene.StruUtils_Common_Properties

        IfcStore = get_ifc_store()

        clipboard_str = ""

        fi = IfcStore.get_file()
        for o1 in bpy.context.selected_objects:
            ifc_elem = fi.by_id(o1.BIMObjectProperties["ifc_definition_id"])
            if props.name_clip_prefix != "":
                clipboard_str += props.name_clip_prefix
            clipboard_str += ifc_elem.Name + "\n"
        context.window_manager.clipboard = clipboard_str.rstrip()
        return {"FINISHED"}


class StruUtils_InstallUpdate_Operator(bpy.types.Operator):
    bl_idname = "view3d.stru_utils_install_update"
    bl_label = "Simply Measure (install update)"
    bl_description = "Simply Measure update installation"

    def execute(self, context):
        module_name = "StruUtils"
        common_props = context.scene.StruUtils_Common_Properties
        if common_props.update_exists:
            dest_path = "c:/temp/bl_measure_latest.zip"
            if os.path.isfile(dest_path):
                os.remove(dest_path)
            download_to(dest_path, common_props.download_url)

            # Code for updating addon here
            bpy.ops.preferences.addon_install(overwrite=True, filepath=dest_path)
            # bpy.ops.preferences.addon_enable(module='Simply Measure')
            addon_utils.enable(module_name, default_set=True, persistent=False, handle_error=None)
            bpy.ops.script.reload()
            # bpy.ops.wm.save_userpref()
            # When finished
            common_props.local_version = common_props.online_version
            common_props.update_exists = False
        else:
            print("No newer version exists")
        return {"FINISHED"}


class StruUtils_CheckForUpdate_Operator(bpy.types.Operator):
    bl_idname = "view3d.stru_utils_update_check"
    bl_label = "Measure (check for update)"
    bl_description = "Measure Data"

    def execute(self, context):
        common_props = context.scene.StruUtils_Common_Properties
        addon_ver = [
            addon.bl_info.get("version", (-1, -1, -1))
            for addon in addon_utils.modules()
            if addon.bl_info["name"] == "Simply Measure"
        ][0]
        common_props.local_version = f"{addon_ver[0]}.{addon_ver[1]}.{addon_ver[2]}"

        api_url = "https://api.github.com/repos/Krande/blender_addons/releases/latest"
        r = requests.get(api_url)
        content = r.json()
        common_props.download_url = content["assets"][0]["browser_download_url"]
        tag_name = content["tag_name"]
        cver = tag_name.split("_")[-1]
        common_props.online_version = cver
        release = tuple([int(x) for x in cver.split(".")])
        print("local versus online version:", addon_ver, release)

        if release > addon_ver:
            print("Update Exists")
            common_props.update_exists = True

        return {"FINISHED"}


class StruUtils_Measure_Operator(bpy.types.Operator):
    bl_idname = "view3d.stru_utils_get_coord_from_3dcursor"
    bl_label = "Measure (Simple)"
    bl_description = "Measure Data"

    def execute(self, context):
        # Get the current scene
        scene = context.scene

        # Get the 3D cursor location
        cursor = scene.cursor.location
        scene_props = context.scene.StruUtils_Measure_Properties

        if scene_props.on_start is True:
            scene_props.start = cursor
            scene_props.on_start = False
        else:
            scene_props.end = cursor
            scene_props.on_start = True

        start = scene_props.start
        end = scene_props.end

        lengthc = np.array(end) - np.array(start)

        scene_props.length_comp = list(lengthc)
        scene_props.length = float(np.sqrt(lengthc[0] ** 2 + lengthc[1] ** 2 + lengthc[2] ** 2))

        return {"FINISHED"}


class StruUtils_AddToClipBoard_Operator(bpy.types.Operator):
    bl_idname = "view3d.stru_utils_copy_coords_to_clipboard"
    bl_label = "Copy Measurements to Clipboard"
    bl_description = "Copy Measure Data to ClipBoard"

    def execute(self, context):
        scene_props = context.scene.StruUtils_Measure_Properties

        start = scene_props.start
        end = scene_props.end

        context.window_manager.clipboard = f"({start[0]}, {start[1]}, {start[2]}),({end[0]}, {end[1]}, {end[2]})"
        return {"FINISHED"}
