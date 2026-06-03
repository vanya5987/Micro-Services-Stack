from app.entitys.session_entity.player_params_entity import PlayerParams

from dataclasses import dataclass
from typing import *

@dataclass
class TargetParams:
    playerId: int
    centers: Dict[int, Tuple[int, int]]
    radii: List[float]
    currentTime: int
    player_params: Dict[int, PlayerParams]
    laser: Tuple[int, int]