from app.utils.laser_utils.laser_position_checker import LaserPositionChecker
from app.entitys.target_params_entity import TargetParams


class TargetIsValidate:
    def __init__(self, delay: int):
        self.delay: int = delay

    # Проверяет валидность цели.
    def target_is_validate(self, target_entity: TargetParams) -> bool:
        if not target_entity.playerId in target_entity.centers:
            return False

        if not target_entity.playerId in target_entity.player_params:
            return False

        if target_entity.radii is None:
            return False
        if target_entity.currentTime - target_entity.player_params[
            target_entity.playerId].last_trigger_time < self.delay:
            return False

        return LaserPositionChecker.check_laser_position_to_player(target_entity,
                                                                   target_entity.centers[target_entity.playerId])
