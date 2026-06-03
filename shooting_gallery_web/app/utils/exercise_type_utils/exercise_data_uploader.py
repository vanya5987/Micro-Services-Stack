from app.entitys.exercise_types.exercise_type.gto_type_entity import GtoType
from app.entitys.exercise_types.exercise_type.obzr_type_entity import ObzrType
from app.entitys.exercise_types.exercise_type.liberty_type_entity import LibertyType

from app.entitys.session_entity.shooting_session_entity import ShootingSessionParams
from app.presenters.json_presenter import JsonPresenter
from shared.configs.core_configs.exercise_config import ExerciseContainer
from shared.configs.keys_configs.json_key_config import JsonKeyConfig

from app.entitys.exercise_types.data_uploader.gto_data_uploader_entity import GtoDataUploader
from app.entitys.exercise_types.data_uploader.obzr_data_uploader_entity import ObzrDataUploader
from app.entitys.exercise_types.data_uploader.liberty_data_uploader_entity import LibertyDataUploader

from typing import Union, Tuple


class ExerciseDataUploader:
    @staticmethod
    def _upload_data_by_exercise_type(data_uploader: Union[GtoDataUploader, ObzrDataUploader]):
        json_controller = JsonPresenter.get_instance()

        base_exercise_type: Union[GtoType, ObzrType] = data_uploader.base_exercise_type
        index: int = base_exercise_type.player_id

        if data_uploader.shooting_session_params.exercise_type == base_exercise_type.exercise_type:
            if data_uploader.player_params[index].type_iterator < base_exercise_type.training_bullets:
                data_uploader.player_params[index].type_iterator += 1
                data_uploader.player_params[index].all_coins.append(base_exercise_type.current_coins[index])
                json_controller.update_session_keys(index, base_exercise_type.shooting_session_entity,
                                                    data_uploader.player_params, data_uploader.program_start_timer)

                data_uploader.sound_player.PlayRandomShootsSound()
            else:
                base_exercise_type.current_coins[index] = base_exercise_type.validated_point
                data_uploader.player_params[index].coins += base_exercise_type.validated_point
                data_uploader.player_params[index].all_coins.append(base_exercise_type.current_coins[index])
                json_controller.update_session_keys(index, base_exercise_type.shooting_session_entity,
                                                    data_uploader.player_params, data_uploader.program_start_timer)

                data_uploader.sound_player.PlayRandomShootsSound()

    @staticmethod
    def upload_liberty_data_type(data_uploader: LibertyDataUploader):
        json_controller = JsonPresenter.get_instance()

        liberty_exercise_type: LibertyType = data_uploader.base_exercise_type
        index: int = liberty_exercise_type.player_id

        if data_uploader.shooting_session_params.exercise_type == ExerciseContainer.LIBERTY_EXERCISE_TYPE:  # Вычисления для свободного режима.
            if not liberty_exercise_type.shooting_session_entity.shooting_mods.game_mode:  # Режим игровой мишени выключен.
                liberty_exercise_type.current_coins[index] = liberty_exercise_type.validated_point
                data_uploader.player_params[index].coins += liberty_exercise_type.validated_point
                data_uploader.player_params[index].all_coins.append(liberty_exercise_type.validated_point)
                json_controller.update_session_keys(index, liberty_exercise_type.shooting_session_entity,
                                                    data_uploader.player_params,
                                                    data_uploader.program_start_timer)

                data_uploader.sound_player.PlayRandomShootsSound()
            else:  # Режим игровой мишени включен.
                data_uploader.player_params[index].coins += liberty_exercise_type.current_coins[index]
                data_uploader.player_params[index].all_coins.append(liberty_exercise_type.current_coins[index])
                json_controller.update_session_keys(index, liberty_exercise_type.shooting_session_entity,
                                                    data_uploader.player_params,
                                                    data_uploader.program_start_timer)

    @staticmethod
    def upload_data_by_time(countdownTimerParams: Tuple[bool, int, int], shooting_session_params: ShootingSessionParams,
                            gto_uploader: GtoDataUploader, obzr_uploader: ObzrDataUploader):
        json_controller = JsonPresenter.get_instance()

        if (countdownTimerParams[0] == False and countdownTimerParams[1] > 0 and countdownTimerParams[2] > 0 and
                shooting_session_params.time_is_end == False):
            ExerciseDataUploader._upload_data_by_exercise_type(gto_uploader)
            ExerciseDataUploader._upload_data_by_exercise_type(obzr_uploader)
        else:
            shooting_session_params.time_is_end = True

            if countdownTimerParams[0] == False and countdownTimerParams[1] == 0 and countdownTimerParams[2] == 0:
                ExerciseDataUploader._upload_data_by_exercise_type(obzr_uploader)

        if shooting_session_params.time_is_end == True and countdownTimerParams[0] == True:
            json_controller.update_any_shooting_states_key(JsonKeyConfig.SHOOTING_IS_STOP[0], True)

        return shooting_session_params.time_is_end
