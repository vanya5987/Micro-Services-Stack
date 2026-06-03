from app.presenters.json_presenter import JsonPresenter
from app.utils.formaters.string_format import StringFormat
from app.entitys.shooting_mods import ShootingMods
from shared.configs.keys_configs.json_key_config import JsonKeyConfig


class ShootingDateSetter:
    @staticmethod
    def set_shooting_date(shooting_mods: ShootingMods, shootingDateIsSet: bool):
        json_controller = JsonPresenter.get_instance()

        if shooting_mods.shoot_is_start:
            if not shootingDateIsSet:
                json_controller.update_any_shooting_states_key(JsonKeyConfig.SHOOTING_DATE[0],
                                                               StringFormat.create_shooting_date())
                shootingDateIsSet = True

        return shootingDateIsSet
