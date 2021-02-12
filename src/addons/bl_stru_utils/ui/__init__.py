import bpy
from . import prop, operator, panel

classes = [
    operator.StructuralUtilsOperator,
    panel.StructuralUtilsPanel,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
