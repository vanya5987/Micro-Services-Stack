from shared.configs.core_configs.decode_config import DecodeConfig
from shared.configs.keys_configs.http_keys_configs import HttpKeysConfig

from typing import Tuple, Dict
import httpx


class HttpHandler:
    def __init__(self):
        self.decode_config = DecodeConfig()
        self.httpKeysContainer = HttpKeysConfig()

    # Делает запрос к серверу и получает ответ в json.
    def GetHttpForJson(self, number: int) -> Tuple[Dict[str, str], str]:
        api_key: str = "6a848a929e5ec825914aff88a9b13dd6f4d75485ce117effe9c8b7f6e7ece0bb"
        licenceCode: str = self.decode_config.CreateLicencePass()
        softwareType: str = self.decode_config.CreateLicencePass()[-2:]

        headers = {
            "Authorization": f"Bearer {api_key}",
        }

        with httpx.Client() as client:
            response = client.get(
                f"https://api.algkod.com?dogovor_number={number}&license_code"
                f"={licenceCode}&software_type={softwareType}",
                headers=headers
            )
            return response.json(), licenceCode

    def GetJsonWithExceptionCode(self, documentNumber: int) -> Tuple[Dict[str, str], int]:
        try:
            data, licenceCode = self.GetHttpForJson(documentNumber)
        except:
            return self.httpKeysContainer.GetDefaultHttpData(), 3  # Код ошибки, нет интернета.

        if self.httpKeysContainer.GetErrorKey() in data:
            return data, 0  # Код ошибки получения данных (Данных нет).
        elif data[self.httpKeysContainer.GetLicenceCodeKey()] == licenceCode:
            return data, 1  # Код корректной регистрации/получения.
        else:
            return data, 2  # Код ошибки валидации входных данных.
