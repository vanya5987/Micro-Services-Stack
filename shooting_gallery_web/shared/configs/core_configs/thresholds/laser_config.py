from typing import Tuple

class LaserConfig:
    MIN_LASER_CONTOUR: int = 1
    MAX_LASER_CONTOUR: int = 300

    def __init__(self, laserThreshold: Tuple[int, int]):
        self.laserLowThreshold: int = laserThreshold[0]
        self.laserUpThreshold: int = laserThreshold[1]