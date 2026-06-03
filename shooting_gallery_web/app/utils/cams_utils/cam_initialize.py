from app.utils.cams_utils.cams_count_calculator import CamsCountCalculator
from app.presenters.json_presenter import JsonPresenter
from app.controllers.VideoCapture import VideoCapture
from shared.configs.core_configs.cam_config import CamConfig
from shared.pathings.path_config import PathConfig
from shared.configs.keys_configs.json_key_config import JsonKeyConfig

from typing import *


class CamInitialize:
    # Выбирает доступную и подходящую камеру.
    @staticmethod
    def select_available_camera() -> int:
        availableCameras: Dict[int, str] = CamsCountCalculator.get_available_cams()
        resultCamIndex: int = 0

        for i in range(len(availableCameras)):
            try:
                if CamInitialize._get_valid_cam(availableCameras[i].lower()):
                    resultCamIndex = i
                    break
            except:
                continue

        return resultCamIndex

    # Возвращает все доступные камеры.
    @staticmethod
    def get_all_available_cameras() -> Dict[int, str]:
        return CamsCountCalculator.get_available_cams()

    # Получает валидную камеру.
    @staticmethod
    def _get_valid_cam(camName: str) -> bool:
        currentCamName: Dict[str, str] = JsonPresenter.get_instance().read_json_file(PathConfig.CAM_SETTING_JSON_PATH)

        if currentCamName[JsonKeyConfig.STANDARD_CAMERA_NAME[0]].lower() in camName:
            return True
        return False

    # Запускаем видеопоток.
    @staticmethod
    def GetVideoCapture(selectedCameraIndex: int):
        data: Dict[str, Union[str, bool, int, List[int]]] = (
            JsonPresenter.get_instance().read_json_file(PathConfig.PROGRAM_SETTINGS_JSON_PATH))

        # if data[JsonKeyConfig.VIDEO_RESOLUTION[0]] == "low":
        #     videoCapture = VideoCapture(CamConfig.LOW_RESOLUTION_VALUES[0],
        #                                     CamConfig.LOW_RESOLUTION_VALUES[1], selectedCameraIndex)

        if data[JsonKeyConfig.VIDEO_RESOLUTION[0]] == "medium" or data[JsonKeyConfig.VIDEO_RESOLUTION[0]] == "low":
            videoCapture = VideoCapture(CamConfig.MIDDLE_RESOLUTION_VALUES[0],
                                            CamConfig.MIDDLE_RESOLUTION_VALUES[1], selectedCameraIndex)

        if data[JsonKeyConfig.VIDEO_RESOLUTION[0]] == "high":
            videoCapture = VideoCapture(CamConfig.UPP_RESOLUTION_VALUES[0],
                                            CamConfig.UPP_RESOLUTION_VALUES[1], selectedCameraIndex)


        return videoCapture
