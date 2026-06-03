from shared.configs.ui_configs.UserInterfaceColors import ContoursColors
from shared.configs.core_configs.screen_config import ScreenConfig
from app.entitys.processing_entity.base_shooting_processing_entity import BaseShootingProcessing

from shared.configs.ui_configs.TextContainer_KZ import TextContainer_KZ
from shared.configs.ui_configs.TextContainer import TextContainer
from shared.configs.keys_configs.exceptional_keys import ExceptionalKeys
from shared.configs.keys_configs.json_key_config import JsonKeyConfig

from typing import *
import cv2
import numpy as np

class ContourDrawer:
    _FONT = cv2.FONT_HERSHEY_COMPLEX

    _CONTOURS_THICKNESS: int = 7
    _TEXT_THICKNESS: int = 2
    _CAMERA_ERROR_TEXT_THICKNESS: int = 4
    _PLAYER_INFO_THICKNESS: int = 6

    _LASER_POINT_THICKNESS: int = 5
    _LASER_POINT_RADIUS: int = 3

    _FULCRUM_RESOLUTION: int = 1080
    _PADDING_STEP_X: int = 35
    _PADDING_STEP_Y: int = 45
    _HALF_COEF: int = 2

    _CAMERA_ERROR_FONT_SCALE: float = 3.0
    _BASE_TEXT_FONT_SCALE: float = 1.0
    _HEADER_POSITION_X_SCALE: float = 0.40
    _BASE_TEXT_POSITION_X_SCALE: float = 0.73
    _PLAYER_INFO_POSITION_X_SCALE: float = 2.0

    #Тестовый вариант
    @staticmethod
    def draw_circle(image: np.ndarray, center: tuple, radius: int) -> None:
        cv2.circle(image, center, radius, ContoursColors.VALID_TARGET_CONTOUR_COLOR,
                   ContourDrawer._CONTOURS_THICKNESS)

    @staticmethod
    def draw_valid_shape_contour(image: np.ndarray, contour: np.ndarray) -> None:
        cv2.drawContours(image, [contour], -1, ContoursColors.VALID_TARGET_CONTOUR_COLOR,
                         ContourDrawer._CONTOURS_THICKNESS)

    @staticmethod
    def draw_invalid_shape_contour(image: np.ndarray, contour: np.ndarray) -> None:
        cv2.drawContours(image, [contour], -1, ContoursColors.INVALID_TARGET_CONTOUR_COLOR,
                         ContourDrawer._CONTOURS_THICKNESS)

    @staticmethod
    def draw_qr_code_contour(image: np.ndarray, contour: np.ndarray) -> None:
        cv2.drawContours(image, [contour], -1, ContoursColors.QR_COLOR, ContourDrawer._CONTOURS_THICKNESS)

    @staticmethod
    def draw_laser_point(image: np.ndarray, laser: Tuple[int, int]) -> None:
        cv2.circle(image, laser, ContourDrawer._LASER_POINT_RADIUS, ContoursColors.VALID_TARGET_CONTOUR_COLOR,
                   ContourDrawer._LASER_POINT_THICKNESS)

    #Тестовый вариант
    @staticmethod
    def draw_target_for_points(image: np.ndarray, points: List[Tuple[int, int]]) -> None:
        cv2.polylines(image, [points], isClosed=True, color=ContoursColors.VALID_TARGET_CONTOUR_COLOR,
                      thickness=ContourDrawer._CONTOURS_THICKNESS)

    @staticmethod
    def _get_text_rect(text: str,  x: int, y: int, padding: int = 5, font_scale: float = 1):
        (text_width, text_height), baseline = cv2.getTextSize(text, ContourDrawer._FONT, font_scale, ContourDrawer._TEXT_THICKNESS)

        top_left = (x - padding, y - text_height - padding)
        bottom_right = (x + text_width + padding, y + baseline + padding)

        return top_left, bottom_right

    @staticmethod
    def draw_fps_count(image: np.ndarray, text: str, index: int):
        ContourDrawer.draw_text_with_background(image, text, index, x=ContourDrawer._PADDING_STEP_X,
                                                y=ContourDrawer._PADDING_STEP_Y)

    @staticmethod
    def draw_text_with_background(image: np.ndarray, text: str, position_index: int, x: int = None, y: int = None,
                                  background_color = ContoursColors.TEXT_BACKGROUND_COLOR):
        height, width = image.shape[:2]

        scale = height / ContourDrawer._FULCRUM_RESOLUTION
        font_scale: float = ContourDrawer._BASE_TEXT_FONT_SCALE * scale

        if x is None:
            x = int(width * ContourDrawer._BASE_TEXT_POSITION_X_SCALE)

        if y is None:
            y = int(ContourDrawer._PADDING_STEP_Y * scale) * position_index
        else:
            y = int(y * scale)

        top_left, bottom_right = ContourDrawer._get_text_rect(
            text, x, y, font_scale=font_scale)


        cv2.rectangle(image, top_left, bottom_right, background_color, -1)

        cv2.putText(image, text, (x, y), ContourDrawer._FONT, font_scale, ContoursColors.CALIBRATION_TEXT_COLOR, ContourDrawer._TEXT_THICKNESS)

    @staticmethod
    def draw_camera_error_text(image: np.ndarray, text: str) -> None:
        height, width = image.shape[:2]

        scale = height / ContourDrawer._FULCRUM_RESOLUTION
        font_scale = ContourDrawer._CAMERA_ERROR_FONT_SCALE * scale
        text_thickness = int(ContourDrawer._CAMERA_ERROR_TEXT_THICKNESS * scale)

        (text_width, text_height), baseline = cv2.getTextSize(text, ContourDrawer._FONT, font_scale, text_thickness)

        x = (width - text_width) // ContourDrawer._HALF_COEF
        y = (height + text_height) // ContourDrawer._HALF_COEF

        cv2.putText(image, text, (x, y), ContourDrawer._FONT, font_scale, ContoursColors.ERROR_TEXT_COLOR,
                    text_thickness, cv2.LINE_AA)

    @staticmethod
    def draw_image_header(image: np.ndarray, text: str, position_index: int):
        height, width = image.shape[:2]

        scale = height / ContourDrawer._FULCRUM_RESOLUTION
        font_scale: float = ContourDrawer._BASE_TEXT_FONT_SCALE * scale
        x, y = int(width * ContourDrawer._HEADER_POSITION_X_SCALE), int(ContourDrawer._PADDING_STEP_Y * scale)

        top_left, bottom_right = ContourDrawer._get_text_rect(
            text, x, y, font_scale=font_scale)

        cv2.rectangle(image, top_left, bottom_right, ContoursColors.TEXT_BACKGROUND_COLOR, -1)
        cv2.putText(image, text, (x, y), ContourDrawer._FONT, font_scale, ContoursColors.CALIBRATION_TEXT_COLOR,
                    ContourDrawer._TEXT_THICKNESS)

    @staticmethod
    def get_text_container(program_settings):
        if program_settings[JsonKeyConfig.LANGUAGE[0]] == ExceptionalKeys.RU_KEY:
            container = TextContainer()
        else:
            container = TextContainer_KZ()

        return container

    @staticmethod
    def draw_target_position_message(image: np.ndarray, container, program_settings, filtered_contours: Dict[int, np.ndarray]):
        for position_index, contour in filtered_contours.items():
            contour_length: float = cv2.contourArea(contour)
            min_target_threshold: int = ScreenConfig.MIN_TARGET_THRESHOLD
            max_target_threshold: int = ScreenConfig.MAX_TARGET_THRESHOLD

            if (program_settings[JsonKeyConfig.VIDEO_RESOLUTION[0]] == JsonKeyConfig.LOW_VIDEO_RESOLUTION or
                    program_settings[JsonKeyConfig.VIDEO_RESOLUTION[0]] == JsonKeyConfig.MEDIUM_VIDEO_RESOLUTION):
                min_target_threshold -= ScreenConfig.MIDDLE_RESOLUTION_CORRECTION
                max_target_threshold -= ScreenConfig.MIDDLE_RESOLUTION_CORRECTION

            if min_target_threshold > contour_length:
                ContourDrawer.draw_text_with_background(image,
                                                        container.TARGET_LONG_MESSAGE.format(position_index), position_index)

            if max_target_threshold < contour_length:
                ContourDrawer.draw_text_with_background(image,
                                                        container.TARGET_SHORT_MESSAGE.format(position_index), position_index)

            if min_target_threshold < contour_length < max_target_threshold:
                ContourDrawer.draw_text_with_background(image,
                                                        container.TARGET_IS_STATIC_MESSAGE.format(position_index), position_index)

    @staticmethod
    def show_player_info(shooting_session_entity: BaseShootingProcessing):
        if shooting_session_entity.centers:
            for playerIndex, center in shooting_session_entity.centers.items():
                if center and playerIndex in shooting_session_entity.sorted_contours:
                    x, y = center

                    if x > 0 and y > 0:
                        cv2.putText(shooting_session_entity.contour_image, f"{playerIndex}",
                                    (x - 10, y - 170), cv2.FONT_HERSHEY_SIMPLEX,
                                    ContourDrawer._PLAYER_INFO_POSITION_X_SCALE,
                                    ContoursColors.PLAYER_INFO,
                                    ContourDrawer._PLAYER_INFO_THICKNESS)
