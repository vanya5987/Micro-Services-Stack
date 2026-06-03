from shared.configs.core_configs.system_analyzer_config import SystemAnalyzerConfig
from tools.message_boxes.tkinter_extension.notificator import Notificator
from app.services.os_system_services.system_info_loader import SystemInfoLoader
from shared.pathings.logs_path_config import LogsPathConfig

from typing import List, Dict

class SystemAnalyzer:
    def __init__(self):
        self.system_info_loader = SystemInfoLoader()

        self.base_log_headers: List[str] = SystemAnalyzerConfig.BASE_LOG_HEADERS
        self.base_system_info_keys: List[str] = SystemAnalyzerConfig.BASE_SYSTEM_INFO_KEYS
        self.base_current_info: List[str] = SystemAnalyzerConfig.BASE_CURRENT_INFO

        self.logs_directory_path: str = LogsPathConfig.LOGS_DIRECTORY_PATH
        self.logs_file_name: str = LogsPathConfig.LOGS_FILE_NAME

        self.registrate_base_config: List[List[str]] = [self.base_system_info_keys, self.base_current_info]

        self.current_system_info: Dict[str, str] = {}

        self.base_length: int = len(self.base_log_headers)

    def load_base_system_info(self):
        try:
            for index in range(self.base_length):
                self.current_system_info[self.base_system_info_keys[index]] = self.base_current_info[index]
        except Exception as ex:
            Notificator.show_error_message_box(f"{ex}")

    def create_base_system_info_log(self):
        self.system_info_loader.write_system_info(self.logs_directory_path, self.logs_file_name,
                                                  self.base_log_headers, self.base_current_info)

    def compare_base_system_settings(self):
        SystemAnalyzer._check_collection_length(self.registrate_base_config, self.base_length)

    @staticmethod
    def _check_collection_length(comparable_info: List[List[str]], valid_length: int):
        for comparable_item in comparable_info:
            if len(comparable_item) != valid_length:
                Notificator.show_error_message_box("Params is invalid count!")
                break