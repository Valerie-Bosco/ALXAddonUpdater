
from . import ALX_AddonUpdater

bl_info = {
    "name": "ALX-AddonUpdater",
    "description": "",
    "author": "Valerie Bosco[Valy Arhal], (Patrick W. Crawford, neomonkeus)[original developers]",
    "version": (1, 1, 0),
    "blender": (4, 0, 0),
    "location": "Preferences",
    "warning": "",
    "wiki_url": "https://github.com/Valerie-Bosco/ALX-AddonUpdater",
    "tracker_url": "https://github.com/Valerie-Bosco/ALX-AddonUpdater/issues",
    "category": "System"
}


addon_updater = ALX_AddonUpdater.Alx_Addon_Updater(
    path=__path__,
    bl_info=bl_info,
    engine="Github",
    engine_user_name="Valerie-Bosco",
    engine_repo_name="ALX-AddonUpdater",
    manual_download_website="https://github.com/Valerie-Bosco/ALX-AddonUpdater/releases/tag/main_branch_latest"
)


def register():
    addon_updater.register_addon_updater(True)


def unregister():
    addon_updater.unregister_addon_updater()


if __name__ == "__main__":
    register()
