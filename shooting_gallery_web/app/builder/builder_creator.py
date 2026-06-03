import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from root_path import  RootDirectoryPath
from app.utils.os_system_utils.file_system_shared_utils import FilesystemUtils
from tools.message_boxes.tkinter_extension.notificator import Notificator
from app.utils.os_system_utils.get_system_type import SystemTypeGetter

from shared.pathings.builder_config import BuilderConfig
from builder_packages import BuilderPackages
from build_command import BuildCommand

from app.presenters.json_presenter import JsonPresenter
from shared.pathings.path_config import PathConfig
from shared.configs.keys_configs.json_key_config import JsonKeyConfig

import subprocess

BUILDER_CONFIG = BuilderConfig()
ROOT_PATH: str = RootDirectoryPath.GetRootPath()
DIST_PATH: str = os.path.join(ROOT_PATH, BUILDER_CONFIG.uploading_dist_name)
BUILD_PATH: str = os.path.join(ROOT_PATH, BUILDER_CONFIG.base_build_directory_name)

class BuildCreator:
    @staticmethod
    def create_standard_build():
        try:
            subprocess.run(BuildCommand().create_extend_cmd_command(BuilderConfig()), check=True)

            for src_rel, dest_rel in BuilderPackages.get_files_for_copy():
                src = os.path.join(BUILDER_CONFIG.indicator_path, src_rel)
                dest = os.path.join(BUILDER_CONFIG.build_directory, dest_rel)

                FilesystemUtils.copy_any(src, dest)
        except Exception:
            raise

developer_settings = JsonPresenter.get_instance().read_json_file(
            PathConfig.DEVELOPER_SETTINGS)
is_clear_build: bool = developer_settings[JsonKeyConfig.CLEAR_BUILD[0]]
is_astra = developer_settings[JsonKeyConfig.CURRENT_SYSTEM[0]][JsonKeyConfig.ASTRA_KEY]

if is_astra:
    BuildCreator.create_standard_build()
else:
    if not is_clear_build:
        try:
            # FilesystemUtils.delete_any(BUILD_PATH)
            # FilesystemUtils.delete_any(DIST_PATH)

            BuildCreator.create_standard_build()
            # FilesystemUtils.delete_any(BUILD_PATH)

            if SystemTypeGetter.system_is_windows():
                error_directory_path: str = os.path.join(DIST_PATH, BUILDER_CONFIG.start_file_name)

                # FilesystemUtils.copy_any(error_directory_path, BUILD_PATH)
                # FilesystemUtils.delete_any(error_directory_path)
                # FilesystemUtils.copy_any(BUILD_PATH, DIST_PATH)

                FilesystemUtils.delete_any(BUILD_PATH)
                Notificator.print_debug("\n✅ Build is complete!")
        except Exception as ex:
            # FilesystemUtils.delete_any(BUILD_PATH)
            # FilesystemUtils.delete_any(DIST_PATH)
            Notificator.show_error_message_box(message=f"{ex}")
    else:
        # FilesystemUtils.delete_any(BUILD_PATH) #Пробуем удалить Build если он уже есть.
        # FilesystemUtils.copy_any(BUILD_PATH, DIST_PATH)
        subprocess.run(BuildCommand().create_base_cmd_command(BuilderConfig()), check=True)
        # FilesystemUtils.delete_any(BUILD_PATH) #Тут Build явно создается сборкой, поэтому удаляем его.

    # FilesystemUtils.delete_any(os.path.join(ROOT_PATH, "ShootingGallery.exe.spec"))
    # FilesystemUtils.delete_any(os.path.join(ROOT_PATH, "Стрелковый ас.exe.spec"))