from dataclasses import dataclass, field
from typing import List
from shared.configs.core_configs.target_config.GameTargetContainer import GameTargetContainer


@dataclass
class PlayerParams:
    game_target_container: GameTargetContainer
    bullets: int

    coins: int = 0
    last_trigger_time: int = 0
    random_point: int = field(init=False)
    type_iterator: int = 0
    all_coins: List[int] = field(default_factory=list)
    all_times: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.random_point = self.game_target_container.get_random_point()
