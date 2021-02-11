import bpy
import requests
import numpy as np
import os
import shutil
import addon_utils


def download_to(destination, url):

    import urllib.request

    os.makedirs(os.path.dirname(destination), exist_ok=True)

    if os.path.isfile(destination) is False:
        with urllib.request.urlopen(url) as response, open(destination, "wb") as out_file:
            shutil.copyfileobj(response, out_file)


class SimpleMeasureInstallUpdateOperator(bpy.types.Operator):
    bl_idname = "view3d.simply_measure_install_update"
    bl_label = "Simply Measure (install update)"
    bl_description = "Simply Measure update installation"

    def execute(self, context):
        module_name = 'Simply Measure'
        common_props = context.scene.CommonProperties
        if common_props.update_exists:
            dest_path = "c:/temp/bl_measure_latest.zip"
            if os.path.isfile(dest_path):
                os.remove(dest_path)
            download_to(dest_path, common_props.download_url)

            # Code for updating addon here
            bpy.ops.preferences.addon_install(overwrite=True, filepath=dest_path)
            # bpy.ops.preferences.addon_enable(module='Simply Measure')
            addon_utils.enable(
                module_name, default_set=True, persistent=False, handle_error=None)
            # bpy.ops.wm.save_userpref()
            # When finished
            common_props.local_version = common_props.online_version
            common_props.update_exists = False
        else:
            print('No newer version exists')
        return {"FINISHED"}


class SimpleMeasureUpdateOperator(bpy.types.Operator):
    bl_idname = "view3d.simply_measure_update_check"
    bl_label = "Measure (check for update)"
    bl_description = "Measure Data"

    def execute(self, context):
        common_props = context.scene.CommonProperties
        addon_ver = [
            addon.bl_info.get("version", (-1, -1, -1))
            for addon in addon_utils.modules()
            if addon.bl_info["name"] == "Simply Measure"
        ][0]
        common_props.local_version = f'{addon_ver[0]}.{addon_ver[1]}.{addon_ver[2]}'

        api_url = "https://api.github.com/repos/Krande/blender_addons/releases/latest"
        r = requests.get(api_url)
        content = r.json()
        common_props.download_url = content['assets'][0]["browser_download_url"]
        tag_name = content["tag_name"]
        cver = tag_name.split("_")[-1]
        common_props.online_version = cver
        release = tuple([int(x) for x in cver.split(".")])
        print(addon_ver)
        print(release)
        print(addon_ver, release)

        if release > addon_ver:
            print("Update Exists")
            common_props.update_exists = True

        return {"FINISHED"}


class SimpleMeasureOperator(bpy.types.Operator):
    bl_idname = "view3d.get_coord_from_3dcursor"
    bl_label = "Measure (Simple)"
    bl_description = "Measure Data"

    def execute(self, context):
        # Get the current scene
        scene = context.scene

        # Get the 3D cursor location
        cursor = scene.cursor.location
        scene_props = context.scene.MeasureProperties

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


class SimpleMeasureAddToClipBoardOperator(bpy.types.Operator):
    bl_idname = "view3d.copy_coords_to_clipboard"
    bl_label = "Copy Measurements to Clipboard"
    bl_description = "Copy Measure Data to ClipBoard"

    def execute(self, context):
        scene_props = context.scene.MeasureProperties

        start = scene_props.start
        end = scene_props.end

        context.window_manager.clipboard = f"({start[0]}, {start[1]}, {start[2]})({end[0]}, {end[1]}, {end[2]})"
        return {"FINISHED"}
