from app.utils.laser_utils.laser_radius_calculator import LaserRadiusCalculator
from app.utils.laser_utils.laser_position_checker import LaserPositionChecker
from shared.configs.core_configs.target_config.ParentTargetContainer import ParentTargetContainer

from typing import *


class CoinsAdder:
    def __init__(self, coinScaleIndex: int):
        self.coinScaleIndex: int = coinScaleIndex

    # Добавляет очко для игрока.
    def add_coins(self, center: Tuple[int, int], radii: List[float], laser: Tuple[int, int], coins: List[int]) -> None:
        if center is not None and radii is not None:
            for i in range(ParentTargetContainer.MAX_RADII_COUNT):
                laserRadius: float = LaserRadiusCalculator.calculate_laser_radius(laser, radii[i], center, radii[9])

                if laserRadius is not None:
                    coin: int = int(LaserPositionChecker.check_laser_position_to_radii(laserRadius, radii[0], radii[i]))
                    coins.append(round(coin / self.coinScaleIndex))
