from app.utils.target_utils.virtual_target_calculators.ArmyTargetCalculator import ArmyTargetCalculator
from app.entitys.processing_entity.draw_processing_entity import DrawShootingProcessing
from app.utils.draw_utils.contour_drawer import ContourDrawer

import numpy as np


class ArmyDrawer:
    # Осуществляет постоянную отрисовку армейских мишеней.
    @staticmethod
    def permanent_draw_army_target(shooting_session: DrawShootingProcessing):
        if shooting_session.shooting_mods.army_mode == True and len(shooting_session.sorted_contours) == len(
                shooting_session.centers):
            for player_id in range(1, len(shooting_session.centers) + 1):
                if player_id in shooting_session.valid_contour_matrix:
                    if shooting_session.valid_contour_matrix[player_id]:
                        points: np.ndarray = ArmyTargetCalculator.calculate_army_target_angle_point(shooting_session,
                                                                                                    player_id)
                        ContourDrawer.draw_target_for_points(shooting_session.contour_image,
                                                             points)  # Рисует внутреннию мишень.
