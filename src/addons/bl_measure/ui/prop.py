from bpy.types import PropertyGroup
from bpy.props import (
    FloatVectorProperty,
    FloatProperty,
    BoolProperty
)


class MeasureProps(PropertyGroup):
    start: FloatVectorProperty(default=[0, 0, 0], name="start", description="Start Position of Measurement")
    end: FloatVectorProperty(default=[0, 0, 0], name="end", description="End position of measurement")
    length_comp: FloatVectorProperty(default=[0, 0, 0], name="Delta", description="Length components of measurement")
    length: FloatProperty(default=0, name="Length", description="Length of measurement")
    on_start: BoolProperty(default=True, name="Set start value", description="Set start of measurement")
