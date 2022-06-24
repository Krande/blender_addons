import bpy

class StruUtils_EdgeDB_PT_Panel(bpy.types.Panel):
    bl_idname = "StruUtils_EdgeDB_PT_Panel"
    bl_label = "EdgeDB"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "StruUtils"

    def draw(self, context):
        layout = self.layout
        common_props = bpy.context.scene.StruUtils_Common_Properties
        layout.row().prop(common_props, "view_coll_name")
        layout.row().prop(common_props, "view_data_dest")
        layout.row().operator("view3d.stru_utils_viewpoints_create", text="Create Viewpoint")
        layout.row().operator("view3d.stru_utils_viewpoints_export", text="Export Viewpoints")
        layout.row().operator(
            "view3d.stru_utils_viewpoints_import",
            text="Import Viewpoints",
        )
        layout.row().operator("view3d.stru_utils_viewpoints_clear", text="Clear all Viewpoints")
