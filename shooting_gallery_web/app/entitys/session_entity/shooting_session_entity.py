from dataclasses import dataclass

@dataclass
class ShootingSessionParams:
    player_count: int
    exercise_type: int
    bullet_count: int
    shoot_time_threshold: str

    is_bullet_not: bool = False
    time_is_end: bool = False
    bullets_count_iterator: int = 1
