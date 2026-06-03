from tools.message_boxes.tkinter_extension.notificator import Notificator

import shutil
import os

class FilesystemUtils:
    @staticmethod
    def get_all_directory_files(directory_path: str):
        return os.listdir(directory_path)

    @staticmethod
    def check_file_contains(path: str):
        return os.path.exists(path)

    @staticmethod
    def file_is_directory(path: str):
        return os.path.isdir(path)

    @staticmethod
    def _copy_file(source_path: str, target_path: str):
        shutil.copy2(source_path, target_path)

    @staticmethod
    def _copy_directory(source_path: str, target_path: str):
        shutil.copytree(source_path, target_path, dirs_exist_ok=True)

    @staticmethod
    def copy_any(source_path: str, target_path: str):
        try:
            if FilesystemUtils.file_is_directory(source_path):
                FilesystemUtils._copy_directory(source_path, target_path)
            else:
                FilesystemUtils._copy_file(source_path, target_path)

            Notificator.print_debug(f"Copy {source_path} to {target_path}")
        except:
            FilesystemUtils.delete_any(source_path)
            FilesystemUtils.delete_any(target_path)

    @staticmethod
    def delete_any(path: str):
        try:
            if FilesystemUtils.file_is_directory(path):
                FilesystemUtils._delete_directory(path)
            else:
                FilesystemUtils._delete_file(path)

            Notificator.print_debug(f"Path {path} has been deleted!")
        except:
            Notificator.print_debug(f"Path {path} is not contains!")

    @staticmethod
    def _delete_file(file_path: str):
        os.remove(file_path)

    @staticmethod
    def _delete_directory(directory_path: str):
        shutil.rmtree(directory_path)