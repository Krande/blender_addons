import bpy


class StructuralUtilsPanel(bpy.types.Panel):
    bl_idname = "StructuralUtils_PT_Panel"
    bl_label = "Structural Utils"
    bl_category = "StruUtils"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        props = bpy.context.scene.StruUtilsProperties

        # Export STEP
        layout.row().operator('view3d.export_to_step', text='Export to STEP')
        layout.row().prop(props, 'step_name')
        layout.row().prop(props, 'step_dest')
        layout.row().prop(props, 'step_schema')

        # Copy Name to clipboard
        layout.row().operator('view3d.copy_name_to_clipboard', text='Copy selection name(s) to clipboard')
        layout.row().prop(props, 'name_clip_prefix')

