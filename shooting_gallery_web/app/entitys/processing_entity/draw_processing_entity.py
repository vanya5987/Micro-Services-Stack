from app.entitys.processing_entity.base_shooting_processing_entity import BaseShootingProcessing

from dataclasses import dataclass
from typing import *


@dataclass
class DrawShootingProcessing(BaseShootingProcessing):
    target_params: List[Union[float, bool]]
    current_targets_names: Dict[int, str]

    def __post_init__(self):
        if isinstance(self.current_targets_names, list):
            self.current_targets_names = {i + 1: name for i, name in enumerate(self.current_targets_names)}