import bpy
from . import prop, operator, panel

classes = [
    prop.MeasureProps,
    operator.SimpleMeasureOperator,
    operator.SimpleMeasureAddToClipBoardOperator,
    panel.MeasureUtilPanel,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.MeasureProperties = bpy.props.PointerProperty(type=prop.MeasureProps)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.MeasureProperties
