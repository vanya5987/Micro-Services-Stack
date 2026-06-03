from shared.configs.core_configs.target_config.ParentTargetContainer import ParentTargetContainer
from shared.configs.core_configs.target_config.GameTargetContainer import GameTargetContainer
from app.entitys.processing_entity.base_shooting_processing_entity import BaseShootingProcessing

from typing import *
import cv2
import math


class GameTargetCalculator:
    # Рисует Game - цель на математической основе.
    @staticmethod
    def calculate_game_target_angle_point(shooting_session_entity: BaseShootingProcessing, player_id: int) -> Dict[
        int, Tuple[int, int]]:
        contour_area: float = cv2.contourArea(shooting_session_entity.sorted_contours[
                                                  player_id]) / ParentTargetContainer.REDUCTION  # Сокращенный размер контура.

        log_width_base: float = math.log(contour_area, ParentTargetContainer.LOG_BASE)
        log_height_base: float = math.log(contour_area, ParentTargetContainer.LOG_BASE)

        game_width: int = int((shooting_session_entity.target_scale[0] / shooting_session_entity.target_scale[1])
                              * (
                                          log_width_base * ParentTargetContainer.LOG_SCALE_WIDTH))  # Ширина проецируемой внутренней цели.
        game_height: int = int((shooting_session_entity.target_scale[0] / shooting_session_entity.target_scale[1]) * (
                    log_height_base * ParentTargetContainer.LOG_SCALE_HEIGHT))  # Высота проецируемой внутренней цели.

        game_target_centers: Dict[int, Tuple[int, int]] = GameTargetCalculator._get_game_point(
            shooting_session_entity.centers[player_id], game_width, game_height,
            shooting_session_entity.target_scale[2])

        return game_target_centers

    @staticmethod
    def _get_game_point(center: Tuple[int, int], game_width: int, game_height: int, drawing_scale: float) -> Dict[
        int, Tuple[int, int]]:
        game_x: int = int(center[0] + game_width // ParentTargetContainer.POSITION_SCALE)
        game_y: int = int(center[1] - (game_height // drawing_scale) // ParentTargetContainer.POSITION_SCALE)

        game50_drawing_scale: float = 2.0  # Значение == значению из контейнера для game50, обычный маркер для различения мишеней.

        if drawing_scale == game50_drawing_scale:
            game_x = int(
                game_x + GameTargetContainer.DRAWING_POSITION_SCALE // drawing_scale) + GameTargetContainer.START_POINT_POSITION_SCALE

        position_index: int = 1

        game_target_centers: Dict[int, Tuple[int, int]] = {}

        for horizontal_point_index in range(GameTargetContainer.MIN_POINTS_COUNT,
                                            GameTargetContainer.MAX_HORIZONTAL_POINTS_COUNT):
            for vertical_point_index in range(GameTargetContainer.MIN_POINTS_COUNT,
                                              GameTargetContainer.MAX_VERTICAL_POINTS_COUNT):
                game_target_centers[position_index] = \
                    (int(game_x - int(game_width) + (
                                horizontal_point_index * (GameTargetContainer.DRAWING_POSITION_SCALE / drawing_scale))),
                     int(game_y + (
                                 vertical_point_index * (GameTargetContainer.DRAWING_POSITION_SCALE / drawing_scale))))
                position_index += 1

        return game_target_centers

    # Проверяет, находится ли точка внутри проецируемой цели.
    @staticmethod
    def check_laser_in_target(game_points: Dict[int, Tuple[int, int]], laser_point: Tuple[int, int],
                              target_scale: float) \
            -> Tuple[bool, int]:
        for point, (x, y) in game_points.items():
            distance = math.sqrt((laser_point[0] - x) ** 2 + (laser_point[1] - y) ** 2)

            if distance <= target_scale:
                return True, point
        return False, 0
