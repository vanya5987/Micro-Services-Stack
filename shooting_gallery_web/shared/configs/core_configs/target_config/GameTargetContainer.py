# Библиотеки.
from typing import *
import random


# Библиотеки.

class GameTargetContainer:
    DRAWING_POSITION_SCALE: int = 23
    START_POINT_POSITION_SCALE: int = 5

    MIN_POINTS_COUNT: int = 0
    MAX_HORIZONTAL_POINTS_COUNT: int = 4
    MAX_VERTICAL_POINTS_COUNT: int = 6

    GAME_TARGET_TEMPLATE: List[int] = [
        8, 8, 7, 6, 3, 3,
        5, 2, 3, 2, 6, 2,
        4, 1, 4, 1, 6, 7,
        4, 5, 8, 5, 7, 1
    ]

    MIN_SOUNDS_COUNT: int = 1
    MAX_SOUNDS_COUNT: int = 8

    @staticmethod
    def get_random_point():
        return random.randint(1, 8)
