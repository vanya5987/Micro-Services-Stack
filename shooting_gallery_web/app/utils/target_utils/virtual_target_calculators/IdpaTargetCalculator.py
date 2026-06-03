from shared.configs.core_configs.target_config.IdpaTargetContainer import IdpaTargetContainer
from shared.configs.core_configs.target_config.ParentTargetContainer import ParentTargetContainer
from app.entitys.processing_entity.base_shooting_processing_entity import BaseShootingProcessing

from typing import *
import cv2
import numpy as np
import math


class IdpaTargetCalculator:
    # Рисует IDPA - цель на математической основе.
    @staticmethod
    def calculate_idpa_target_angle_point(shooting_session_entity: BaseShootingProcessing,
                                          player_id: int) -> np.ndarray:
        contour_area: float = cv2.contourArea(shooting_session_entity.sorted_contours[
                                                  player_id]) / ParentTargetContainer.REDUCTION  # Сокращенный размер контура.

        log_width_base: float = math.log(contour_area, ParentTargetContainer.LOG_BASE)
        log_height_base: float = math.log(contour_area, ParentTargetContainer.LOG_BASE)

        idpa_width: int = int(shooting_session_entity.target_scale[0] * (
                    log_width_base * ParentTargetContainer.LOG_SCALE_WIDTH))  # Ширина проецируемой внутренней цели.
        idpa_height: int = int(shooting_session_entity.target_scale[0] * (
                    log_height_base * ParentTargetContainer.LOG_SCALE_HEIGHT))  # Высота проецируемой внутренней цели.

        cut_points: List[Tuple[int, int]] = IdpaTargetCalculator.get_idpa_points(
            shooting_session_entity.centers[player_id],
            idpa_width, idpa_height, shooting_session_entity.target_scale[1])

        points: np.ndarray = np.array(cut_points, dtype=np.int32)  # Конвертация коллекции в np.ndarray.

        return points

    @staticmethod
    def get_idpa_points(center: Tuple[int, int], idpa_width: int, idpa_height: int, drawingScale: float) \
            -> List[Tuple[int, int]]:
        idpa_x1: int = int(center[0] - idpa_width // ParentTargetContainer.POSITION_SCALE)
        idpa_y1: int = int(center[1] - idpa_height // ParentTargetContainer.POSITION_SCALE)
        idpa_x2: int = int(center[0] + idpa_width // ParentTargetContainer.POSITION_SCALE)
        ipda_y2: int = int(center[1] + idpa_height // ParentTargetContainer.POSITION_SCALE)

        idpa_trapezoid_scale_to_head: float = IdpaTargetContainer.IDPA_TRAPEZOID_SCALE_TO_HEAD * drawingScale  # Скейл посадки трапеции ближе к шее.
        idpa_head_height_scale: float = IdpaTargetContainer.IDPA_HEAD_HEIGHT_SCALE * drawingScale  # Скейл высоты головы.
        idpa_head_width_scale: float = IdpaTargetContainer.IDPA_HEAD_WIDTH_SCALE * drawingScale  # Скейл ширины головы.
        idpa_trapezoid_scale_to_shoulders: float = IdpaTargetContainer.IDPA_TRAPEZOID_SCALE_TO_SHOULDERS * drawingScale  # Скейл посадки трапеции ближе к плечам.
        idpa_trapezoid_to_sholders_scale: float = IdpaTargetContainer.IDPA_TRAPEZOID_TO_SHOULDERS_SCALE * drawingScale  # Скейл длины трапеции.
        idpa_sholders_length_scale: float = IdpaTargetContainer.IDPA_SHOULDERS_LENGTH_SCALE * drawingScale  # Скейл длины плечей.
        idpa_sholder_width_scale: float = IdpaTargetContainer.IDPA_SHOULDERS_WIDTH_SCALE * drawingScale  # Скейл ширины плечей.
        idpa_body_height: float = IdpaTargetContainer.IDPA_BODY_HEIGHT * drawingScale  # Скейл высоты туловища.

        cut_points: List[Tuple[int, int]] = [
            (idpa_x1 + int(idpa_width * IdpaTargetContainer.BOTTOM_IDPA_CUT_SCALE), ipda_y2),  # Нижняя левая точка.
            (idpa_x2 - int(idpa_width * IdpaTargetContainer.BOTTOM_IDPA_CUT_SCALE), ipda_y2),  # Нижняя правая точка.
            (idpa_x2 + idpa_sholders_length_scale, idpa_y1 + int(idpa_height * IdpaTargetContainer.TOP_IDPA_CUT_SCALE
                                                                 ) + idpa_body_height),
            # Правая точка у основания (2 - ая снизу).
            (idpa_x2 + idpa_sholders_length_scale, idpa_y1 + int(idpa_height * IdpaTargetContainer.TOP_IDPA_CUT_SCALE
                                                                 ) - idpa_sholder_width_scale),
            # Правая плечевая точка.
            (idpa_x2 - idpa_trapezoid_to_sholders_scale,
             idpa_y1 + int(idpa_height * IdpaTargetContainer.TOP_IDPA_CUT_SCALE
                           ) - idpa_trapezoid_scale_to_shoulders),
            # Правая трапеция - плечевая точка.
            (idpa_x2 - int(idpa_width * IdpaTargetContainer.TOP_IDPA_CUT_SCALE),
             idpa_y1 + idpa_trapezoid_scale_to_head),
            # Правая трапеция - шеевая точка.
            (idpa_x2 - idpa_head_width_scale, (idpa_y1 + int(idpa_width) - idpa_head_height_scale)),
            # Правая верхняя точка.
            ((idpa_x2 - int(idpa_width)) + idpa_head_width_scale, (idpa_y1 + int(idpa_width) - idpa_head_height_scale)),
            # Левая верхняя точка.
            (idpa_x1 + int(idpa_width * IdpaTargetContainer.TOP_IDPA_CUT_SCALE),
             idpa_y1 + idpa_trapezoid_scale_to_head),
            # Левая трапеция - шеевая точка.
            (idpa_x1 + idpa_trapezoid_to_sholders_scale,
             idpa_y1 + int(idpa_height * IdpaTargetContainer.TOP_IDPA_CUT_SCALE
                           ) - idpa_trapezoid_scale_to_shoulders),
            # Левая трапеция - плечевая точка.
            (idpa_x1 - idpa_sholders_length_scale,
             idpa_y1 + int(idpa_height * IdpaTargetContainer.TOP_IDPA_CUT_SCALE) - idpa_sholder_width_scale),
            # Левая плечевая точка.
            (idpa_x1 - idpa_sholders_length_scale,
             idpa_y1 + int(idpa_height * IdpaTargetContainer.TOP_IDPA_CUT_SCALE) + idpa_body_height),
            # Левая точка у основания (2 - ая снизу).
        ]

        return cut_points

    # Проверяет, находится ли точка внутри проецируемой цели.
    @staticmethod
    def check_laser_in_target(points: np.ndarray, laserPoint: Tuple[int, int]) -> bool:
        return cv2.pointPolygonTest(points, (laserPoint[0], laserPoint[1]), measureDist=False) >= 0
