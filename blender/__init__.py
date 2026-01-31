"""Main entry point for the Unleashed fur editor blender addon"""

if "register" in locals():
    from .source import reload_package
    reload_package(locals())

from .source import register, unregister

bl_info = {
    "name": "Sonic Unleashed Fur Editor",
    "author": "Justin113D",
    "description": "Adds tools to help with viewing and editing Sonic Unleashed fur normal data",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "tracker_url": "https://github.com/Justin113D/SonicUnleashedFurEditor/issues/new",
    "category": "Modeling"
}
