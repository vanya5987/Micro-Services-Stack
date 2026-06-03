from shared.pathings.path_config import PathConfig
from shared.configs.keys_configs.json_key_config import JsonKeyConfig

from app.entitys.processing_entity.base_shooting_processing_entity import BaseShootingProcessing
from app.entitys.session_entity.player_params_entity import PlayerParams
from app.utils.formaters.string_format import StringFormat

import threading
from typing import *
import json
import os
import time


class JsonController:
    def __init__(self):
        self.last_data: Dict[str, Dict[str, Union[str, int, bool, List[int]]]] = {}
        self.last_modify_time: Dict[str, float] = {}
        self._lock = threading.Lock()

    # Основной метод для отслеживания
    def read_json_file(self, filePath: str) -> Dict[str, any]:
        currentData = {}

        try:
            currentModifyTime = os.path.getmtime(filePath)

            if filePath not in self.last_modify_time or currentModifyTime != self.last_modify_time[filePath]:
                currentData = self._read_data(filePath)
                self.last_data[filePath] = currentData
                self.last_modify_time[filePath] = currentModifyTime
            else:
                currentData = self.last_data[filePath]

        except:
            if filePath in self.last_data:
                currentData = self.last_data[filePath]

        return currentData

    # Основной метод для отслеживания
    def upload_data(self, filePath: str, data: Dict[str, any]) -> None:
        with open(filePath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def update_any_shooting_states_key(self, key: str, new_value: any):
        self.update_json_value_by_key(key, new_value, PathConfig.SHOOTING_STATES_JSON_PATH)

    def update_licence_key(self, key: str, newValue: str):
        self.update_json_value_by_key(key, newValue, PathConfig.LICENCE_JSON_PATH)

    def update_any_settings_value_key(self, key: str, new_value: any):
        self.update_json_value_by_key(key, new_value, PathConfig.PROGRAM_SETTINGS_JSON_PATH)

    def update_cam_name_by_key(self, newName: Union[int, bool, str]):
        self.update_json_value_by_key(JsonKeyConfig.STANDARD_CAMERA_NAME[0], newName,
                                      PathConfig.CAM_SETTING_JSON_PATH)

    def update_json_value_by_key(self, key: str, newValue: Union[int, bool, str], path_to_file: str):
        data = self._read_data(path_to_file)
        data[key] = newValue
        self.upload_data(path_to_file, data)

    def update_int_dictionary_values(self, key: str, playerId: int, newValue: any):
        validJsonPath: str = PathConfig.SHOOTING_SESSION_PATHS.format(playerId)

        data = self._read_data(validJsonPath)
        data[key] = newValue
        self.upload_data(validJsonPath, data)

    def update_settings_component(self, key: str, index: int, newValue: int):
        settingPath: str = PathConfig.PROGRAM_SETTINGS_JSON_PATH

        with self._lock:
            data = self._read_data(settingPath)
            data[key][index] = newValue
            self.upload_data(settingPath, data)

    def update_session_keys(self, player_id: int, shooting_session_entity: BaseShootingProcessing,
                            player_params: Dict[int, PlayerParams], program_start_timer):
        string_format: str = StringFormat.create_time_format(program_start_timer.GetElapsedTime()[0],
                                                             program_start_timer.GetElapsedTime()[1])
        player_params[player_id].all_times.append(string_format)

        collections: Dict[str, any] = {JsonKeyConfig.ALL_SESSION_POINTS: player_params[player_id].all_coins,
                                       JsonKeyConfig.ALL_SESSION_TIMES: player_params[player_id].all_times,
                                       JsonKeyConfig.ALL_SESSION_BULLETS: player_params[player_id].bullets,
                                       JsonKeyConfig.ABSTRACT_SESSION_LASERS:
                                           shooting_session_entity.abstract_laser_points[player_id]}

        for key, value in collections.items():
            self.update_int_dictionary_values(key, player_id, value)

    def _read_data(self, filePath: str, max_retries: int = 10, delay: float = 0.001) -> Dict[str, any]:
        for attempt in range(max_retries):
            try:
                with open(filePath, 'r', encoding='utf-8') as file:
                    data = json.load(file)

                    return data

            except (json.JSONDecodeError, FileNotFoundError):
                if attempt < max_retries - 1:
                    time.sleep(delay)
                else:
                    return self.last_data.get(filePath, {})

        return {}
