from typing import List

class LogsPathConfig:
    LOGS_DIRECTORY_PATH: str = "logs"
    LOGS_FILE_NAME: str = "system_info.md"
    LOG_ERROR_FILE_NAME: str = "error_log"
    LOG_DEBUG_FILE_NAME: str = "debug_log"
    LOG_INFO_FILE_NAME: str = "info_log"
    ROLL_BACK_ARMORED_FILES: List[str] = [".storage"]
    STATIC_ARMORED_FILES: List[str] = [".storage", "system_info.md"]