from bpy.types import PropertyGroup
from bpy.props import StringProperty, CollectionProperty


class StruUtilsProps(PropertyGroup):
    step_dest = StringProperty(default="c:/temp/step_files", name="STEP export path", description="STEP export path")
    step_name = StringProperty(default="mystepfile", name="STEP name", description="STEP name")
    step_schema = StringProperty(default="AP242", name="STEP schema", description="STEP export path")

    # Name export prefix
    name_clip_prefix = StringProperty(default="", name="Export Name prefix", description="Export Name prefix")