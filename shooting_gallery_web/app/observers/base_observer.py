from app.presenters.json_presenter import JsonPresenter

from typing import *
import time


class BaseObserver:
    def __init__(self, keys: List[str], path: str):
        self.jsonLoader = JsonPresenter.get_instance()
        self.path: str = path

        data: Dict[str, Union[str, bool, int, List[int]]] = self.jsonLoader.read_json_file(path)
        self.lastChangeTime: float = 0

        self.keys: List[str] = keys
        self.dataValues: Dict[str, int] = {key: data[key] for key in self.keys}

    def is_settings_changed(self):
        currentTime = time.time()

        if currentTime - self.lastChangeTime < 2:
            return False

        currentData: Dict[str, Union[str, bool, int, List[int]]] = self.jsonLoader.read_json_file(self.path)

        dataValues: Dict[str, int] = {key: currentData[key] for key in self.keys}

        if self.dataValues != dataValues:
            self.dataValues = dataValues

            return True
        return False
