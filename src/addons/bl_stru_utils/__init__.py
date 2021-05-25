
bl_info = {
    "name": "Structural Utils",
    "description": "Utilities that I needed and that others might find useful",
    "author": "Kristoffer H. Andersen",
    "blender": (2, 91, 2),
    "version": (0, 0, 99),
    "location": "View3D",
    "category": "Development",
}

import os
import site
from .ui import register, unregister

cwd = os.path.dirname(os.path.realpath(__file__))
site.addsitedir(os.path.join(cwd, "libs", "site", "packages"))

if __name__ == "__main__":
    register()
