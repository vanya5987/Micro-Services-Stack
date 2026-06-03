from app.entitys.exercise_types.exercise_type.base_exercise_type_entity import BaseExerciseType
from shared.configs.core_configs.exercise_config import ExerciseContainer

from dataclasses import dataclass


@dataclass
class LibertyType(BaseExerciseType):
    exercise_type: int = ExerciseContainer.LIBERTY_EXERCISE_TYPE
