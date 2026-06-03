from shared.configs.core_configs.target_config.GameTargetContainer import GameTargetContainer
from root_path import RootDirectoryPath

import os
from typing import *

class PathConfig:
    SERVER_URL = "http://127.0.0.1:8000"
    __ROOT_PATH = RootDirectoryPath.GetRootPath()
    RESOURCES_PATH = os.path.join(__ROOT_PATH, "resources")
    DATA_PATH = os.path.join(__ROOT_PATH, "app", "data")
    JSON_PATH = os.path.join(DATA_PATH, "json")
    SOUNDS_PATH = os.path.join(RESOURCES_PATH, "Sounds")
    PAGES_PATH = os.path.join(__ROOT_PATH, "frontend", "pages")

    SHOOTING_STATES_JSON_PATH = os.path.join(JSON_PATH, "shootingStates.json")
    VERSION_JSON_PATH = os.path.join(JSON_PATH, "versionInfo.json")
    CAM_SETTING_JSON_PATH = os.path.join(JSON_PATH, "camSettings.json")
    PROGRAM_SETTINGS_JSON_PATH = os.path.join(JSON_PATH, "programSettings.json")
    DATA_BASE_PATH = os.path.join(DATA_PATH, "shooting_db.sqlite")
    SHOOTING_SESSION_PATHS = os.path.join(JSON_PATH, "ShootingSessionsFiles", "{0}_shooting_session.json")
    LICENCE_JSON_PATH = os.path.join(JSON_PATH, "licenceKey.json")
    DEVELOPER_SETTINGS = os.path.join(JSON_PATH, "developer_settings.json")

    PRINT_TARGETS = os.path.join(RESOURCES_PATH, "PrintTargets")
    QR_IMAGES = os.path.join(RESOURCES_PATH, "qr_images")
    PDF_PATH = os.path.join(__ROOT_PATH, "documentation", "manual", "ru_user_manual.pdf")
    REPORT_DIRECTORY_PATH = os.path.join(__ROOT_PATH, "reports")

    VIDEO_STREAM_PAGE_PATH = os.path.join(PAGES_PATH, "video_stream_page", "video_stream_page.html")
    MENU_PAGE_PATH = os.path.join(PAGES_PATH, "menu_page", "menu_page.html")

    BOOTSTRAP_JSON_PROGRAM_SETTINGS_PATH: str = os.path.join("dist", "app", "data", "json", "programSettings.json")
    BOOTSTRAP_JSON_DEVELOPER_SETTINGS_PATH: str = os.path.join("app", "data", "json", "developer_settings.json")

    VIDEO_STREAM_SCR_PATH = os.path.join(PAGES_PATH, "video_stream_page", "video_stream_page.js")
    MENU_SCR_PATH = os.path.join(PAGES_PATH, "menu_page", "menu_page.js")

    def __init__(self):
        self.game_target_container = GameTargetContainer()

        self.shoot_sounds_path = {index: os.path.join(PathConfig.SOUNDS_PATH, "ShootsSounds", f"{index}.wav") for index in
                                  range(1, 6)}
        self.program_sounds_path = {"fire": os.path.join(PathConfig.SOUNDS_PATH, "ProgramSounds", "fire.wav"),
                               "end": os.path.join(PathConfig.SOUNDS_PATH, "ProgramSounds", "end.wav")}
        self.ui_sounds_path = {
            "click": os.path.join(PathConfig.SOUNDS_PATH, "UISounds", "Click.wav"),
            "Countdown": os.path.join(PathConfig.SOUNDS_PATH, "UISounds", "Countdown.wav"),
        }

    def get_game_target_sounds_paths(self) -> Dict[int, str]:
        return {index: os.path.join(PathConfig.SOUNDS_PATH, "GameSounds", f"{index}.wav")
                for index in range(
                self.game_target_container.MIN_SOUNDS_COUNT, self.game_target_container.MAX_SOUNDS_COUNT + 1)}