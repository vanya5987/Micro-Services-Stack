from shared.configs.core_configs.logger_config import LoggerConfig, LogLevel
from shared.pathings.logs_path_config import LogsPathConfig
from root_path import RootDirectoryPath

import os
import threading
import datetime

class Logger:
    def __init__(self, file_name: str, use_console_output: bool, use_file_output: bool):
        self.logger_config = LoggerConfig(file_name)

        self.use_console_output: bool = use_console_output #Вывод в консоль.
        self.use_file_output: bool = use_file_output #Запись в файл.
        self.max_file_size = 10 * 1024 * 1024 #Максимальный размер файла логов - (10MB).

        self._lock = threading.RLock() #Мьютекс.

        logs_path = os.path.join(RootDirectoryPath.GetRootPath(), LogsPathConfig.LOGS_DIRECTORY_PATH)

        os.makedirs(logs_path, exist_ok=True)

        self.log_file = os.path.join(logs_path, f"{file_name}_{datetime.datetime.now().strftime('%Y%m%d')}.md")

        #Создаем заголовок Markdown файла при первом запуске.
        if use_file_output and not os.path.exists(self.log_file):
            self._init_log_file()

    #Инициализация Mark-down файла с заголовком.
    def _init_log_file(self):
        with self._lock:
            try:
                with open(self.log_file, 'w', encoding='utf-8') as file:
                    for row in self.logger_config.get_logs_headers():
                        file.write(row)
            except Exception as e:
                print(f"Ошибка создания файла логов: {e}")

    #Ротация файла при превышении размера.
    def _rotate_file_if_needed(self):
        if not os.path.exists(self.log_file):
            return

        file_size = os.path.getsize(self.log_file)
        if file_size > self.max_file_size:
            with self._lock:

                backup_name = f"{self.log_file}.{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
                os.rename(self.log_file, backup_name)

                self._init_log_file()

    #Запись в файл.
    def _write_to_file(self, level: LogLevel, message: str):
        if not self.use_file_output:
            return

        try:
            self._rotate_file_if_needed()

            with self._lock:
                with open(self.log_file, 'a', encoding='utf-8') as f:
                    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    #Экранируем специальные символы Markdown.
                    escaped_message = message.replace('|', '\\|').replace('\n', '<br>')

                    #Запись в таблицу Markdown.
                    f.write(f"| {timestamp} | {level.value} | {escaped_message} |\n")
                    f.flush()

        except Exception as e:
            print(f"Ошибка записи в файл логов: {e}")

    #Вывод в консоль с цветами.
    def _write_to_console(self, level: LogLevel, message: str):
        if not self.use_console_output:
            return
        reset = '\033[0m'

        color = self.logger_config.get_log_colors().get(level, '')
        timestamp = datetime.datetime.now().strftime('%H:%M:%S')

        log_message = f"{color}[{timestamp}] [{level.value}]"

        log_message += f": {message}{reset}"

        print(log_message)

    def _log(self, level: LogLevel, message: str):
        self._write_to_console(level, message)
        self._write_to_file(level, message)

    def debug(self, message: str):
        self._log(LogLevel.DEBUG, message)

    def info(self, message: str):
        self._log(LogLevel.INFO, message)

    def warning(self, message: str):
        self._log(LogLevel.WARNING, message)

    def error(self, message: str):
        self._log(LogLevel.ERROR, message)

    def critical(self, message: str):
        self._log(LogLevel.CRITICAL, message)

    #Включить/выключить вывод в консоль.
    def enable_console_output(self, enable: bool = True):
        with self._lock:
            self.use_console_output = enable

    #Включить/выключить запись в файл.
    def enable_file_output(self, enable: bool = True):
        with self._lock:
            self.use_file_output = enable