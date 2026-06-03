from app.services.bullet_servies.bullets_calculator import BulletsCalculator
from app.services.coins_services.coins_adder import CoinsAdder
from app.utils.formaters.program_start_timer import ProgramStartTimer

from app.entitys.processing_entity.base_shooting_processing_entity import BaseShootingProcessing
from app.entitys.session_entity.shooting_session_entity import ShootingSessionParams
from app.entitys.session_entity.player_params_entity import PlayerParams
from app.presenters.sound_presenter import SoundPresenter

from dataclasses import dataclass

from typing import *


@dataclass
class LaserProcessionParams:
    player_id: int
    laser: Tuple[int, int]
    current_time: int
    current_coins: Dict[int, int]
    shooting_session_processing: BaseShootingProcessing
    shooting_session_params: ShootingSessionParams
    player_params: Dict[int, PlayerParams]
    program_start_timer: ProgramStartTimer
    bullet_count_calculator: BulletsCalculator
    coins_adder: CoinsAdder
    sound_presenter = SoundPresenter.get_instance()
