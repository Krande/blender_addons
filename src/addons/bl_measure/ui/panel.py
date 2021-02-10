import bpy


class MeasureUtilPanel(bpy.types.Panel):
    bl_idname = "MeasureUtil_PT_Panel"
    bl_label = "Measurement Util (Hello World)"
    bl_category = "Measure Util"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        scene_props = context.scene.MeasureProperties
        layout.row().operator('view3d.get_coord_from_3dcursor', text='Get position from 3d cursor')

        layout.row().prop(scene_props, "on_start")
        layout.row().prop(scene_props, "start")
        layout.row().prop(scene_props, "end")

        layout.row().prop(scene_props, "length_comp")
        layout.row().prop(scene_props, "length")

        layout.row().operator('view3d.copy_coords_to_clipboard', text='Copy coords to clipboard')

