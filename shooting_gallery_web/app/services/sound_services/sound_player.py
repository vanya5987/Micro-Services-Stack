from shared.pathings.path_config import PathConfig
from app.presenters.json_presenter import JsonPresenter
from app.entitys.session_entity.player_params_entity import PlayerParams
from shared.configs.keys_configs.exceptional_keys import ExceptionalKeys
from shared.configs.keys_configs.target_name_keys import TargetNameKeys
from app.entitys.shooting_mods import ShootingMods
from shared.configs.keys_configs.json_key_config import JsonKeyConfig

from typing import *
from random import randint
import pygame
import asyncio


class SoundPlayer:
    def __init__(self):
        self.pathContainer = PathConfig()
        self.jsonLoader = JsonPresenter.get_instance()

        self.mixer_is_initialize: bool = False

        try:
            pygame.mixer.init()  # Инициализация микшера pygame.
            self.mixer_is_initialize = True
        except:
            pass

    def PlaySound(self, filePath: str) -> None:
        if self.mixer_is_initialize:
            settingsData: Dict[str, Union[str, bool, int, List[int]]] = self.jsonLoader.read_json_file(
                PathConfig.PROGRAM_SETTINGS_JSON_PATH)

            volume: float = settingsData[JsonKeyConfig.SOUND_VALUE[0]] / 100

            sound = pygame.mixer.Sound(filePath)
            sound.set_volume(volume)
            sound.play()

    def GetSoundState(self) -> bool:
        settingsData: Dict[str, Union[str, bool, int, List[int]]] = self.jsonLoader.read_json_file(
            PathConfig.PROGRAM_SETTINGS_JSON_PATH)

        return settingsData[JsonKeyConfig.SOUND_IS_ENABLE[0]]

    def PlayStopSound(self):
        if self.GetSoundState():
            self.PlaySound(PathConfig().program_sounds_path[ExceptionalKeys.END_KEY])

    def PlayStartSound(self):
        if self.GetSoundState():
            self.PlaySound(PathConfig().program_sounds_path[ExceptionalKeys.FIRE_KEY])

    def PlaySoundByShootIndex(self, selectedSoundIndex: int) -> None:
        if self.GetSoundState():
            self.PlaySound(self.pathContainer.get_game_target_sounds_paths()[selectedSoundIndex])

    def PlayRandomShootsSound(self) -> None:
        if self.GetSoundState():
            self.PlaySound(self.pathContainer.shoot_sounds_path[randint(1, 5)])

    def PlayButtonClickSound(self):
        if self.GetSoundState():
            self.PlaySound(self.pathContainer.ui_sounds_path[ExceptionalKeys.CLICK_KEY])

    def PlayCountdownSound(self):
        if self.GetSoundState():
            self.PlaySound(self.pathContainer.ui_sounds_path[ExceptionalKeys.COUNTDOWN_KEY])

    def _play_first_game_sound(self, targetName: str, player_params: Dict[int, PlayerParams]):
        if targetName == f"{TargetNameKeys.GAME_25_KEY}.png" or targetName == f"{TargetNameKeys.GAME_50_KEY}.png":
            self.PlaySoundByShootIndex(
                player_params[1].random_point)  # Проигрывается всегда для единственного пользователя.

    async def play_first_sound(self, shooting_mods: ShootingMods,
                               programSettings: Dict[str, Union[str, List[int], bool]],
                               first_game_point_is_play: bool,
                               player_params: Dict[int, PlayerParams]):

        if not first_game_point_is_play and not programSettings[JsonKeyConfig.IS_CALIBRATION_MODE[0]]:
            if shooting_mods.shoot_is_start:
                await asyncio.sleep(1.0)
                self._play_first_game_sound(programSettings[JsonKeyConfig.TARGET_FILE_NAME[0]], player_params)
                first_game_point_is_play = True

                return first_game_point_is_play

        return first_game_point_is_play
