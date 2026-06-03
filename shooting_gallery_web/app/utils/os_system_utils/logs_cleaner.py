from app.utils.os_system_utils.file_system_shared_utils import FilesystemUtils
from shared.pathings.logs_path_config import LogsPathConfig
from app.utils.time_utils.datetime_utils import DatetimeUtils
from shared.configs.core_configs.logger_config import BaseLogsConfig

from datetime import date
from typing import Dict, List
import os

class LogsCleaner:
    @staticmethod
    def clean_old_log():
        all_logs_dates: Dict[str, date] = LogsCleaner._get_all_logs_dates()

        for file_name, file_date in all_logs_dates.items():
            if DatetimeUtils.append_days_for_data(file_date, BaseLogsConfig.MAX_LOG_DATE_STEP) < DatetimeUtils.get_current_day():
                log_path: str = os.path.join(LogsPathConfig.LOGS_DIRECTORY_PATH, file_name)
                FilesystemUtils.delete_any(log_path)

    @staticmethod
    def _get_all_logs_dates() -> Dict[str, date]:
        logs_indicator: Dict[str, date] = {}

        try:
            all_files_names: List[str] = FilesystemUtils.get_all_directory_files(LogsPathConfig.LOGS_DIRECTORY_PATH)
            armored_files: List[str] = LogsPathConfig.STATIC_ARMORED_FILES

            for name in all_files_names:
                if not name in armored_files:
                    logs_indicator[name] = DatetimeUtils.convert_str_to_date(name[-11:-3])
        except:
            pass

        return logs_indicator