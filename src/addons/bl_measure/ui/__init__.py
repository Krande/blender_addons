import bpy
from . import prop, operator, panel

classes = [
    prop.MeasureProps,
    prop.CommonProps,
    operator.SimpleMeasureInstallUpdateOperator,
    operator.SimpleMeasureUpdateOperator,
    operator.SimpleMeasureOperator,
    operator.SimpleMeasureAddToClipBoardOperator,
    panel.MeasureUtilPanel,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.MeasureProperties = bpy.props.PointerProperty(type=prop.MeasureProps)
    bpy.types.Scene.CommonProperties = bpy.props.PointerProperty(type=prop.CommonProps)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.MeasureProperties
    del bpy.types.Scene.CommonProperties
