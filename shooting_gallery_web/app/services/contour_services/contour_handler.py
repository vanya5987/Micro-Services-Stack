from app.utils.laser_utils.laser_center_searcher import PointSearcher
from app.utils.player_utils.player_finder import PlayerFinder
from app.utils.draw_utils.contour_drawer import ContourDrawer
from app.services.laser_services.abstract_point_calculator import AbstractPointCalculator

from shared.configs.core_configs.screen_config import ScreenConfig
from app.utils.target_utils.target_size_calculator import TargetSizeCalculator
from app.entitys.shooting_mods import ShootingMods
from app.utils.formaters.generic_converter import GenericConverter

from typing import *
import cv2
import numpy as np


class ContourHandler:
    def __init__(self, screenContainer: ScreenConfig):
        self.drawer: ContourDrawer = ContourDrawer()

        self.screenContainer: ScreenConfig = screenContainer

        self.epsilon: float = 0.09
        self.maxPlayersCount: int = 5

        self.targetsCoordinates: Dict[int, List[int]] = {}
        self.sortedContours = []

        self.min_contour_length: float = self.screenContainer.minTargetContour #41к/ср == 28к/вск
        self.max_contour_length: float = self.screenContainer.maxTargetContour #97к/cр == 65к/вск

    # Получает контуры цели.
    async def get_target_contours(self, thresholdedImage: np.ndarray, originalFrame: np.ndarray,
                                  shooting_mods: ShootingMods) -> Tuple[List[np.ndarray], np.ndarray, np.ndarray]:
        if shooting_mods.is_calibration_mode:
            contours, _ = cv2.findContours(thresholdedImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            validContours: List[np.ndarray] = []
            self.targetsCoordinates.clear()

            for contour in contours:
                contourArea: float = cv2.contourArea(contour)

                if self.min_contour_length <= contourArea <= self.max_contour_length:
                    approx: np.ndarray = cv2.approxPolyDP(contour, self.epsilon * cv2.arcLength(contour, True), True)

                    contour_points = approx.reshape(-1, 2).tolist()

                    if len(contour_points) != 4:
                        continue

                    validContours.append(approx)

                    contour_points = approx.reshape(-1, 2).tolist()

                    if len(contour_points) >= 3:
                        center = np.mean(contour_points, axis=0)
                        sorted_points = sorted(contour_points,
                                               key=lambda point: np.arctan2(point[1] - center[1], point[0] - center[0]))
                        self.targetsCoordinates[len(validContours)] = sorted_points
                    else:
                        self.targetsCoordinates[len(validContours)] = contour_points

            sortedContours = sorted(validContours, key=lambda cnt: cv2.boundingRect(cnt)[0])
        else:
            sortedContours = []

            for target_coordinates in self.targetsCoordinates.values():
                contour = np.array(target_coordinates, dtype=np.int32).reshape(-1, 1, 2)
                sortedContours.append(contour)

            sortedContours = sorted(sortedContours, key=lambda cnt: cv2.boundingRect(cnt)[0])

        return GenericConverter.convert_generic(sortedContours, self.sortedContours), originalFrame, thresholdedImage

    # Высчитывает положение абстрактной точки относительно внутреннего контура цели.
    async def calculate_abstract_point_to_contours(self, originalFrame: np.ndarray, targetThresholdImage: np.ndarray,
                                                   laserPoints: Dict[int, Tuple[int, int]],
                                                   shooting_mods: ShootingMods) -> Dict[int, Tuple[int, int]]:
        abstractPoints: Dict[int, Tuple[int, int]] = {playerId: (0, 0) for playerId in
                                                      range(1, self.maxPlayersCount + 1)}

        targetContours, _, _ = await self.get_target_contours(targetThresholdImage, originalFrame, shooting_mods)

        for contourIndex in range(len(targetContours)):
            if len(laserPoints) > 0:
                for laserPointIndex, laserPoint in laserPoints.items():
                    abstractPointCalculator = AbstractPointCalculator(targetContours[contourIndex])
                    abstractPoint: Tuple[int, int] = abstractPointCalculator.TransformToScaled(laserPoint)

                    if contourIndex + 1 == laserPointIndex:
                        abstractPoints[contourIndex + 1] = abstractPoint

        return abstractPoints

    # Получаем центр мишени относительно его контуров.
    async def get_target_centers(self, originalFrame: np.ndarray, targetThresholdImage: np.ndarray,
                                 shooting_mods: ShootingMods,
                                 centers) -> Dict[int, Tuple[int, int]]:
        targetContours, _, _ = await self.get_target_contours(targetThresholdImage, originalFrame, shooting_mods)

        for contourIndex in range(0, len(targetContours)):
            currentCenter: Tuple[int, int] = PointSearcher.GetCenter(targetContours[contourIndex])

            if currentCenter is None:
                return centers

            centers[contourIndex + 1] = currentCenter

        return centers

    # Получаем радиус мишени относительно его контуров.
    async def get_target_radii(self, originalFrame: np.ndarray,
                               targetThresholdImage: np.ndarray, shooting_mods: ShootingMods) -> List[int]:
        targetContours, _, _ = await self.get_target_contours(targetThresholdImage, originalFrame, shooting_mods)
        radii: List[int] = []

        for contour in targetContours:
            contourArea: float = cv2.contourArea(contour)
            frameDistance, maxCircleDiameter = TargetSizeCalculator.calculate_target_size(contourArea)
            radii: List[int] = PlayerFinder.get_target_radii_handler(maxCircleDiameter, frameDistance)

        return radii
