import sys
import os

from shared.pathings.python_config import PythonConfig

PythonConfig.set_python_paths()

from shared.configs.ui_configs.Lang import LangSignal
from shared.configs.ui_configs.WidgetParams.LicenseWindowParams import LicenseWindowParams
from frontend.modal_window.LicenseWindow import LicenseWindow
from frontend.Utils.CheckLicense import CheckLicense

sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication, QDialog
from frontend.Pages.LoadingScreen import LoadingScreen
from frontend.cursor.cursor_manager import CursorManager
from frontend.Utils.FontLoader import Fonts

from app.utils.validators.check_programm_running import CheckProgramRunning
from app.schemas.json_schemas.json_schema_validator import JsonSchemaValidator
from tests.test_tarceback import TestTraceback
from tools.pipeline_templates.splash_launcher.locker_config import LockerConfig

from app.utils.time_utils.datetime_utils import DatetimeUtils
from app.utils.licence_utils.encryptor import Encryptor
from app.api.database_api.DataStorageGetter import DataStorageGetter
from app.api.database_api.EncryptedDataRepository import EncryptedDataRepository
from app.utils.time_utils.date_checker import DateChecker
from app.services.os_system_services.system_analyzer import SystemAnalyzer


def _clean_old_logs():
    from app.utils.os_system_utils.logs_cleaner import LogsCleaner
    LogsCleaner.clean_old_log()

class Main:
    def __init__(self):
        system_analyzer = SystemAnalyzer()
        system_analyzer.load_base_system_info()
        system_analyzer.create_base_system_info_log()
        system_analyzer.compare_base_system_settings()

        _clean_old_logs()
        TestTraceback.setup_global_exception_handling()
        JsonSchemaValidator().check_valid_schemas()

        if not CheckProgramRunning.app_is_running(LockerConfig.GENERAL_LOCKER_FILE):
            app = QApplication(sys.argv)
            encrypted_data_connection = EncryptedDataRepository(DataStorageGetter())

            LangSignal.InitLanguageFromJson()

            self.cursorManager = CursorManager()
            fonts = Fonts()
            fonts.RegistrateFonts()

            use_passkey: bool = True  # Если True, то лицензия будет использована.
            use_offline_licence: bool = False #Добавляем ли offline активацию? Да если True.

            if use_offline_licence:
                pass_is_invalid_date: bool = False
            else:
                key_is_valid: bool = False

                try:
                    pass_key: str = Encryptor.decrypt(encrypted_data_connection.get_encrypted_pass_key())
                    key_is_valid = DateChecker.is_valid_date(pass_key)
                except:
                    pass

                if key_is_valid:
                    pass_is_invalid_date: bool = DatetimeUtils.get_current_date() > pass_key #Текущее время больше записанного.
                else:
                    pass_is_invalid_date: bool = True

            if use_passkey:
                checkLicense = CheckLicense()

                if pass_is_invalid_date or not checkLicense.CheckKey():
                    dialog = LicenseWindow(LicenseWindowParams(checkLicense=checkLicense))
                    result = dialog.exec()

                    if result != QDialog.Accepted:
                        sys.exit(0)

            self.loadingScreen = LoadingScreen()
            self.loadingScreen.show()
            sys.exit(app.exec_())

Main()
