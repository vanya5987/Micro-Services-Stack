from shared.configs.keys_configs.json_key_config import JsonKeyConfig
from typing import *


class JsonStatesSchema:
    @staticmethod
    def create_target_states() -> Dict[str, any]:
        data = {
            JsonKeyConfig.SHOOTING_DATE[0]: "",
            JsonKeyConfig.SHOOTING_IS_START[0]: False,
            JsonKeyConfig.SHOOTING_IS_STOP[0]: False
        }

        return data
