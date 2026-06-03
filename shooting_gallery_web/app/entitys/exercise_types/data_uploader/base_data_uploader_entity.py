from app.entitys.session_entity.shooting_session_entity import ShootingSessionParams
from app.entitys.session_entity.player_params_entity import PlayerParams
from app.services.sound_services.sound_player import SoundPlayer
from app.utils.formaters.program_start_timer import ProgramStartTimer
from app.entitys.laser_procession_entity import LaserProcessionParams

from dataclasses import dataclass
from typing import Dict


@dataclass
class BaseDataUploader:
    laser_procession_params: LaserProcessionParams

    def __post_init__(self):
        self.shooting_session_params: ShootingSessionParams = self.laser_procession_params.shooting_session_params
        self.player_params: Dict[int, PlayerParams] = self.laser_procession_params.player_params
        self.sound_player: SoundPlayer = self.laser_procession_params.sound_presenter
        self.program_start_timer: ProgramStartTimer = self.laser_procession_params.program_start_timer
