from shared.configs.core_configs.target_config.ParentTargetContainer import ParentTargetContainer

from typing import *
import numpy as np

class AbstractPointCalculator:
    def __init__(self, contourPoints: np.ndarray): #Контур имеющий 4 точки.
        self.parentTargetContainer: ParentTargetContainer = ParentTargetContainer()

        self.contour: np.ndarray = contourPoints[:, 0, :]

        self.minX, self.minY = np.min(self.contour, axis=0) #Минимальная точка контура.
        self.maxX, self.maxY = np.max(self.contour, axis=0) #Максимальная точка контура.
        
        self.targetWidth: int = self.maxX - self.minX
        self.targetHeight: int = self.maxY - self.minY

    #Получаем относительные координаты.
    def TransformToRelative(self, laser: Tuple[int, int]) -> Tuple[float, float]:
        relativeX: int = (laser[0] - self.minX) / self.targetWidth
        relativeY: int = (laser[1] - self.minY) / self.targetHeight

        return relativeX, relativeY

    #Преобразование в абстрактные координаты.
    def TransformToScaled(self, laser: Tuple[int, int]) -> Tuple[int, int]:
        relativeX, relativeY = self.TransformToRelative(laser)

        scaledX: int = int(relativeX * self.parentTargetContainer.SCALED_TARGET_WIDTH) #Преобразование (X) в абстрактную ось.
        scaledY: int = int(relativeY * self.parentTargetContainer.SCALED_TARGET_HEIGHT) #Преобразование (Y) в абстрактную ось.

        return scaledX, scaledY
