from app.services.bullet_servies.bullets_calculator import BulletsCalculator
from app.services.coins_services.coins_adder import CoinsAdder
from app.services.target_services.target_is_validate import TargetIsValidate

from app.utils.draw_utils.contour_drawer import ContourDrawer
from app.utils.laser_utils.laser_position_checker import LaserPositionChecker
from app.utils.validators.mods_validators.check_mode_type import CheckModeType

from app.presenters.sound_presenter import SoundPresenter

from app.utils.formaters.string_format import StringFormat
from app.utils.formaters.program_start_timer import ProgramStartTimer
from app.utils.laser_utils.shoot_by_type_calculator import ShootByTypeCalculator
from app.utils.laser_utils.inside_laser_calculator import InsideLaserCalculator

from shared.configs.core_configs.target_config.GameTargetContainer import GameTargetContainer
from shared.configs.core_configs.exercise_config import ExerciseContainer

from app.entitys.target_params_entity import TargetParams
from app.entitys.processing_entity.base_shooting_processing_entity import BaseShootingProcessing
from app.entitys.session_entity.shooting_session_entity import ShootingSessionParams
from app.entitys.session_entity.player_params_entity import PlayerParams
from app.entitys.laser_procession_entity import LaserProcessionParams

from typing import *
import time


class PlayerHandler:
    def __init__(self, coinsAdder: CoinsAdder, delay: int, playersCount: int, bulletsCount: int, exerciseType: int,
                 shootTimeThreshold: str):
        self.laserPositionChecker = LaserPositionChecker()
        self.target_is_validate = TargetIsValidate(delay)
        self.bullet_calculator = BulletsCalculator()

        self.programStartTimer = ProgramStartTimer()
        self.coinsAdder = coinsAdder

        self.gameTargetContainer = GameTargetContainer()

        self.player_params: Dict[int, PlayerParams] = {playerId: PlayerParams(self.gameTargetContainer, bulletsCount)
                                                       for playerId in range(1, playersCount + 1)}
        self.shooting_session_params = ShootingSessionParams(playersCount, exerciseType, bulletsCount,
                                                             shootTimeThreshold)

        if ExerciseContainer.INVALID_TIME_FORMAT != self.shooting_session_params.shoot_time_threshold:
            self.shootingTime: Tuple[List[int], bool] = StringFormat.parse_time_format_to_int(shootTimeThreshold)
            self.programStartTimer.StartCountdown(minutes=self.shootingTime[0][0], seconds=self.shootingTime[0][1])

    # Применяет настройки для целей.
    def ApplySettingToPlayer(self, shooting_session_entity: BaseShootingProcessing) -> None:
        currentCoins: Dict[int, int] = {playerId: 0 for playerId in
                                        range(1, len(self.player_params) + 1)}
        currentTime: int = int(time.time() * 1000)

        for playerId, (laser, _) in shooting_session_entity.player_to_laser.items():
            target_entity: TargetParams = TargetParams(playerId, shooting_session_entity.centers,
                                                       shooting_session_entity.radii, currentTime, self.player_params,
                                                       laser)

            if not self.target_is_validate.target_is_validate(target_entity):
                continue

            isLaserInsideContour, coin = InsideLaserCalculator.check_laser_is_inside_contour(shooting_session_entity, playerId,
                                                                                 laser)

            if CheckModeType.check_game_mode(shooting_session_entity):  # Игровая - мишень.
                if isLaserInsideContour:
                    if self.player_params[playerId].random_point == GameTargetContainer.GAME_TARGET_TEMPLATE[coin - 1]:
                        currentCoins[playerId] = 1
                    else:
                        currentCoins[playerId] = -1
                else:
                    currentCoins[playerId] = 0

                if shooting_session_entity.shooting_mods.shoot_is_start:
                    self.player_params[playerId].random_point = self.gameTargetContainer.get_random_point()

                    if self.player_params[
                        playerId].bullets > 0 and self.shooting_session_params.bullets_count_iterator < self.shooting_session_params.bullet_count:
                        SoundPresenter.get_instance().PlaySoundByShootIndex(self.player_params[playerId].random_point)
                        self.shooting_session_params.bullets_count_iterator += 1

            if shooting_session_entity.shooting_mods.shoot_is_start:
                self.programStartTimer.StartShootTimer()

                laser_procession_params = LaserProcessionParams(playerId, laser, currentTime, currentCoins,
                                                                shooting_session_entity,
                                                                self.shooting_session_params, self.player_params,
                                                                self.programStartTimer,
                                                                self.bullet_calculator, self.coinsAdder)

                ShootByTypeCalculator.calculate_shot_by_type(laser_procession_params, isLaserInsideContour)

            ContourDrawer.draw_laser_point(shooting_session_entity.contour_image, laser)

        ContourDrawer.show_player_info(shooting_session_entity)
