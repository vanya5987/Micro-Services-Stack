from shared.configs.core_configs.qr_config import QrConfig

from typing import List

import numpy as np
import cv2

class QrSearcher:
    def __init__(self, min_contour_length: int, max_contour_length: int):
        self.min_contour_length: int = min_contour_length
        self.max_contour_length: int = max_contour_length

        self.matrix_size: int = QrConfig.MATRIX_SIZE
        self.half_coef: int = QrConfig.HALF_COEF
        self.approx_coef: float = QrConfig.APPROX_COEF
        self.max_angle_count: int = QrConfig.MAX_ANGLE_COUNT

    #Декодирует картинку.
    def decode_image(self, image: np.ndarray, pixel_threshold: int, bounding_box: np.ndarray):
        all_matrix: List[List[List[bool]]] = []
        find_contours: List[np.ndarray] = []

        if image is None:
            return ([], [])

        contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            matrix: List[List[bool]] = []
            epsilon = self.approx_coef * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            contourArea: float = cv2.contourArea(contour)

            if (self._is_contour_inside_box(contour, bounding_box) and len(approx) == self.max_angle_count and
                    self.min_contour_length < contourArea < self.max_contour_length):
                x, y, width, height = cv2.boundingRect(approx)
                width_part = width // self.matrix_size
                height_part = height // self.matrix_size

                for row_index in range(self.matrix_size):
                    row: list[bool] = []

                    for column_index in range(self.matrix_size):
                        center_x: int = x + column_index * width_part + width_part // self.half_coef
                        center_y: int = y + row_index * height_part + height_part // self.half_coef

                        pixel_value = image[center_y, center_x]
                        is_black = pixel_value < pixel_threshold
                        row.append(bool(is_black))

                    matrix.append(row)

                all_matrix.append(matrix)
                find_contours.append(contour)

        return all_matrix, find_contours

    def _is_contour_inside_box(self, contour: np.ndarray, bounding_box: np.ndarray) -> bool:
        x, y, width, height = cv2.boundingRect(contour)

        center_x: int = x + width // self.half_coef
        center_y: int = y + height // self.half_coef

        return cv2.pointPolygonTest(bounding_box, (center_x, center_y), False) >= 0