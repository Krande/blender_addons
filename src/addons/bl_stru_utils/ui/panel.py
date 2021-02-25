import bpy

# class BIM_PT_misc_utilities(Panel):
#     bl_idname = "BIM_PT_misc_utilities"
#     bl_label = "Miscellaneous"
#     bl_space_type = "VIEW_3D"
#     bl_region_type = "UI"
#     bl_category = "BlenderBIM"


class StruUtils_Update_PT_Panel(bpy.types.Panel):
    bl_idname = "StruUtils_Update_PT_Panel"
    bl_label = "Updates"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "StruUtils"

    def draw(self, context):
        layout = self.layout
        common_props = context.scene.StruUtils_Common_Properties

        layout.row()

        layout.row().operator("view3d.stru_utils_update_check", text="Check For Update")
        if common_props.update_exists:
            layout.row().label(text=f"Update from {common_props.local_version} to {common_props.online_version}?")
        else:
            layout.row().label(text=f'Local version "{common_props.local_version}" is latest')

        update_row = layout.row(align=True)
        update_row.enabled = common_props.update_exists

        update_row.operator("view3d.stru_utils_install_update", text="Install update")


class StruUtils_STEP_PT_Panel(bpy.types.Panel):
    bl_idname = "StruUtils_STEP_PT_Panel"
    bl_label = "STEP IO"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "StruUtils"

    def draw(self, context):
        layout = self.layout
        props = bpy.context.scene.StruUtils_STEP_Properties
        common_props = bpy.context.scene.StruUtils_Common_Properties

        # Export STEP
        layout.row().operator("view3d.stru_utils_export_to_step", text="Export to STEP")
        layout.row().prop(props, "step_name")
        layout.row().prop(props, "step_dest")
        layout.row().prop(props, "step_schema")

        # Copy Name to clipboard
        layout.row().operator("view3d.stru_utils_copy_name_to_clipboard", text="Copy selection name(s) to clipboard")
        layout.row().prop(common_props, "name_clip_prefix")


class StruUtils_Measure_PT_Panel(bpy.types.Panel):
    bl_idname = "StruUtils_Measure_PT_Panel"
    bl_label = "Simply Measure"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "StruUtils"

    def draw(self, context):
        layout = self.layout
        scene_props = context.scene.StruUtils_Measure_Properties

        layout.row().operator("view3d.stru_utils_get_coord_from_3dcursor", text="Get position from 3d cursor")

        layout.row().prop(scene_props, "on_start")
        layout.row().prop(scene_props, "start")
        layout.row().prop(scene_props, "end")

        layout.row().prop(scene_props, "length_comp")
        layout.row().prop(scene_props, "length")

        layout.row().operator("view3d.stru_utils_copy_coords_to_clipboard", text="Copy coords to clipboard")
