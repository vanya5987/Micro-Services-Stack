from app.entitys.exercise_types.exercise_type.obzr_type_entity import ObzrType
from app.entitys.exercise_types.exercise_type.gto_type_entity import GtoType
from app.entitys.exercise_types.exercise_type.liberty_type_entity import LibertyType
from app.entitys.exercise_types.data_uploader.gto_data_uploader_entity import GtoDataUploader
from app.entitys.exercise_types.data_uploader.obzr_data_uploader_entity import ObzrDataUploader
from app.entitys.exercise_types.data_uploader.liberty_data_uploader_entity import LibertyDataUploader
from shared.configs.keys_configs.json_key_config import JsonKeyConfig

from app.utils.exercise_type_utils.exercise_data_uploader import ExerciseDataUploader
from app.entitys.laser_procession_entity import LaserProcessionParams
from app.utils.coins_utils.coins_converter import CoinsConverter
from app.presenters.json_presenter import JsonPresenter

from typing import *


class ShootByTypeCalculator:
    @staticmethod
    def calculate_shot_by_type(laser_procession_params: LaserProcessionParams, isLaserInsideContour: bool):
        player_id = laser_procession_params.player_id

        if player_id <= laser_procession_params.shooting_session_params.player_count:
            coins: List[int] = []
            ShootByTypeCalculator._check_shoot_is_last(laser_procession_params, coins)

            laser_is_processed, validated_point = CoinsConverter.convert_coin_by_type(coins, player_id,
                                                                                      laser_procession_params.shooting_session_processing.shooting_mods,
                                                                                      isLaserInsideContour)

            if laser_is_processed:
                ShootByTypeCalculator._apply_type_settings(laser_procession_params, validated_point)

        ShootByTypeCalculator._check_bullet_is_end(laser_procession_params)

    @staticmethod
    def _apply_type_settings(laser_procession_params: LaserProcessionParams, validatedPoint: int):
        laser_procession_params.player_params[
            laser_procession_params.player_id].last_trigger_time = laser_procession_params.current_time  # Обновляем таймер.

        countdownTimerParams: Tuple[
            bool, int, int] = laser_procession_params.program_start_timer.GetCountdownStatus()

        gto_type = GtoType(laser_procession_params, validatedPoint)
        obzr_type = ObzrType(laser_procession_params, validatedPoint)
        liberty_type = LibertyType(laser_procession_params, validatedPoint)

        gto_uploader = GtoDataUploader(laser_procession_params, gto_type)
        obzr_uploader = ObzrDataUploader(laser_procession_params, obzr_type)
        liberty_uploader = LibertyDataUploader(laser_procession_params, liberty_type)

        ExerciseDataUploader.upload_data_by_time(countdownTimerParams,
                                                 laser_procession_params.shooting_session_params,
                                                 gto_uploader, obzr_uploader)

        ExerciseDataUploader.upload_liberty_data_type(liberty_uploader)

    @staticmethod
    def _check_shoot_is_last(laser_procession_params: LaserProcessionParams, coins: List[int]):
        isLastShoot: bool = laser_procession_params.bullet_count_calculator.CheckBulletIsLast(
            laser_procession_params.player_id,
            laser_procession_params.player_params)

        if isLastShoot:
            laser_procession_params.coins_adder.add_coins(
                laser_procession_params.shooting_session_processing.centers[laser_procession_params.player_id],
                laser_procession_params.shooting_session_processing.radii, laser_procession_params.laser, coins)

    @staticmethod
    def _check_bullet_is_end(laser_procession_params: LaserProcessionParams):
        if (len(laser_procession_params.bullet_count_calculator.zeroBulletStatusShown)
                == laser_procession_params.shooting_session_params.player_count):
            laser_procession_params.shooting_session_params.is_bullet_not = True
            JsonPresenter.get_instance().update_any_shooting_states_key(JsonKeyConfig.SHOOTING_IS_STOP[0], True)
