from app.controllers.CoreController import CoreController
from app.utils.formaters.target_name_converter import TargetNameConverter

from shared.pathings.path_config import PathConfig

from app.presenters.json_presenter import JsonPresenter
from app.api.json_api.shooter_session_creator import ShooterSessionController

from app.observers.cam_settings_observer import CamSettingsObserver
from app.observers.program_settings_observer import ProgramSettingsObserver

from app.presenters.cam_presenter import CamPresenter
from shared.configs.core_configs.cam_config import CamConfig
from app.utils.formaters.program_start_timer import ProgramStartTimer
from app.utils.draw_utils.contour_drawer import ContourDrawer
from shared.configs.ui_configs.TextContainer import TextContainer
from shared.configs.ui_configs.TextContainer_KZ import TextContainer_KZ
from shared.configs.keys_configs.json_key_config import JsonKeyConfig
from shared.configs.keys_configs.exceptional_keys import ExceptionalKeys

import asyncio
import time
import cv2
import atexit
import numpy as np


class VideoCapture:
    def __init__(self, resolutionWidth: int, resolutionHeight: int, camIndex: int):
        self.resolutionWidth = resolutionWidth
        self.resolutionHeight = resolutionHeight

        self.program_settings_observer = ProgramSettingsObserver()
        self.cam_settings_observer = CamSettingsObserver()

        self.shooterSessionController = ShooterSessionController()
        self.json_controller = JsonPresenter.get_instance()
        self.programStartTimer = ProgramStartTimer()

        self.cam = CamPresenter(camIndex, only_expose=True)

        self.cam.print_properties(only_supported=False)

        program_settings = self.json_controller.read_json_file(PathConfig.PROGRAM_SETTINGS_JSON_PATH)

        if not self.cam.video_stream.isOpened():
            if program_settings[JsonKeyConfig.LANGUAGE[0]] == ExceptionalKeys.RU_KEY:
                print(TextContainer.CAM_ERROR_MESSAGE_BOX_TEXT)
            else:
                print(TextContainer_KZ.CAM_ERROR_MESSAGE_BOX_TEXT)

        if program_settings[JsonKeyConfig.VIDEO_RESOLUTION[0]] == "low":
            self.coef_scaler = CamConfig.LOW_SCALE_COEF

        if program_settings[JsonKeyConfig.VIDEO_RESOLUTION[0]] == "medium":
            self.coef_scaler = CamConfig.MIDDLE_SCALE_COEF

        if program_settings[JsonKeyConfig.VIDEO_RESOLUTION[0]] == "high":
            self.coef_scaler = CamConfig.UPP_SCALE_COEF

        self.cam.set_image_frame(resolutionWidth, resolutionHeight)
        self.cam.set_mjpeg()

        self.shoot_stop_is_update: bool = False
        self.coreController = CoreController((resolutionWidth, resolutionHeight), self.coef_scaler)
        self.screenImageProcessor, self.playerHandler = self.coreController.InitializeCore()

        self.target_name_converter = TargetNameConverter()

        self.prev_frame_time = 0
        self.new_frame_time = 0

        atexit.register(self.cleanup)

    def GetMatrix(self):
        ret, frame = self.cam.video_stream.read()

        shootingStates = self.json_controller.read_json_file(PathConfig.SHOOTING_STATES_JSON_PATH)
        programSettings = self.json_controller.read_json_file(PathConfig.PROGRAM_SETTINGS_JSON_PATH)

        if not ret or frame is None or frame.size == 0:
            black_frame = np.zeros((self.resolutionHeight, self.resolutionWidth, 3), dtype=np.uint8)

            text = TextContainer.CAM_ERROR_IMAGE_TEXT if programSettings[JsonKeyConfig.LANGUAGE[
                0]] == ExceptionalKeys.RU_KEY else TextContainer_KZ.CAM_ERROR_IMAGE_TEXT
            ContourDrawer.draw_camera_error_text(black_frame, text)
            return np.ascontiguousarray(black_frame), False

        #FPS
        self.new_frame_time = time.time()
        fps = 1 / (self.new_frame_time - self.prev_frame_time) if self.prev_frame_time != 0 else 0
        self.prev_frame_time = self.new_frame_time
        #FPS

        program_settings_is_changed: bool = self.program_settings_observer.is_settings_changed()
        cam_settings_is_changed: bool = self.cam_settings_observer.is_settings_changed()

        if cam_settings_is_changed:
            #     self.cam.set_cam_params(only_expose=True)
            self.cam.print_properties(only_supported=False)

        if program_settings_is_changed or programSettings[JsonKeyConfig.CORE_IS_INITIALIZATION[0]]:
            self.coreController = CoreController((self.resolutionWidth, self.resolutionHeight), self.coef_scaler)
            self.target_name_converter = TargetNameConverter()
            self.screenImageProcessor, self.playerHandler = self.coreController.InitializeCore()
            self.json_controller.update_any_settings_value_key(JsonKeyConfig.CORE_IS_INITIALIZATION[0], False)
            self.shoot_stop_is_update = False

        image = asyncio.run(self.screenImageProcessor.ProcessFrame(
            cv2.resize(frame, (self.resolutionWidth, self.resolutionHeight)), shootingStates, programSettings))

        ContourDrawer.draw_fps_count(image, f"FPS: {fps:.2f}", 1)
        ContourDrawer.draw_image_header(image, self.target_name_converter.get_current_target(f"{programSettings['tagetFileName']}"), 1)

        return image, ret

    def cleanup(self):
        self.cam.video_stream.release()