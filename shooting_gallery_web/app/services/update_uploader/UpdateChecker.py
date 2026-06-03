from app.presenters.json_presenter import JsonPresenter

from app.services.update_uploader.FileDownloader import FileDownloader
from shared.pathings.path_config import PathConfig
from app.utils.os_system_utils.get_system_type import SystemTypeGetter
from app.utils.os_system_utils.file_system_shared_utils import FilesystemUtils

from typing import Tuple
from pathlib import Path

import tempfile
import uuid
import os

class UpdateChecker:
    def __init__(self):
        self.temp_dir = tempfile.TemporaryDirectory(prefix="updater_")
        temp_dir_path = self.temp_dir.name

        config_archive_name: str = str(uuid.uuid4())[:20]  # Имя устанавливаемого архива.

        if os.name == 'nt':  # Windows
            self.program_update_archive_path = Path.home() / "Downloads" / "shooting_gallery_update.7z"
        else:  # Linux, macOS и другие UNIX-подобные
            self.program_update_archive_path = Path.home() / "Загрузки" / "shooting_gallery_update.7z"  # Или "Downloads" в некоторых дистрибутивах.

        self.config_file_path: str = os.path.join(temp_dir_path,
                                                  f"{config_archive_name}.txt")  # Конфиг скачанный с сервера.

        self.json_controller = JsonPresenter.get_instance()

        self.file_downloader = FileDownloader()

    def setup_configurator(self) -> Tuple[int, bool]:
        # Скачиваем конфигуратор с сервера.
        try:
            self.file_downloader.download_with_progress(
                "https://update.algkod.com/ver.txt", self.config_file_path)  # 0 - Корректно/ 1 - Ошибка.
        except:
            return 1, False  # Нет интернета или скачать файл невозможно!

        # Парсим конфигуратор с сервера.
        try:
            with open(self.config_file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                data_list = content.split('|')
        except:
            FilesystemUtils.delete_any(self.config_file_path)  # 0 - Корректно/ 1 - Ошибка.
            return 2, False  # Доступ к файлу - конфигуратору закрыт!

        check_update: bool = False

        # Проверяем дату релиза.
        try:
            data = self.json_controller.read_json_file(PathConfig.VERSION_JSON_PATH)

            if data_list[1] > data["release_date"]:
                check_update = True
        except:
            FilesystemUtils.delete_any(self.config_file_path)  # 0 - Корректно/ 1 - Ошибка.

            return 3, False  # Проверка обновлений завершена с ошибкой!

        FilesystemUtils.delete_any(self.config_file_path)  # 0 - Корректно/ 1 - Ошибка.

        return 0, check_update

    def setup_update(self) -> Tuple[int, bool]:
        try:
            if SystemTypeGetter.system_is_windows():
                download_archive_command_code = self.file_downloader.download_with_progress(
                    f"https://update.algkod.com/win/windows_dist.7z",
                    str(self.program_update_archive_path))  # 0 - Корректно/ 1 - Ошибка.
            else:
                download_archive_command_code = self.file_downloader.download_with_progress(
                    f"https://update.algkod.com/unix/linux_dist.7z",
                    str(self.program_update_archive_path))  # 0 - Корректно/ 1 - Ошибка.
            return download_archive_command_code, True
        except:
            return 2, False
