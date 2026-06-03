from typing import Dict,List

class QrConfig:
    MATRIX_SIZE: int = 5
    BIT_COUNT: int = 9
    PIXEL_SIZE: int = 400
    BORDER_SIZE: int = 200

    HALF_COEF: int = 2
    APPROX_COEF: float = 0.02
    MAX_ANGLE_COUNT: int = 4

    MIN_MATRIX_VALUE: int = 0
    MAX_MATRIX_VALUE: int = 511

    OUTLINE_INDEXES: List[List[bool]] = [
            [True, True, True, True, True],
            [True, False, False, False, True],
            [True, False, False, False, True],
            [True, False, False, False, True],
            [True, True, True, True, True]]

    TARGET_TYPES: Dict[str, int] = {
            "ГТО_5": 20,  "ГТО_10": 10,
            "Пистолетная_25": 22, "Пистолетная_50": 5,
            "Пистолетная_75": 60, "Пистолетная_100": 25,
            "Army_25": 26, "Army_50": 50,
            "Army_75": 28, "Army_100": 70,
            "IDPA_25": 80, "IDPA_50": 150,
            "IDPA_100": 130, "IDPA_150": 33,
            "IDPA_200": 34, "IDPA_500": 200,
            "Game_25": 36, "Game_50": 140}