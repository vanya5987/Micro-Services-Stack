from typing import *

class ScreenConfig:
    MIN_TARGET_THRESHOLD: int = 62000
    MAX_TARGET_THRESHOLD: int = 68000
    MIDDLE_RESOLUTION_CORRECTION: int = 15000

    def __init__(self, resolution: Tuple[int, int], targetSize: Tuple[int, int], contourScaler: int):
        self.resolution: Tuple[int, int] = resolution
        self.minTargetContour: int = targetSize[0] * contourScaler
        self.maxTargetContour: int = targetSize[1] * contourScaler