from app.entitys.processing_entity.base_shooting_processing_entity import BaseShootingProcessing
from shared.configs.core_configs.exercise_config import ExerciseContainer
from app.entitys.laser_procession_entity import LaserProcessionParams

from dataclasses import dataclass
from typing import Dict


@dataclass
class BaseExerciseType:
    laser_procession_params: LaserProcessionParams
    validated_point: int

    training_bullets: int = ExerciseContainer.TRAINING_BULLETS

    def __post_init__(self):
        self.player_id: int = self.laser_procession_params.player_id
        self.current_coins: Dict[int, int] = self.laser_procession_params.current_coins
        self.shooting_session_entity: BaseShootingProcessing = self.laser_procession_params.shooting_session_processing
