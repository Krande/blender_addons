import bpy
from . import prop, operator, panel

classes = [
    # Props
    prop.StruUtils_STEP_Props,
    prop.StruUtils_Measure_Props,
    prop.StruUtils_Common_Props,
    # Operators
    operator.StruUtils_InstallUpdate_Operator,
    operator.StruUtils_CheckForUpdate_Operator,
    operator.StruUtils_Measure_Operator,
    operator.StruUtils_AddToClipBoard_Operator,
    operator.StruUtils_STEP_Operator,
    operator.StruUtils_AddNameToClipBoard_Operator,
    # Panels
    panel.StruUtils_STEP_PT_Panel,
    panel.StruUtils_Measure_PT_Panel,
    panel.StruUtils_Update_PT_Panel,

]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.StruUtils_STEP_Properties = bpy.props.PointerProperty(type=prop.StruUtils_STEP_Props)
    bpy.types.Scene.StruUtils_Measure_Properties = bpy.props.PointerProperty(type=prop.StruUtils_Measure_Props)
    bpy.types.Scene.StruUtils_Common_Properties = bpy.props.PointerProperty(type=prop.StruUtils_Common_Props)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.StruUtils_STEP_Properties
    del bpy.types.Scene.StruUtils_Measure_Properties
    del bpy.types.Scene.StruUtils_Common_Properties
