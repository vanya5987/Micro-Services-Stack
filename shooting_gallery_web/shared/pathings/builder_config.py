from app.builder.builder_packages import BuilderPackages
from root_path import RootDirectoryPath
from tools.pipeline_templates.splash_launcher.splash_file_indicator import SplashDirectoryPath
from app.utils.os_system_utils.get_system_type import SystemTypeGetter

from app.presenters.json_presenter import JsonPresenter
from shared.pathings.path_config import PathConfig
from shared.configs.keys_configs.json_key_config import JsonKeyConfig

from typing import List, Dict
import os

class BuilderConfig:
    def __init__(self):
        developer_settings = JsonPresenter.get_instance().read_json_file(PathConfig.DEVELOPER_SETTINGS)

        is_clear_build: bool = developer_settings[JsonKeyConfig.CLEAR_BUILD[0]]
        system_is_windows: bool =  developer_settings[JsonKeyConfig.CURRENT_SYSTEM[0]][JsonKeyConfig.WINDOWS_KEY]

        self.root_directory_path: str = RootDirectoryPath.GetRootPath()

        windows_bootstrap_filename: str = "windows_bootstrap.py"
        linux_bootstrap_filename: str = "linux_bootstrap.py"

        if system_is_windows:
            current_bootstrap_filename: str = windows_bootstrap_filename
        else:
            current_bootstrap_filename: str = linux_bootstrap_filename


        if is_clear_build:
            self.start_file_name: str = "Стрелковый ас.exe" if SystemTypeGetter.system_is_windows() else "Стрелковый ас"
            self.indicator_path: str = SplashDirectoryPath().get_splash_path()
            self.root_file_name: str = current_bootstrap_filename
        else:
            self.start_file_name: str = "ShootingGallery.exe" if SystemTypeGetter.system_is_windows() else "ShootingGallery"
            self.indicator_path: str = os.path.join(self.root_directory_path, "app", "entry_points")
            self.root_file_name: str = "test_core_bootstrap.py"

        self.uploading_dist_name: str = "dist"
        self.base_build_directory_name: str = "build"

        #Путь куда будет сохранена директория со сборкой.
        self.build_directory = os.path.join(self.root_directory_path, self.uploading_dist_name)

        #Список файлов для копирования в partable папку с исполняемым файлом. (Относительно корня проекта).
        copy_files_temp: List[str] = ["app/data",
                                      "reports",
                                      "resources",
                                      "frontend",
                                      "documentation/manual",
                                      "documentation/CHANGELOG.md",
                                      "logs"
                                      "wh200python.dat",
                                      "icon.ico"]

        self.files_for_copy: Dict[str, str] = {os.path.join(self.root_directory_path, item): os.path.join(self.build_directory, item)
                                               for item in copy_files_temp}

        if developer_settings[JsonKeyConfig.CURRENT_SYSTEM[0]][JsonKeyConfig.ASTRA_KEY]:
            self.command_params: List[str] = ['pyinstaller', '--onefile', '--icon=icon.ico', '--windowed',
                                              '--hidden-import=pydantic.dataclasses',
                                              '--hidden-import=typing_extensions',
                                              '--hidden-import=uuid', '--hidden-import=colorsys',
                                              '--hidden-import=ipaddress'
                                              f'--distpath={self.uploading_dist_name}']
        else:
            self.command_params: List[str] = ['pyinstaller', '--onefile', '--icon=icon.ico', '--windowed',
                                              '--hidden-import=pydantic.dataclasses',
                                              '--hidden-import=typing_extensions',
                                              '--hidden-import=uuid', '--hidden-import=colorsys',
                                              '--hidden-import=ipaddress'
                                              f'--distpath={self.uploading_dist_name}']

        #Список библиотек для ручного импорта.
        if is_clear_build:
            self.add_packages_commands: List[str] = ["PyQt5"]
        else:
            self.add_packages_commands: List[str] = ["PIL", "PyQt5", "numpy", "cv2", "dotenv", "httpx", "idna", "pygrabber",
                                                     "httpcore", "certifi", "h11", "h2", "patoolib", "ipaddress", "screeninfo",
                                                     "fastapi", "uvicorn", "starlette", "annotated_doc", 'anyio', "pydantic", "http",
                                                     "logging", "click"]

            if not system_is_windows:
                self.add_packages_commands.extend(["psutil"])

    #Возвращает команду сборки бинарных файлов.
    def get_add_packages_command(self) -> List[str]:
        return BuilderPackages.get_add_packages_command(self.add_packages_commands)