import bpy
import os
import logging
import pathlib


class StructuralUtilsOperator(bpy.types.Operator):
    bl_idname = "view3d.export_to_step"
    bl_label = "Export IFC elements to STEP"
    bl_description = "Export IFC elements to STEP"

    def execute(self, context):
        # Get the current scene
        scene = context.scene
        props = scene.StruUtilsProperties

        # print(self.step_dest)
        destination_file = (pathlib.Path(props.step_dest) / props.step_name).with_suffix(".stp")
        os.makedirs(destination_file.parent, exist_ok=True)

        # Assuming you already have blenderbim installed
        try:
            from blenderbim.bim.ifc import IfcStore
        except:
            raise ModuleNotFoundError("Installation of BlenderBIM not found. Please check your installation")

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


class StructuralUtilAddNameToClipBoardOperator(bpy.types.Operator):
    bl_idname = "view3d.copy_name_to_clipboard"
    bl_label = "Copy Name to Clipboard"
    bl_description = "Copy Name to ClipBoard"

    def execute(self, context):
        scene = context.scene
        props = scene.StruUtilsProperties
        # Assuming you already have blenderbim installed
        try:
            from blenderbim.bim.ifc import IfcStore
        except:
            raise ModuleNotFoundError("Installation of BlenderBIM not found. Please check your installation")

        clipboard_str = ""

        fi = IfcStore.get_file()
        for o1 in bpy.context.selected_objects:
            ifc_elem = fi.by_id(o1.BIMObjectProperties["ifc_definition_id"])
            if props.name_clip_prefix != "":
                clipboard_str += props.name_clip_prefix
            clipboard_str += ifc_elem.Name + "\n"
        context.window_manager.clipboard = clipboard_str  # .rstrip()
        return {"FINISHED"}
