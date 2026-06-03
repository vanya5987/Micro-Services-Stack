from pathlib import Path
from typing import List
import os

class ProjectDirectorySearcher:
    def __init__(self):
        self.file_indicator: str = "found_file_name"
        self.max_depth: int = 8
        self.found_paths: List[str] = []

    #Ищет директории с программой по файлу-индикатору.
    def find_directory(self) -> List[str]:
        search_path = Path.home()

        ProjectDirectorySearcher._fast_scan_with_indicator(self,
                                                           search_path, self.file_indicator, self.max_depth, 0)

        return sorted([str(path) for path in self.found_paths])

    #Вспомогательный метод для поиска по файлу-индикатору.
    def _fast_scan_with_indicator(self, path: Path, file_indicator: str, max_depth: int, depth: int) -> bool:
        if depth > max_depth:
            return False

        try:
            with os.scandir(path) as entries:
                for entry in entries:
                    if entry.is_dir():
                        #Проверяем наличие файла-индикатора в текущей директории.
                        indicator_path = Path(entry.path) / file_indicator
                        if indicator_path.exists():
                            self.found_paths.append(str(Path(entry.path)))

                        #Рекурсивно продолжаем поиск в поддиректориях.
                        ProjectDirectorySearcher._fast_scan_with_indicator(self,
                                                                           Path(entry.path), file_indicator,
                                                                           max_depth, depth + 1)

            return True
        except PermissionError:
            return False