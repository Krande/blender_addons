bl_info = {
    "name": "Simply Measure",
    "description": "A simple utility to make measurements",
    "author": "Kristoffer H. Andersen",
    "blender": (2, 90, 1),
    "version": (0, 0, 1),
    "location": "View3D",
    "category": "Development",
}

from .ui import register, unregister

if __name__ == "__main__":
    register()
