from shared.configs.core_configs.qr_config import QrConfig
from shared.pathings.path_config import PathConfig

from typing import List
import numpy as np
import os
import cv2

class QrImageSaver:
    def __init__(self):
        self.pixel_size: int = QrConfig.PIXEL_SIZE
        self.border_size: int = QrConfig.BORDER_SIZE

    def save_qr_image(self, file_name: str, matrix: List[List[bool]]) -> None:
        image_size = (QrConfig.MATRIX_SIZE * self.pixel_size + 2 * self.border_size)

        image = np.ones((image_size, image_size, 3), dtype=np.uint8) * 255

        for y in range(QrConfig.MATRIX_SIZE):
            for x in range(QrConfig.MATRIX_SIZE):
                if QrConfig.OUTLINE_INDEXES[y][x]:
                    color = (0, 0, 0)
                else:
                    color = (0, 0, 0) if matrix[y][x] else (255, 255, 255)

                start_x = self.border_size + x * self.pixel_size
                start_y = self.border_size + y * self.pixel_size
                end_x = start_x + self.pixel_size
                end_y = start_y + self.pixel_size

                cv2.rectangle(image, (start_x, start_y), (end_x, end_y), color, -1)

        filename = f"{file_name}q.jpg"
        filepath = os.path.join(PathConfig.QR_IMAGES, filename)

        success: bool = cv2.imwrite(filepath, image)

        if success:
            print(f"Image has been saved: {filepath}")
        else:
            print(f"Image save error: {filepath}")
