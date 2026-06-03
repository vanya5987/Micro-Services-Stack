from app.utils.laser_utils.laser_contours import LaserContours
from app.services.contour_services.contour_handler import ContourHandler
from app.utils.cams_utils.mats_calculator import MatsCalculator
from app.controllers.PlayerHandler import PlayerHandler
from app.utils.player_utils.player_finder import PlayerFinder

from app.utils.draw_utils.shaped_target_drawer import ShapedTargetDrawer
from shared.configs.core_configs.target_config.ShootingModsGetter import ShootingModsGetter
from app.entitys.shooting_mods import ShootingMods

from app.utils.time_utils.shooting_date_setter import ShootingDateSetter
from app.services.qr_services.qr_launcher import QrLauncher
from app.services.cams_services.qr_matrix_calculator import QrMatrixCalculator
from app.entitys.processing_entity.shooting_processing_entity import ShootingProcessing
from app.entitys.processing_entity.draw_processing_entity import DrawShootingProcessing

from app.utils.formaters.generic_converter import GenericConverter
from app.presenters.sound_presenter import SoundPresenter
from app.presenters.json_presenter import JsonPresenter
from shared.configs.keys_configs.json_key_config import JsonKeyConfig
from app.utils.draw_utils.contour_drawer import ContourDrawer

from typing import *
import numpy as np
import asyncio
import time

class ScreenImageController:
    def __init__(self, contourHandler: ContourHandler,
                 target_params: List[Union[float, bool]], roiHandler: PlayerHandler, qrRangeValue: List[int],
                 player_count: int):
        self.qr_launcher = QrLauncher(qrRangeValue[0], qrRangeValue[1])
        self.qr_matrix_calculator = QrMatrixCalculator(self.qr_launcher)

        self.contourHandler = contourHandler
        self.playerHandler = roiHandler

        self.target_params: List[Union[float, bool]] = target_params
        self.current_target_names: List[str] = []
        self.player_count: int = player_count

        self.firstGamePointIsPlay: bool = False
        self.shootingDateIsSet: bool = False
        self.sortedContoursForAllPlayer = {}
        self.valid_contour_matrix = {}
        self.centers = {}
        self.last_update_time: int = 0

    async def ProcessFrame(self, frame: np.ndarray, shootingStates: Dict[str, Union[str, List[int], bool]],
                           programSettings: Dict[str, Union[str, List[int], bool]]):
        shooting_mods: ShootingMods = ShootingModsGetter.get_shooting_mods(shootingStates, programSettings,
                                                                           self.target_params)
        targetMatrix, laserMatrix = await asyncio.gather(MatsCalculator.create_target_matrix_thread(frame),
                                                         MatsCalculator.create_laser_matrix_thread(frame,
                                                                                                   programSettings[
                                                                                                       JsonKeyConfig.LASER_BRIGHTEST[0]]))

        sorted_contours, image, targetMask = await self.contourHandler.get_target_contours(targetMatrix, frame,
                                                                                                  shooting_mods)


        current_time = time.time()

        if current_time - self.last_update_time >= 0.5:
            self.last_update_time = current_time

            self.sortedContoursForAllPlayer = {
                i + 1: item for i, item in enumerate(sorted_contours)
            }

            self.centers = await self.contourHandler.get_target_centers(
                frame, targetMask, shooting_mods, self.centers
            )

        laserPoints: List[Tuple[int, int]] = LaserContours.get_laser_contours(frame, laserMatrix, sorted_contours)
        radii: List[float] = await self.contourHandler.get_target_radii(frame, targetMask, shooting_mods)

        playerToLaser, nearestLaserPoints = PlayerFinder.GetNearestPlayer(laserPoints, self.centers, radii)

        abstractLaserPoints: Dict[
            int, Tuple[int, int]] = await self.contourHandler.calculate_abstract_point_to_contours(frame,
                                                                                                   targetMask,
                                                                                                   nearestLaserPoints,
                                                                                                   shooting_mods)

        self.shootingDateIsSet = ShootingDateSetter.set_shooting_date(shooting_mods, self.shootingDateIsSet)
        self.firstGamePointIsPlay = await SoundPresenter.get_instance().play_first_sound(shooting_mods, programSettings,
                                                                                         self.firstGamePointIsPlay,
                                                                                         self.playerHandler.player_params)

        current_targets_names: Dict[int, str] = {}  # Мишени которые сейчас валидны.

        # Получаем все матрицы и контуры для текущей мишени.
        matrix_contours = self.qr_matrix_calculator.calculate_qr_matrix(self.sortedContoursForAllPlayer,
                                                                            image,
                                                                            targetMask,
                                                                            current_targets_names, shooting_mods)

        self.current_target_names = GenericConverter.convert_generic(current_targets_names,
                                                                         self.current_target_names)

        drawing_shooting_session_entity = DrawShootingProcessing(playerToLaser, self.centers, radii, image,
                                                                     self.sortedContoursForAllPlayer, shooting_mods,
                                                                     self.target_params[0], abstractLaserPoints,
                                                                     self.valid_contour_matrix, programSettings,
                                                                     self.target_params,
                                                                     self.current_target_names)

        ShapedTargetDrawer.draw_target_outline_by_type(drawing_shooting_session_entity, matrix_contours)

        # ВОТ ТУТ ПРОВОДИМ ПЕРЕСЧЕТ ДЛЯ КАЖДОГО СЛОВАРЯ!!!
        new_player_to_laser: Dict[int, Tuple[Tuple[int, int], float]] = {}
        new_centers: Dict[int, Tuple[int, int]] = {}
        filtered_contours: Dict[int, np.ndarray] = {}
        new_abstract_laser_points: Dict[int, Tuple[int, int]] = {}
        new_index: int = 1

        for old_index, target_is_enable in self.valid_contour_matrix.items():
            if target_is_enable:

                if old_index in playerToLaser:
                    new_player_to_laser[new_index] = playerToLaser[old_index]

                if len(self.centers) > 0 and old_index in self.centers and old_index in self.sortedContoursForAllPlayer:
                    new_centers[new_index] = self.centers[old_index]

                if old_index in self.sortedContoursForAllPlayer:
                    filtered_contours[new_index] = self.sortedContoursForAllPlayer[old_index]

                if old_index in abstractLaserPoints:
                    new_abstract_laser_points[new_index] = abstractLaserPoints[old_index]

                new_index += 1

        shooting_session_entity = ShootingProcessing(new_player_to_laser, new_centers, radii, image,
                                                         filtered_contours, shooting_mods,
                                                         self.target_params[0], new_abstract_laser_points,
                                                         self.valid_contour_matrix, programSettings)

        self.playerHandler.ApplySettingToPlayer(shooting_session_entity)

        if len(new_centers) == len(filtered_contours):
            JsonPresenter.get_instance().update_any_settings_value_key(JsonKeyConfig.CENTERS_COUNT[0], len(new_centers))

        text_container = ContourDrawer.get_text_container(programSettings)

        ContourDrawer.draw_target_position_message(image, text_container, programSettings, filtered_contours)

        # IdpaDrawer.permanent_draw_idpa_target(drawing_shooting_session_entity)
        # ArmyDrawer.permanent_draw_army_target(drawing_shooting_session_entity)
        # GameDrawer.permanent_draw_game_target(drawing_shooting_session_entity)

        return image
