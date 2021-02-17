import bpy
from . import prop, operator, panel

classes = [
    prop.StruUtilsProps,
    operator.StructuralUtilsOperator,
    operator.StructuralUtilAddNameToClipBoardOperator,
    panel.StructuralUtilsPanel,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.StruUtilsProperties = bpy.props.PointerProperty(type=prop.StruUtilsProps)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.StruUtilsProperties