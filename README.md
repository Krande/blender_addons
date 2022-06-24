# blender_addons

Experiments with blender addons

## Goals
* Get to know the blender api by creating a "bare minimum" addon
* Create a demo addon that checks for updates (using github REST api) and allow the user to update the addon using a single click.

![figure](docs/figures/just_a_figure.png)

For local development of blender addons, I recommend installing the `fake-bpy-module` from https://github.com/nutti/fake-bpy-module using

```
pip install fake-bpy-module-3.2
```

and set the `Scripts` path to the "src" subfolder of your git clone of this repo (as shown below) 

![Blender Preferences](docs/figures/BlenderPrefs.png)

## Remaining work
* Currently the user needs to restart Blender for (at least) the GUI portion of the addon to be updated. Ideally some 
kind of "reload" functionality would be great. But in case there are modules\dependencies that needs a full restart of 
  blender this might as well be the "correct way" of implementing it. 
  
  