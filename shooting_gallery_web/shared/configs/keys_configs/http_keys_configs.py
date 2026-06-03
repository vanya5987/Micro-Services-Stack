from typing import Dict

class HttpKeysConfig:
    def __init__(self):
        self.defaultData: Dict[str, str] = {'dogovor_number': "", 'license_date': "", 'license_code': "",
			 'activation_code': "", 'software_type': "", 'notes': "", 'activation_count': 0}

    #Возвращает дефолтный словарь - заглушку.
    def GetDefaultHttpData(self) -> Dict[str, str]:
        return self.defaultData

    #Возвращает ключ ошибки для полученного json по http запросу.
    def GetErrorKey(self) -> str:
        return "error"

    #Возвращает ключ договора для полученного json по http запросу.
    def GetContractKey(self) -> str:
        return "dogovor_number"

    #Возвращает ключ даты регистрации лицензии для полученного json по http запросу.
    def GetLicenceDateKey(self) -> str:
        return "license_date"

    #Возвращает ключ кода лицензии для полученного json по http запросу.
    def GetLicenceCodeKey(self) -> str:
        return "license_code"

    #Возвращает ключ кода активации для полученного json по http запросу.
    def GetActivationCodeKey(self) -> str:
        return "activation_code"

    #Возвращает ключ типа продукта для полученного json по http запросу.
    def GetSoftwareTypeKey(self) -> str:
        return "software_type"

    #Возвращает ключ комментария для полученного json по http запросу.
    def GetNotesKey(self) -> str:
        return "notes"