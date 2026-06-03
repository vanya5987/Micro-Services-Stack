from dataclasses import dataclass


@dataclass
class ShootingMods:
    shoot_is_start: bool  # 0
    radius_mode: bool  # 1
    circle_state: bool  # 2
    idpa_mode: bool  # 3
    army_mode: bool  # 4
    game_mode: bool  # 5
    is_calibration_mode: bool  # 6
    is_qr_searcher_use: bool  # 7
