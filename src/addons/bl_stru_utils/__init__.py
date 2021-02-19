bl_info = {
    "name": "Structural Utils",
    "description": "Utilities that I needed and that others might find useful",
    "author": "Kristoffer H. Andersen",
    "blender": (2, 91, 2),
    "version": (0, 0, 99),
    "location": "View3D",
    "category": "Development",
}

from .ui import register, unregister

if __name__ == "__main__":
    register()
