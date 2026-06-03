from shared.configs.keys_configs.json_key_config import JsonKeyConfig
from app.entitys.shooting_mods import ShootingMods
from typing import List, Dict, Union


class ShootingModsGetter:
    @staticmethod
    def get_shooting_mods(shootingStates: Dict[str, Union[str, List[int], bool]],
                          programSettings: Dict[str, Union[str, List[int], bool]],
                          target_params: List[Union[float, bool]]) -> ShootingMods:
        return ShootingMods(shootingStates[JsonKeyConfig.SHOOTING_IS_START[0]], target_params[1], target_params[2],
                            target_params[3],
                            target_params[4], target_params[5], programSettings[JsonKeyConfig.IS_CALIBRATION_MODE[0]],
                            programSettings[JsonKeyConfig.IS_QR_SEARCHER_USE[0]])
