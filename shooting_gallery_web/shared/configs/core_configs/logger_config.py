from enum import Enum
from typing import List
import datetime

class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class BaseLogsConfig:
    MAX_LOG_DATE_STEP: int = 10 #Возвращает максимальное количество дней для хранения логов.

class LoggerConfig:
    def __init__(self, log_file_name: str):
        log_file_name: str = log_file_name

        self.logs_headers: List[str] = [
            f"# Логи приложения: {log_file_name}\n\n",
            f"**Создан:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n", "---\n\n",
            "## Записи логов\n\n", "| Время | Уровень | Модуль | Сообщение |\n",
            "|-------|---------|--------|-----------|\n"
        ]

        self.log_colors = {
            LogLevel.DEBUG: '\033[38;5;255;48;5;18m', #Белый на темно-синем.
            LogLevel.INFO: '\033[38;5;255;48;5;22m', #Белый на темно-зеленом.
            LogLevel.WARNING: '\033[38;5;255;48;5;58m',#Белый на темно-желтом/коричневом.
            LogLevel.ERROR: '\033[38;5;255;48;5;52m', #Белый на темно-красном.
            LogLevel.CRITICAL: '\033[38;5;255;48;5;90m' #Белый на темно-фиолетовом.
        }

    #Возвращает заголовки для Loger.
    def get_logs_headers(self) -> List[str]:
        return self.logs_headers

    #Возвращает цвета для логирования.
    def get_log_colors(self):
        return self.log_colors