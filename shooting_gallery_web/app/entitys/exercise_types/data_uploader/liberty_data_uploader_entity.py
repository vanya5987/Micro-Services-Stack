from app.entitys.exercise_types.exercise_type.base_exercise_type_entity import BaseExerciseType
from app.entitys.exercise_types.data_uploader.base_data_uploader_entity import BaseDataUploader

from dataclasses import dataclass


@dataclass
class LibertyDataUploader(BaseDataUploader):
    base_exercise_type: BaseExerciseType
