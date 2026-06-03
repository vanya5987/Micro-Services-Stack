from typing import Tuple

class CamConfig:
    LOW_RESOLUTION_VALUES: Tuple[int, int] = (640, 360)
    MIDDLE_RESOLUTION_VALUES: Tuple[int, int] = (1280, 720)
    UPP_RESOLUTION_VALUES: Tuple[int, int] = (1920, 1080)

    LOW_SCALE_COEF: float = 0.3333
    MIDDLE_SCALE_COEF: float = 0.6667
    UPP_SCALE_COEF: float = 1.0