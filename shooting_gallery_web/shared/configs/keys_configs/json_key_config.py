from shared.configs.core_configs.exercise_config import ExerciseContainer
from shared.configs.keys_configs.exceptional_keys import ExceptionalKeys
from shared.configs.keys_configs.target_name_keys import TargetNameKeys

from typing import Tuple, List, Dict


class JsonKeyConfig:
    LOW_VIDEO_RESOLUTION: str = "low"
    MEDIUM_VIDEO_RESOLUTION: str = "medium"
    HIGH_VIDEO_RESOLUTION: str = "high"

    STANDARD_CAMERA_NAME: Tuple[str, str] = ("STANDARD_CAMERA_NAME", "c992 pro")
    CAMERA_BRIGHTNESS: Tuple[str, int] = ("BRIGHTNESS", 0)  # Или 128 для c992 pro
    CAMERA_CONTRAST: Tuple[str, int] = ("CONTRAST", 0)  # Или 128 для c992 pro
    CAMERA_SATURATION: Tuple[str, int] = ("SATURATION", 48)  # Или 128 для c992 pro
    CAMERA_EXPOSURE: Tuple[str, int] = ("EXPOSURE", -5)  # Или -5 для c992 pro\

    LICENCE_KEY: Tuple[str, str] = ("licenceKey", "")

    VERSION: Tuple[str, str] = ("version", ExceptionalKeys.CURRENT_VERSION)

    SHOOTING_DATE: Tuple[str, str] = ("shootingDate", "")
    SHOOTING_IS_START: Tuple[str, bool] = ("shootIsStart", False)
    SHOOTING_IS_STOP: Tuple[str, bool] = ("shootIsStop", False)

    LASER_PULSE_DURATION: Tuple[str, int] = ("laserPulseDuration", 200)
    LASER_BRIGHTEST: Tuple[str, int] = ("laserBrightest", 220)
    SOUND_VALUE: Tuple[str, int] = ("soundValue", 100)
    SOUND_IS_ENABLE: Tuple[str, bool] = ("soundIsEnable", True)
    VIDEO_RESOLUTION: Tuple[str, str] = ("videoResolution", MEDIUM_VIDEO_RESOLUTION)
    EXERCISE_TYPE_INDEX: Tuple[str, int] = ("exerciseTypeIndex", 3)
    PLAYER_COUNT: Tuple[str, int] = ("playerCount", 1)
    CENTERS_COUNT: Tuple[str, int] = ("centersCount", 0)
    BULLET_COUNT: Tuple[str, int] = ("bulletCount", 10)
    SHOOT_TIME_THRESHOLD: Tuple[str, str] = ("shootTimeThreshold", ExerciseContainer.INVALID_TIME_FORMAT)
    TARGET_FILE_NAME: Tuple[str, str] = ("tagetFileName", TargetNameKeys.PISTOL_25_FILE_NAME)
    CORE_IS_INITIALIZATION: Tuple[str, str] = ("coreIsInitialize", False)
    LANGUAGE: Tuple[str, str] = ("language", ExceptionalKeys.RU_KEY)
    IS_CALIBRATION_MODE: Tuple[str, bool] = ("isCalibrationMode", True)
    USE_RED_FILTER: Tuple[str, bool] = ("useRedFilter", True)
    IS_QR_SEARCHER_USE: Tuple[str, bool] = ("isQrSearcherUse", True)
    QR_CONTOUR_LENGTH: Tuple[str, List[int]] = ("qrContourLength", [500, 2000])
    FILE_INDICATOR: Tuple[str, str] = ("fileIndicator", "wh200python.dat")
    SEARCH_DEPTH: Tuple[str, int] = ("searchDepth", 8)

    WEAPON_TYPES: Tuple[str, Dict[str, bool]] = ("weapon_types", {"use_pistol": [True, 1], "use_rifle": [True, 2],
                                                                  "use_rifle_and_assault_rifle": [True, 3],
                                                                  "use_multi_weapon": [True, 4]})

    WINDOWS_KEY: str = "windows"
    MOS_KEY: str = "mos"
    UBUNTU_KEY: str = "ubuntu"
    ASTRA_KEY: str = "astra"

    CURRENT_SYSTEM: Tuple[str, Dict[str, bool]] = ("system", {WINDOWS_KEY: True, MOS_KEY: False, UBUNTU_KEY: False,
                                                                          ASTRA_KEY: False})
    TARGET_SIZE: Tuple[str, List[int]] = ("targetSize", [28, 65])
    TARGET_SCALER: Tuple[str, int] = ("targetScaler", 1000)
    CLEAR_BUILD: Tuple[str, int] = ("clear_build", False)

    ALL_SESSION_POINTS: str = "allPoints"
    ALL_SESSION_TIMES: str = "allTimesToAllPoints"
    ALL_SESSION_BULLETS: str = "bulletsForPlayer"
    ABSTRACT_SESSION_LASERS: str = "abstractLasers"

    CAM_NAME: List[str] = [STANDARD_CAMERA_NAME, CAMERA_BRIGHTNESS, CAMERA_CONTRAST, CAMERA_SATURATION,
                           CAMERA_EXPOSURE]
    LICENSE: List[str] = [LICENCE_KEY]
    VERSION_INFO: List[str] = [VERSION]
    SHOOTING_STATES: List[str] = [SHOOTING_DATE, SHOOTING_IS_START, SHOOTING_IS_STOP]
    PROGRAM_SETTINGS: List[str] = [LASER_PULSE_DURATION, LASER_BRIGHTEST, SOUND_VALUE, SOUND_IS_ENABLE,
                                   VIDEO_RESOLUTION,
                                   EXERCISE_TYPE_INDEX, PLAYER_COUNT, CENTERS_COUNT, BULLET_COUNT, SHOOT_TIME_THRESHOLD,
                                   TARGET_FILE_NAME,
                                   CORE_IS_INITIALIZATION, LANGUAGE, IS_CALIBRATION_MODE, USE_RED_FILTER,
                                   IS_QR_SEARCHER_USE,
                                   QR_CONTOUR_LENGTH, TARGET_SIZE, TARGET_SCALER, FILE_INDICATOR, SEARCH_DEPTH]
    DEVELOPER_SETTINGS: List[str] = [WEAPON_TYPES, CURRENT_SYSTEM, CLEAR_BUILD]

    ALL_SCHEMAS: List[List[str]] = [CAM_NAME, LICENSE, VERSION_INFO, SHOOTING_STATES, PROGRAM_SETTINGS, DEVELOPER_SETTINGS]

    PROGRAM_SETTINGS_OBSERVER_KEYS: List[str] = [LASER_PULSE_DURATION[0], LASER_BRIGHTEST[0], SOUND_VALUE[0],
                                                 SOUND_IS_ENABLE[0], EXERCISE_TYPE_INDEX[0],
                                                 PLAYER_COUNT[0], BULLET_COUNT[0], TARGET_FILE_NAME[0],
                                                 USE_RED_FILTER[0],
                                                 IS_QR_SEARCHER_USE[0], QR_CONTOUR_LENGTH[0],
                                                 TARGET_SIZE[0], TARGET_SIZE[0], CENTERS_COUNT[0]]

    VIDEO_RESOLUTION_VARIANTS: List[str] = [LOW_VIDEO_RESOLUTION, MEDIUM_VIDEO_RESOLUTION, HIGH_VIDEO_RESOLUTION]

    CAMERA_OBSERVER_KEYS: List[str] = [CAMERA_BRIGHTNESS[0], CAMERA_CONTRAST[0], CAMERA_SATURATION[0],
                                       CAMERA_EXPOSURE[0]]
