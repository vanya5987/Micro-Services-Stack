from shared.configs.core_configs.thresholds.laser_config import LaserConfig

from app.utils.draw_utils.contour_drawer import ContourDrawer
from app.utils.laser_utils.laser_center_searcher import PointSearcher

from typing import *
import cv2
import numpy as np

class LaserContours:
    @staticmethod
    def get_laser_contours(originalFrame: np.ndarray, thresholdedImage: np.ndarray, sortedContours: List[np.ndarray]) -> List[Tuple[int, int]]:
        lasersContours, _ = cv2.findContours(thresholdedImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        searchedPoints = [PointSearcher.GetCenter(laser) for laser in lasersContours]
        target_rects = [cv2.boundingRect(contour) for contour in sortedContours]

        validPoints: List[Tuple[int, int]] = [] #Список для хранения найденных точек. Индексацию начинаем с 1 (ключ) и т.д.

        for targetContourIndex in range(len(sortedContours)):
            x, y, w, h = target_rects[targetContourIndex]

            for laser_index in range(len(searchedPoints)):
                if searchedPoints[laser_index] is not None and (not (x <= searchedPoints[laser_index][0] <= x + w
                                                                     and y <= searchedPoints[laser_index][1] <= y + h)):
                    continue

                isInside = cv2.pointPolygonTest(sortedContours[targetContourIndex], searchedPoints[laser_index], False)

                if LaserConfig.MIN_LASER_CONTOUR <= cv2.contourArea(lasersContours[laser_index]) <= LaserConfig.MAX_LASER_CONTOUR and isInside >= 0:
                    ContourDrawer.draw_valid_shape_contour(originalFrame, lasersContours[laser_index])
                    validPoints.append(searchedPoints[laser_index])
                    break

        return validPoints