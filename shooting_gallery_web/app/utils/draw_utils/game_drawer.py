from app.utils.target_utils.virtual_target_calculators.GameTargetCalculator import GameTargetCalculator
from shared.configs.ui_configs.UserInterfaceColors import ContoursColors
from app.entitys.processing_entity.draw_processing_entity import DrawShootingProcessing

from typing import *
import numpy as np
import cv2


class GameDrawer:
    # Осуществляет постоянную рисовку ростовых мишеней.
    @staticmethod
    def permanent_draw_game_target(shooting_session: DrawShootingProcessing):
        if shooting_session.shooting_mods.game_mode == True and len(shooting_session.sorted_contours) == len(
                shooting_session.centers):
            for player_id in range(1, len(shooting_session.centers) + 1):
                if player_id in shooting_session.valid_contour_matrix:
                    if shooting_session.valid_contour_matrix[player_id]:
                        game_target_centers = GameTargetCalculator.calculate_game_target_angle_point(shooting_session,
                                                                                                     player_id)
                        GameDrawer._draw_circles_around_points(shooting_session.contour_image, game_target_centers,
                                                               shooting_session.target_scale[0])

    @staticmethod
    def _draw_circles_around_points(image: np.ndarray, game_target_centers: Dict[int, Tuple[int, int]],
                                    target_scale: float):
        for _, (x, y) in game_target_centers.items():
            cv2.circle(image, (x, y), int(target_scale), ContoursColors.VALID_TARGET_CONTOUR_COLOR, 2)
