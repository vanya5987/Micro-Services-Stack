from app.observers.base_observer import BaseObserver
from shared.configs.keys_configs.json_key_config import JsonKeyConfig
from shared.pathings.path_config import PathConfig


class CamSettingsObserver:
    def __init__(self):
        self.base_observer = BaseObserver(JsonKeyConfig.CAMERA_OBSERVER_KEYS,
                                          PathConfig.CAM_SETTING_JSON_PATH)

    def is_settings_changed(self):
        return self.base_observer.is_settings_changed()
