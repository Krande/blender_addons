bl_info = {
    "name": "Structural Utils",
    "description": "Utilities that I needed and that others might find useful",
    "author": "Kristoffer H. Andersen",
    "blender": (3, 0, 0),
    "version": (0, 0, 99),
    "location": "View3D",
    "category": "Development",
}

import pathlib
import site

from .ui import register, unregister

cwd = pathlib.Path(__file__).parent.resolve().absolute()
site.addsitedir(str(cwd / "libs/site/packages"))

if __name__ == "__main__":
    register()
