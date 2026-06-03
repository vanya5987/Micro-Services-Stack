from app.presenters.logger_presenter import LoggerPresenter
from shared.pathings.logs_path_config import LogsPathConfig

import inspect
import sys

ERROR_LOGGER = LoggerPresenter.get_program_logger_instance(LogsPathConfig.LOG_ERROR_FILE_NAME)
DEBUG_LOGGER = LoggerPresenter.get_program_logger_instance(LogsPathConfig.LOG_DEBUG_FILE_NAME)
INFO_LOGGER = LoggerPresenter.get_program_logger_instance(LogsPathConfig.LOG_INFO_FILE_NAME)

try:
    from tkinter import messagebox
    import tkinter
except Exception as ex:
    ERROR_LOGGER.error(f"Tkinter is not installed for this system!\n, {ex}")

class Notificator:
    @staticmethod
    def print_error(message: str):
        stack = inspect.stack()

        for item in stack:
            ERROR_LOGGER.error(f"{message}\n {item}")

    @staticmethod
    def print_debug(message: str):
        stack = inspect.stack()

        for item in stack:
            DEBUG_LOGGER.debug(f"{message}\n {item}")

    @staticmethod
    def print_info(message: str):
        stack = inspect.stack()

        for item in stack:
            INFO_LOGGER.info(f"{message}\n {item}")

    @staticmethod
    def show_error_message_box(title: str = "Error", message: str = "", exception: Exception = None, use_message_box: bool = True,
                               exit_outside_program: bool = False):
        stack = inspect.stack()

        if use_message_box:
            Notificator.print_error(f"{message}\n")

            try:
                Notificator._init_root()
                messagebox.showerror(title, f"{message}\n {stack[1]}")
            except Exception as ex:
                Notificator.print_error(f"MessageBox is not active, tkinter is not installed! {ex}")

            if exit_outside_program:
                sys.exit(1)
        else:
            Notificator.print_debug(f"{message}\n {exception}")

    #Не использовать, пути прокинуты неверно
    @staticmethod
    def show_info_message_box(title: str = "Info", message: str = "", use_message_box: bool = True):
        if use_message_box:
            try:
                Notificator._init_root()
                messagebox.showinfo(title, message)
            except Exception as ex:
                Notificator.print_error(f"MessageBox is not active, tkinter is not installed! {ex}")
        else:
            Notificator.print_debug(message)

    @staticmethod
    def _init_root():
        try:
            root = tkinter.Tk()
            root.withdraw()
        except Exception as ex:
            Notificator.print_error(f"Tkinter module is not initialize! {ex}")