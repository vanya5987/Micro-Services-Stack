from shared.configs.core_configs.target_config.ArmyTargetContainer import ArmyTargetContainer
from shared.configs.core_configs.target_config.ParentTargetContainer import ParentTargetContainer
from app.entitys.processing_entity.base_shooting_processing_entity import BaseShootingProcessing

from typing import *
import cv2
import numpy as np
import math


class ArmyTargetCalculator:
    # Рисует Army - цель на математической основе.
    @staticmethod
    def calculate_army_target_angle_point(shooting_session: BaseShootingProcessing, player_id: int) -> np.ndarray:
        contour_area: float = cv2.contourArea(shooting_session.sorted_contours[
                                                  player_id]) / ParentTargetContainer.REDUCTION  # Сокращенный размер контура.

        log_width_base: float = math.log(contour_area, ParentTargetContainer.LOG_BASE)
        log_height_base: float = math.log(contour_area, ParentTargetContainer.LOG_BASE)

        armyWidth: float = int(ParentTargetContainer.POSITION_SCALE *
                               (log_width_base * ArmyTargetContainer.LOG_ARMY_SCALE_WIDTH)) / \
                           shooting_session.target_scale[1]  # Ширина проецируемой внутренней цели.
        army_height: float = int(ParentTargetContainer.POSITION_SCALE *
                                 (log_height_base * ArmyTargetContainer.LOG_ARMY_SCALE_HEIGHT)) / \
                             shooting_session.target_scale[1]  # Высота проецируемой внутренней цели.

        cut_points: List[Tuple[int, int]] = ArmyTargetCalculator.get_army_points(shooting_session.centers[player_id],
                                                                                 armyWidth, army_height,
                                                                                 shooting_session.target_scale[1])

        points: np.ndarray = np.array(cut_points, dtype=np.int32)  # Конвертация коллекции в np.ndarray.

        return points

    @staticmethod
    def get_army_points(center: Tuple[int, int], army_width: float, army_height: float, drawing_scale: float) -> List[
        Tuple[int, int]]:
        army_head_width: float = ArmyTargetContainer.ARMY_HEAD_WIDTH / drawing_scale  # Скейл ширины головы.
        army_head_height: float = ArmyTargetContainer.ARMY_HEAD_HEIGHT / drawing_scale  # Скейл высоты головы.
        army_trapezoid_scale_to_head: float = ArmyTargetContainer.ARMY_TRAPEZOID_SCALE_TO_HEAD / drawing_scale  # Скейл посадки трапеции ближе к шее.
        army_trapezoid_length: float = ArmyTargetContainer.ARMY_TRAPEZOID_LENGTH / drawing_scale  # Скейл длины трапеции.
        army_shoulder_height: float = ArmyTargetContainer.ARMY_SHOULDER_HEIGHT / drawing_scale  # Скейл посадки плечей.

        army_x1: int = int(center[0] - army_width // ParentTargetContainer.POSITION_SCALE)
        army_y1: int = int(center[1] - army_height // ParentTargetContainer.POSITION_SCALE)
        army_x2: int = int(center[0] + army_width // ParentTargetContainer.POSITION_SCALE)
        army_y2: int = int(center[1] + army_height // ParentTargetContainer.POSITION_SCALE)

        cut_points: List[Tuple[int, int]] = [
            (army_x1 + int(army_width * ArmyTargetContainer.BOTTOM_ARMY_CUT_SCALE), army_y2),  # Нижняя левая точка.
            (army_x2 - int(army_width * ArmyTargetContainer.BOTTOM_ARMY_CUT_SCALE), army_y2),  # Нижняя правая точка.
            (army_x2, army_y1 + int(army_height * ArmyTargetContainer.TOP_ARMY_CUT_SCALE) + army_shoulder_height),
            # Правая плечевая точка.
            (army_x2 - int(army_width * ArmyTargetContainer.TOP_ARMY_CUT_SCALE) - army_trapezoid_length,
             army_y1 + army_trapezoid_scale_to_head),
            # Правая трапеция - шеевая точка.
            (army_x2 - army_head_width, (army_y1 + int(army_width) - army_head_height)),  # Правая верхняя точка.
            (army_x2 - int(army_width) + army_head_width, army_y1 + int(army_width) - army_head_height),
            # Левая верхняя точка.
            (army_x1 + int(army_width * ArmyTargetContainer.TOP_ARMY_CUT_SCALE) + army_trapezoid_length,
             army_y1 + army_trapezoid_scale_to_head),
            # Левая трапеция - шеевая точка.
            (army_x1, army_y1 + int(army_height * ArmyTargetContainer.TOP_ARMY_CUT_SCALE) + army_shoulder_height)
            # Левая плечевая точка.
        ]

        return cut_points

    # Проверяет, находится ли точка внутри проецируемой цели.
    @staticmethod
    def check_laser_in_target(points: np.ndarray, laser_point: Tuple[int, int]) -> bool:
        return cv2.pointPolygonTest(points, (laser_point[0], laser_point[1]), measureDist=False) >= 0
