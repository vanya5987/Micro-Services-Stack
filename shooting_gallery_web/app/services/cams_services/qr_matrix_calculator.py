from app.services.qr_services.qr_launcher import QrLauncher
from app.utils.formaters.generic_converter import GenericConverter
from app.entitys.shooting_mods import ShootingMods

from typing import Dict, List
import numpy as np

class QrMatrixCalculator:
    def __init__(self, qr_launcher: QrLauncher):
        self.qr_launcher = qr_launcher
        self.matrix_contours = {}

    #Получаем все матрицы и контуры для текущей мишени.
    def calculate_qr_matrix(self, sortedContoursForAllPlayer: Dict[int, np.ndarray], contourImage: np.ndarray,
                            targetMask: np.ndarray, current_targets_names: Dict[int, str], shooting_mods: ShootingMods):
        if shooting_mods.is_calibration_mode:
            matrix_contours: Dict[int, List[np.ndarray]] = {}

            for temporary_player_id, contour in sortedContoursForAllPlayer.items():
                contourImage, matrix_contour = self.qr_launcher.find_target_by_qr_code(contourImage, targetMask,
                                                                                  contour, temporary_player_id,
                                                                                  current_targets_names)

                matrix_contours[temporary_player_id] = matrix_contour

            self.matrix_contours = GenericConverter.convert_generic(matrix_contours, self.matrix_contours, True)

        return self.matrix_contours