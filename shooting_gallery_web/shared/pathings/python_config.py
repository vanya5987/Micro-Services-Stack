from app.utils.os_system_utils.get_system_type import SystemTypeGetter
from shared.configs.keys_configs.json_key_config import JsonKeyConfig
from app.presenters.json_presenter import JsonPresenter
from shared.pathings.path_config import PathConfig
from root_path import RootDirectoryPath

import sys
import os

class PythonConfig:
    @staticmethod
    def set_python_paths():
        # Добавляем корень проекта в путь Python.
        project_root = RootDirectoryPath.GetRootPath()
        build_root = os.path.join(project_root, "_internal")
        sys.path.insert(0, build_root)

        if SystemTypeGetter.system_is_windows():
            pass
        else:
            if getattr(sys, 'frozen', False):
                json_path: str = os.path.join(project_root, PathConfig.BOOTSTRAP_JSON_DEVELOPER_SETTINGS_PATH)
            else:
                json_path: str = PathConfig.DEVELOPER_SETTINGS

            developer_settings = JsonPresenter.get_instance().read_json_file(json_path)
            current_systems_keys = developer_settings[JsonKeyConfig.CURRENT_SYSTEM[0]]

            if not current_systems_keys[JsonKeyConfig.ASTRA_KEY]:
                if not current_systems_keys[JsonKeyConfig.MOS_KEY]:
                    os.environ["QT_QPA_PLATFORM"] = "wayland"
                os.environ["QT_QUICK_BACKEND"] = "software"

                if current_systems_keys[JsonKeyConfig.MOS_KEY]: #Mos.
                    if getattr(sys, 'frozen', False):
                        base_path = os.path.join(build_root, "PyQt5/Qt5")
                    else:
                        base_path = os.path.join(os.path.join(project_root, ".venv/lib64/python3.8/site-packages/PyQt5/Qt5"))
                else:  # Ubuntu.
                    if getattr(sys, 'frozen', False):
                        base_path = os.path.join(build_root, "PyQt5/Qt5")
                    else:
                        base_path = os.path.join(project_root, ".venv/lib/python3.12/site-packages/PyQt5/Qt5")

                plugins_path = os.path.join(base_path, "plugins")
                platforms_path = os.path.join(plugins_path, "platforms")

                os.environ["QT_PLUGIN_PATH"] = plugins_path
                os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = platforms_path
