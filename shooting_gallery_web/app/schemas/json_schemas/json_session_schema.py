from shared.configs.keys_configs.json_key_config import JsonKeyConfig
from typing import *


class JsonSessionSchema:
    @staticmethod
    def create_session_data() -> Dict[str, any]:
        data = {
            JsonKeyConfig.ALL_SESSION_BULLETS: 0,
            JsonKeyConfig.ABSTRACT_SESSION_LASERS: (0, 0),
            JsonKeyConfig.ALL_SESSION_POINTS: [],
            JsonKeyConfig.ALL_SESSION_TIMES: [],
        }

        return data
