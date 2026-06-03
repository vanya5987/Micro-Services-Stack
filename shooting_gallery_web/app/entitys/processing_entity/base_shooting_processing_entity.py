from app.entitys.shooting_mods import ShootingMods

from dataclasses import dataclass
import numpy as np
from typing import *


@dataclass
class BaseShootingProcessing:
    player_to_laser: Dict[int, Tuple[Tuple[int, int], float]]
    centers: Dict[int, Tuple[int, int]]
    radii: List[float]
    contour_image: np.ndarray
    sorted_contours: Dict[int, np.ndarray]
    shooting_mods: ShootingMods
    target_scale: Union[List[float], bool]
    abstract_laser_points: Dict[int, Tuple[int, int]]
    valid_contour_matrix: Dict[int, bool]
    program_settings: Dict[str, Union[str, List[int], bool]]
