
from .addon_updater import Alx_Addon_Updater

bl_info = {
    "name": "Addon Updater",
    "description": "",
    "author": "Valerie Bosco[Valy Arhal], (Patrick W. Crawford, neomonkeus)[original developers]",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "Preferences",
    "warning": "",
    "wiki_url": "https://github.com/Valerie-Bosco/blender-addon-updater-BL4x",
    "tracker_url": "https://github.com/Valerie-Bosco/blender-addon-updater-BL4x/issues",
    "category": "System"
}

updater = Alx_Addon_Updater(__path__, bl_info, "Github", "Valerie-Bosco", "XNALara-io-Tools", "https://github.com/Valerie-Bosco/blender-addon-updater-BL4x/releases/")


def register():
    updater.register_addon_updater(mute=True)


def unregister():
    updater.unregister_addon_updater(mute=True)
