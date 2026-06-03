from app.entitys.processing_entity.shooting_processing_entity import ShootingProcessing


class CheckModeType:
    @staticmethod
    def check_idpa_mode(shooting_session_entity: ShootingProcessing) -> bool:
        if (shooting_session_entity.shooting_mods.idpa_mode and len(shooting_session_entity.sorted_contours) ==
                len(shooting_session_entity.centers) and not shooting_session_entity.shooting_mods.circle_state):
            return True
        return False

    @staticmethod
    def check_army_mode(shooting_session_entity: ShootingProcessing) -> bool:
        if (shooting_session_entity.shooting_mods.army_mode and len(shooting_session_entity.sorted_contours) ==
                len(shooting_session_entity.centers) and not shooting_session_entity.shooting_mods.circle_state):
            return True
        return False

    @staticmethod
    def check_game_mode(shooting_session_entity: ShootingProcessing) -> bool:
        if (shooting_session_entity.shooting_mods.game_mode and len(shooting_session_entity.sorted_contours)
                == len(shooting_session_entity.centers) and not shooting_session_entity.shooting_mods.circle_state):
            return True
        return False
