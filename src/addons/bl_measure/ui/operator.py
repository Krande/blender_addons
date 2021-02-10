import bpy
import numpy as np


class HelloWorldMeasureOperator(bpy.types.Operator):
    bl_idname = "view3d.get_coord_from_3dcursor"
    bl_label = "Hello World"
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


class HelloWorldMeasureAddToClipBoardOperator(bpy.types.Operator):
    bl_idname = "view3d.copy_coords_to_clipboard"
    bl_label = "Copy Measurements to Clipboard"
    bl_description = "Copy Measure Data to ClipBoard"

    def execute(self, context):
        scene_props = context.scene.MeasureProperties

        start = scene_props.start
        end = scene_props.end

        context.window_manager.clipboard = f"({start[0]}, {start[1]}, {start[2]})({end[0]}, {end[1]}, {end[2]})"
        return {"FINISHED"}
