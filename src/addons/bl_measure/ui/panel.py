import bpy


class MeasureUtilPanel(bpy.types.Panel):
    bl_idname = "Measure_simple_PT_Panel"
    bl_label = "Simply Measure"
    bl_category = "Measure"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        scene_props = context.scene.MeasureProperties
        common_props = context.scene.CommonProperties

        layout.row()

        layout.row().operator("view3d.simply_measure_update_check", text="Check For Update")
        if common_props.update_exists:
            layout.row().label(text=f"Update from {common_props.local_version} to {common_props.online_version}?")
        else:
            layout.row().label(text=f'Local version "{common_props.local_version}" is latest')

        update_row = layout.row(align=True)
        update_row.enabled = common_props.update_exists

        update_row.operator("view3d.simply_measure_install_update", text="Install update")

        layout.row().operator("view3d.get_coord_from_3dcursor", text="Get position from 3d cursor")

        layout.row().prop(scene_props, "on_start")
        layout.row().prop(scene_props, "start")
        layout.row().prop(scene_props, "end")

        layout.row().prop(scene_props, "length_comp")
        layout.row().prop(scene_props, "length")

        layout.row().operator("view3d.copy_coords_to_clipboard", text="Copy coords to clipboard")
