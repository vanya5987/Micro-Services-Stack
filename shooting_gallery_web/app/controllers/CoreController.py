from shared.configs.core_configs.screen_config import ScreenConfig
from shared.pathings.path_config import PathConfig

from app.presenters.json_presenter import JsonPresenter
from app.schemas.json_schemas.json_states_schema import JsonStatesSchema
from app.schemas.json_schemas.json_session_schema import JsonSessionSchema
from shared.configs.keys_configs.json_key_config import JsonKeyConfig

from app.controllers.PlayerHandler import PlayerHandler
from app.services.contour_services.contour_handler import ContourHandler
from app.services.coins_services.coins_adder import CoinsAdder
from app.utils.target_utils.virtual_target_calculators.ValidParentTargetValues import ValidParentTargetValues

from app.controllers.ScreenImageController import ScreenImageController

from typing import *


class CoreController:
    def __init__(self, resolution: Tuple[int, int], scale_coef: float):
        self.json_controller = JsonPresenter.get_instance()

        self.json_controller.update_any_settings_value_key(JsonKeyConfig.IS_CALIBRATION_MODE[0], True)

        self.settingsData: Dict[str, Union[str, bool, int, List[int]]] = self.json_controller.read_json_file(
            PathConfig.PROGRAM_SETTINGS_JSON_PATH)

        self.resolution: Tuple[int, int] = resolution
        self.scale_coef: float = scale_coef

        self.targetSize: Tuple[int, int] = (self.settingsData[JsonKeyConfig.TARGET_SIZE[0]][0],
                                            self.settingsData[JsonKeyConfig.TARGET_SIZE[0]][1])
        self.targetScaler: int = self.settingsData[JsonKeyConfig.TARGET_SCALER[0]]
        self.laserThreshold: List[int] = self.settingsData[JsonKeyConfig.LASER_BRIGHTEST[0]]

        self.laserPulseDuration: int = self.settingsData[JsonKeyConfig.LASER_PULSE_DURATION[0]]

        self.playersCount: int = self.settingsData[JsonKeyConfig.PLAYER_COUNT[0]]
        self.bulletsCount: int = self.settingsData[JsonKeyConfig.BULLET_COUNT[0]]
        self.shootTimeThreshold: str = self.settingsData[JsonKeyConfig.SHOOT_TIME_THRESHOLD[0]]

        self.json_controller.upload_data(PathConfig.SHOOTING_STATES_JSON_PATH,
                                         JsonStatesSchema.create_target_states())

        for jsonIndex in range(1, 6):
            self.json_controller.upload_data(PathConfig.SHOOTING_SESSION_PATHS.format(jsonIndex),
                                             JsonSessionSchema.create_session_data())

    def InitializeCore(self):
        screenContainer = ScreenConfig(self.resolution, self.targetSize, self.targetScaler)

        validTargetValues = ValidParentTargetValues()
        target = validTargetValues.CalculateValidTargetValues(
            self.settingsData[JsonKeyConfig.TARGET_FILE_NAME[0]].rsplit('.png', 1)[0])

        contourHandler = ContourHandler(screenContainer)
        coinsAdder = CoinsAdder(target[0][0])
        playerHandler = PlayerHandler(coinsAdder, self.laserPulseDuration, self.playersCount, self.bulletsCount,
                                      self.settingsData[JsonKeyConfig.EXERCISE_TYPE_INDEX[0]], self.shootTimeThreshold)
        screenImageController = ScreenImageController(contourHandler, target,
                                                                             playerHandler,
                                                                             self.settingsData[
                                                                                 JsonKeyConfig.QR_CONTOUR_LENGTH[0]],
                                                                             self.playersCount)

        return screenImageController, playerHandler
