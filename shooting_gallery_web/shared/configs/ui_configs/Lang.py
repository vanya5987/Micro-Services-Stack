from PyQt5.QtCore import QObject, pyqtSignal

from shared.pathings.path_config import PathConfig
from shared.configs.ui_configs.TextContainer import TextContainer
from shared.configs.ui_configs.TextContainer_KZ import TextContainer_KZ
from app.presenters.json_presenter import JsonPresenter
from shared.configs.keys_configs.json_key_config import JsonKeyConfig
from shared.configs.keys_configs.exceptional_keys import ExceptionalKeys


class LanguageSignal(QObject):
    languageChanged = pyqtSignal()

    def __init__(self):
        try:
            super().__init__()
            self.json_controller = JsonPresenter.get_instance()

            self.language = self.json_controller.read_json_file(PathConfig.PROGRAM_SETTINGS_JSON_PATH)
            self._currentText = TextContainer()
        except Exception as e:
            import traceback
            print("Ошибка:", e)
            traceback.print_exc()

    def InitLanguageFromJson(self):
        lang = self.language.get(JsonKeyConfig.LANGUAGE[0], ExceptionalKeys.RU_KEY)

        if lang == ExceptionalKeys.RU_KEY:
            self._currentText = TextContainer()
        elif lang == ExceptionalKeys.KZ_KEY:
            self._currentText = TextContainer_KZ()
        else:
            self._currentText = TextContainer()

        self.languageChanged.emit()

    def SetLanguage(self, lang: str):
        try:
            if lang == "русский":
                self._currentText = TextContainer()
                self.language[JsonKeyConfig.LANGUAGE[0]] = ExceptionalKeys.RU_KEY
                self.json_controller.update_any_settings_value_key(JsonKeyConfig.LANGUAGE[0], ExceptionalKeys.RU_KEY)
            elif lang == "қазақ":
                self._currentText = TextContainer_KZ()
                self.language[JsonKeyConfig.LANGUAGE[0]] = ExceptionalKeys.KZ_KEY
                self.json_controller.update_any_settings_value_key(JsonKeyConfig.LANGUAGE[0], ExceptionalKeys.KZ_KEY)
            else:
                return

            self.languageChanged.emit()
        except Exception as e:
            import traceback
            print("Ошибка:", e)
            traceback.print_exc()

    def GetTextContainer(self):
        return self._currentText

    def GetLanguage(self) -> str:
        return self.language.get(JsonKeyConfig.LANGUAGE[0], ExceptionalKeys.RU_KEY)


LangSignal = LanguageSignal()
