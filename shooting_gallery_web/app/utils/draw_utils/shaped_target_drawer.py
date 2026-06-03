from app.utils.draw_utils.contour_drawer import ContourDrawer
from app.entitys.processing_entity.draw_processing_entity import DrawShootingProcessing

from shared.configs.keys_configs.json_key_config import JsonKeyConfig

import numpy as np
from typing import *

class ShapedTargetDrawer:
    # Рисуем контуры enable/disable.
    @staticmethod
    def draw_target_outline_by_type(shooting_session: DrawShootingProcessing,
                                     matrix_contours: Dict[int, List[np.ndarray]]):
        for player_contour_id, contour in shooting_session.sorted_contours.items():
            for target_contour_id, target_name in shooting_session.current_targets_names.items():
                if target_contour_id in matrix_contours and target_contour_id in shooting_session.sorted_contours and target_contour_id in shooting_session.centers:
                    if player_contour_id == target_contour_id:
                        if f"{target_name}.png" == shooting_session.program_settings[JsonKeyConfig.TARGET_FILE_NAME[0]]:
                            ContourDrawer.draw_valid_shape_contour(shooting_session.contour_image, contour)
                            shooting_session.valid_contour_matrix[player_contour_id] = True
                        else:
                            ContourDrawer.draw_invalid_shape_contour(shooting_session.contour_image, contour)
                            shooting_session.valid_contour_matrix[player_contour_id] = False

    # Рисуем QR коды.
    @staticmethod
    def _draw_qr_codes(shooting_session: DrawShootingProcessing, matrix_contours: Dict[int, List[np.ndarray]]):
        for player_index, matrix_contour in matrix_contours.items():
            if player_index in shooting_session.sorted_contours:
                if player_index in matrix_contours and player_index in shooting_session.centers:
                    if (len(shooting_session.valid_contour_matrix) == len(shooting_session.valid_contour_matrix)
                            and matrix_contours[player_index]):
                        [ContourDrawer.draw_qr_code_contour(shooting_session.contour_image, contour) for contour in
                         matrix_contour]
            else:
                del matrix_contours[player_index]