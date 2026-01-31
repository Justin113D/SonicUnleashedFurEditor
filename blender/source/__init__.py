"""Blender operators, ui and property groups declared in this addon"""
# Mostly copied from HEIO

import bpy
from .properties import SUFE_Settings
from .operators import (
    SUFE_OT_AddEditor,
    SUFE_OT_AddShells,
    SUFE_OT_SwitchVertexColors,
    SUFE_OT_SetBrushDir,
)

from .ui import (
    SUFT_PT_Tools
)

classes = [
    SUFE_Settings,
    SUFE_OT_AddEditor,
    SUFE_OT_AddShells,
    SUFE_OT_SwitchVertexColors,
    SUFE_OT_SetBrushDir,
    SUFT_PT_Tools
]

def register():
    """Loading API classes into blender"""

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    """Unloading classes loaded in register(), as well as various cleanup"""

    for cls in classes:
        bpy.utils.unregister_class(cls)


def reload_package(module_dict_main):
    import importlib
    from pathlib import Path

    def reload_package_recursive(current_dir: Path, module_dict: dict[str, any]):
        for path in current_dir.iterdir():
            if "__init__" in str(path) or path.stem not in module_dict:
                continue

            if path.is_file() and path.suffix == ".py":
                importlib.reload(module_dict[path.stem])
            elif path.is_dir():
                reload_package_recursive(path, module_dict[path.stem].__dict__)

    reload_package_recursive(Path(__file__).parent, module_dict_main)
