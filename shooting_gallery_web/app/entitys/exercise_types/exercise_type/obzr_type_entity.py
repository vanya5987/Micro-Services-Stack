from app.entitys.exercise_types.exercise_type.base_exercise_type_entity import BaseExerciseType
from shared.configs.core_configs.exercise_config import ExerciseContainer

from dataclasses import dataclass

@dataclass
class ObzrType(BaseExerciseType):
    exercise_type: int = ExerciseContainer.OBZR_EXERCISE_TYPE