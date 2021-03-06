from bpy.props import BoolProperty, FloatProperty, FloatVectorProperty, StringProperty
from bpy.types import PropertyGroup


class StruUtils_STEP_Props(PropertyGroup):
    step_dest: StringProperty(default="c:/temp/step_files", name="STEP export path", description="STEP export path")
    step_name: StringProperty(default="mystepfile", name="STEP name", description="STEP name")
    step_schema: StringProperty(default="AP242", name="STEP schema", description="STEP export path")


class StruUtils_Common_Props(PropertyGroup):
    update_exists: BoolProperty(default=False, name="Update exists?", description="If an update exists or not")
    download_url: StringProperty(default="", name="Download URL", description="Download URL")
    local_version: StringProperty(default="", name="Local Version", description="Local Version")
    online_version: StringProperty(default="", name="Online Version", description="Online Version")

    # Export Selection to Clipboard
    name_clip_prefix: StringProperty(default="", name="Prefix", description="Export Name prefix")

    # Export Viewpoints
    view_coll_name: StringProperty(default="StruViews", name="Views Name", description="Viewpoints Collection Name")
    view_data_dest: StringProperty(
        default="c:/ada/data/views.json", name="Viewpoints data file", description="Viewpoints export path"
    )


class StruUtils_Measure_Props(PropertyGroup):
    start: FloatVectorProperty(default=[0, 0, 0], name="start", description="Start Position of Measurement")
    end: FloatVectorProperty(default=[0, 0, 0], name="end", description="End position of measurement")
    length_comp: FloatVectorProperty(default=[0, 0, 0], name="Delta", description="Length components of measurement")
    length: FloatProperty(default=0, name="Length", description="Length of measurement")
    on_start: BoolProperty(default=True, name="Set start value", description="Set start of measurement")
