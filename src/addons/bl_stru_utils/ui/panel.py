import bpy


class StructuralUtilsPanel(bpy.types.Panel):
    bl_idname = "StructuralUtils_PT_Panel"
    bl_label = "Structural Utils"
    bl_category = "StruUtils"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        layout.row().operator('view3d.export_to_step', text='Export to STEP')
