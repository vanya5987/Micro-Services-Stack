import numpy as np

from app.utils.draw_utils.contour_drawer import ContourDrawer
from shared.pathings.path_config import PathConfig

from app.services.qr_services.qr_searcher import QrSearcher
from app.utils.qr_utils.qr_binary_calculator import QrBinaryHandler
from shared.configs.core_configs.qr_config import QrConfig
from app.services.qr_services.qr_image_saver import QrImageSaver

from collections import Counter
from typing import List, Dict
import os

class QrLauncher:
    def __init__(self, min_contour_length: int, max_contour_length: int):
        self.path_container = PathConfig()
        self.qr_image_saver = QrImageSaver()

        self.qr_searcher = QrSearcher(min_contour_length, max_contour_length)
        self.contour_drawer = ContourDrawer()

    def find_target_by_qr_code(self, frame: np.ndarray, threshold_image: np.ndarray, contour: np.ndarray, player_id: int,
                               current_targets_names: Dict[int, str]):
        matrix_for_current_target, matrix_contours = self.qr_searcher.decode_image(threshold_image, 60, contour)
        decoded_matrix_values: List[int] = []

        for matrix in matrix_for_current_target: #Декодируем матрицы для текущей мишени.
            decoded_matrix_values.append(QrBinaryHandler.decode_with_markers(matrix))

        for key, value in QrConfig.TARGET_TYPES.items(): #Сравниваем каждую матрицу со списком предустановленных матриц.
            if len(decoded_matrix_values) > 0:
                dominate_matrix_valueCounter = Counter(decoded_matrix_values).most_common(1)[0][0]

                if dominate_matrix_valueCounter == value:
                    current_targets_names[player_id] = key #Исправить алгоритм работы.
                    break

        return frame, matrix_contours

    #Работает самостоятельно (вне цикла). Генератор QR кодов.
    def _generate_images(self):
        for text, code in QrConfig.TARGET_TYPES.items():
            delete_path = os.path.join(PathConfig.QR_IMAGES, f"{text}.png")

            try:
                os.remove(delete_path)
                print(f"{delete_path} удален!")
            except:
                print(f"Файла {delete_path} не существует!")

            self.qr_image_saver.save_qr_image(text, QrBinaryHandler.encode_number_with_markers(code))