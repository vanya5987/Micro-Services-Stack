from app.utils.licence_utils.pass_generator import PassGenerator
from app.utils.licence_utils.encryptor import Encryptor

from app.presenters.json_presenter import JsonPresenter
from shared.pathings.path_config import PathConfig
from shared.configs.keys_configs.json_key_config import JsonKeyConfig

from typing import List

class DecodeConfig:
    def __init__(self):
        self.jsonLoader = JsonPresenter.get_instance()

        mask_id: int = PassGenerator.get_mask_key_by_mac(self.jsonLoader.read_json_file(
            PathConfig.LICENCE_JSON_PATH)[JsonKeyConfig.LICENCE_KEY[0]])

        self.template: List[str] = ["12", "Ty", "m5", "9K", "95", "mM"]

        self.pass_collection: str = PassGenerator.get_uuid_template(mask_id)

    # Создает ключ лицензии.
    def CreateLicencePass(self) -> str:
        raw = self.template[3] + self.pass_collection[4] + self.template[2] + self.pass_collection[1] + self.pass_collection[5] + self.template[1] + "aa"

        return Encryptor.pass_key_sha_converter(raw)[:10] + "aa"

    # Создает хэш - пароль для валидации.
    def CreateStrippedHash(self, licence_code: str = None) -> str:
        if licence_code is None:
            licence_code: str = self.CreateLicencePass()[:10]

        licence_code = "".join(self.template) + licence_code[3] + licence_code[4] + licence_code[7] + licence_code[8] + licence_code[
            9] + licence_code[9] + "".join(self.template)

        return Encryptor.pass_key_sha_converter(licence_code)[:10]

    # Получаем текущее состояние лицензии.
    def GetPassState(self):
        if self.jsonLoader.read_json_file(PathConfig.LICENCE_JSON_PATH)[
            "licenceKey"] == self.CreateStrippedHash():
            return True
        return False
