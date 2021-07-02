from bpy.props import BoolProperty, FloatProperty, FloatVectorProperty, StringProperty
from bpy.types import PropertyGroup


class CommonProps(PropertyGroup):
    update_exists: BoolProperty(default=False, name="Update exists?", description="If an update exists or not")
    download_url: StringProperty(default="", name="Download URL", description="Download URL")
    local_version: StringProperty(default="", name="Local Version", description="Local Version")
    online_version: StringProperty(default="", name="Online Version", description="Online Version")


class MeasureProps(PropertyGroup):
    start: FloatVectorProperty(default=[0, 0, 0], name="start", description="Start Position of Measurement")
    end: FloatVectorProperty(default=[0, 0, 0], name="end", description="End position of measurement")
    length_comp: FloatVectorProperty(default=[0, 0, 0], name="Delta", description="Length components of measurement")
    length: FloatProperty(default=0, name="Length", description="Length of measurement")
    on_start: BoolProperty(default=True, name="Set start value", description="Set start of measurement")
