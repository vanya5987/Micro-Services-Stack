from tools.message_boxes.tkinter_extension.logger_app import Logger

from typing import Dict
import threading

class LoggerPresenter:
    _loggers: Dict[str, Logger] = {}
    _loggers_threads_id: Dict[str, int] = {}
    _lock = threading.Lock()

    @staticmethod
    def get_program_logger_instance(log_file_name: str) -> Logger:
        with LoggerPresenter._lock:
            if not log_file_name in LoggerPresenter._loggers:
                LoggerPresenter._loggers[log_file_name] = Logger(log_file_name, True, True)
                LoggerPresenter._loggers_threads_id[log_file_name] = threading.get_ident()

        return LoggerPresenter._loggers[log_file_name]