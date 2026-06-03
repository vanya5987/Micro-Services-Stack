from shared.configs.core_configs.target_config.ParentTargetContainer import ParentTargetContainer
from typing import Tuple

class TargetSizeCalculator:
    @staticmethod
    def calculate_target_size(contourArea: float) -> Tuple[float, float]:
        scale: float = (contourArea / ParentTargetContainer.PHYSICAL_TARGET_SIZE)
        frameDistance: float = ParentTargetContainer.FRAME_DISTANCE * scale #Расстояние от кольца до кольца.
        maxCircleDiameter: float = ParentTargetContainer.MAX_CIRCLE_DIAMETER * scale #Максимальный размер цели.

        return frameDistance, maxCircleDiameter