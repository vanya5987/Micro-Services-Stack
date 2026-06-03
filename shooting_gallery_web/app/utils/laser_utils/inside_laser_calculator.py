from app.utils.validators.mods_validators.check_mode_type import CheckModeType
from app.entitys.processing_entity.base_shooting_processing_entity import BaseShootingProcessing

from app.utils.target_utils.virtual_target_calculators.IdpaTargetCalculator import IdpaTargetCalculator
from app.utils.target_utils.virtual_target_calculators.ArmyTargetCalculator import ArmyTargetCalculator
from app.utils.target_utils.virtual_target_calculators.GameTargetCalculator import GameTargetCalculator

import numpy as np
from typing import *


class InsideLaserCalculator:
    @staticmethod
    def check_laser_is_inside_contour(shooting_session_entity: BaseShootingProcessing, player_id: int, laser: Tuple[int, int]):
        isLaserInsideContour: bool = False
        coin: int = 0

        if CheckModeType.check_idpa_mode(shooting_session_entity):  # IDPA - мишень.
            targetAngles: np.ndarray = IdpaTargetCalculator.calculate_idpa_target_angle_point(shooting_session_entity,
                                                                                              player_id)

            isLaserInsideContour = IdpaTargetCalculator.check_laser_in_target(targetAngles, laser)

        if CheckModeType.check_army_mode(shooting_session_entity):  # Army - мишень.
            targetAngles: np.ndarray = ArmyTargetCalculator.calculate_army_target_angle_point(shooting_session_entity,
                                                                                              player_id)

            isLaserInsideContour = ArmyTargetCalculator.check_laser_in_target(targetAngles, laser)

        if CheckModeType.check_game_mode(shooting_session_entity):  # Игровая - мишень.
            gameTargetCenters: Dict[int, Tuple[int, int]] = GameTargetCalculator.calculate_game_target_angle_point(
                shooting_session_entity, player_id)

            isLaserInsideContour, coin = GameTargetCalculator.check_laser_in_target(gameTargetCenters, laser,
                                                                                    shooting_session_entity.target_scale[
                                                                                        0])

        return isLaserInsideContour, coin