from typing import List
import threading
import os

class SystemInfoLoader:
    def __init__(self):
        self._lock = threading.RLock()

    def write_system_info(self, logs_directory_path: str, file_name: str, headers: List[str], data: List[str]):
        file_path: str = os.path.join(logs_directory_path, file_name)

        with self._lock:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    for item_index in range(len(data)):
                        row = f"[{headers[item_index].format(data[item_index])}]\n"

                        file.write(row)
            except:
                pass