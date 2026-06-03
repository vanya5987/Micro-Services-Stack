from typing import *
import numpy as np

class LaserRadiusCalculator:
    @staticmethod
    def calculate_laser_radius(laserPoint: Tuple[int, int], borderRadius: float, outerCircleCenter: Tuple[int, int],
                               outerCircleRadius: float) -> float:
        distanceToCenter: float = np.sqrt((laserPoint[0] - outerCircleCenter[0]) ** 2 + (laserPoint[1] - outerCircleCenter[1]) ** 2)
        newRadius: float = borderRadius - distanceToCenter

        return outerCircleRadius - newRadius