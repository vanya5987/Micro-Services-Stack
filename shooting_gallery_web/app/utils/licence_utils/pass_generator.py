from shared.configs.core_configs.licence_config import LicenceConfig
from app.utils.licence_utils.encryptor import Encryptor

import random
import psutil


class PassGenerator:
    _MASKS = LicenceConfig.MASKS

    @staticmethod
    def get_user_name_part() -> str:
        username = psutil.users()[0].name

        if len(username) > 2:
            user_part = (username * 7)[:6]
        else:
            user_part = (PassGenerator._MASKS[0] * 7)[:6]

        return user_part

    @staticmethod
    def get_user_part_compose(part: str):
        return PassGenerator.get_user_name_part() + part

    @staticmethod
    def get_uuid_template(mask_key: int = None) -> str:

        if mask_key is not None:
            if mask_key not in PassGenerator._MASKS:
                raise ValueError(mask_key)
            mask_value = PassGenerator._MASKS[mask_key]
        else:
            mask_value = random.choice(list(PassGenerator._MASKS.values()))

        return PassGenerator.get_user_part_compose(mask_value)

    @staticmethod
    def get_mask_key_by_mac(double_encrypt_str: str):
        if len(double_encrypt_str) != 10:
            return None

        for key, value in PassGenerator._MASKS.items():
            raw_pass = PassGenerator.get_user_part_compose(value)

            raw_pass = Encryptor.pass_key_sha_converter(raw_pass)[:10] + "aa"
            raw_pass = Encryptor.pass_key_sha_converter(raw_pass)[:10]

            if raw_pass == double_encrypt_str:
                return key

        return None