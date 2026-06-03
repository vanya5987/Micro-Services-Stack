from app.presenters.json_presenter import JsonPresenter
from shared.pathings.path_config import PathConfig
from shared.configs.keys_configs.json_key_config import JsonKeyConfig
from app.utils.os_system_utils.get_system_type import SystemTypeGetter

from typing import *
import cv2


class CamPresenter:
    def __init__(self, camera_index=0, only_expose: bool = True):
        if SystemTypeGetter.system_is_windows():
            self.video_stream = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
        else:
            self.video_stream = cv2.VideoCapture(camera_index, cv2.CAP_V4L2)

        self.jsonLoader = JsonPresenter.get_instance()
        self.pathContainer = PathConfig()

        self.props = {
            JsonKeyConfig.CAMERA_BRIGHTNESS[0]: cv2.CAP_PROP_BRIGHTNESS,
            JsonKeyConfig.CAMERA_CONTRAST[0]: cv2.CAP_PROP_CONTRAST,
            JsonKeyConfig.CAMERA_SATURATION[0]: cv2.CAP_PROP_SATURATION,
            JsonKeyConfig.CAMERA_EXPOSURE[0]: cv2.CAP_PROP_EXPOSURE
        }

        self.video_stream.set(cv2.CAP_PROP_BUFFERSIZE, 2)
        # self.set_cam_params(only_expose=only_expose)

    def __set_property(self, name, value):
        prop = self.props[name]
        self.video_stream.set(prop, value)

    def set(self, name, value):
        self.__set_property(name, value)

    def set_brightness(self, value):
        self.__set_property(JsonKeyConfig.CAMERA_BRIGHTNESS[0], value)

    def set_contrast(self, value):
        self.__set_property(JsonKeyConfig.CAMERA_CONTRAST[0], value)

    def set_saturation(self, value):
        self.__set_property(JsonKeyConfig.CAMERA_SATURATION[0], value)

    def set_exposure(self, value):
        self.__set_property(JsonKeyConfig.CAMERA_EXPOSURE[0], value)

    def set_mjpeg(self):
        self.video_stream.set(
            cv2.CAP_PROP_FOURCC,
            cv2.VideoWriter_fourcc(*'MJPG')
        )

    def set_image_frame(self, resolutionWidth: int, resolutionHeight: int):
        self.video_stream.set(cv2.CAP_PROP_FRAME_WIDTH, resolutionWidth)
        self.video_stream.set(cv2.CAP_PROP_FRAME_HEIGHT, resolutionHeight)

    def set_cam_params(self, only_expose: bool):
        currentData: Dict[str, Union[str, bool, int, List[int]]] = self.jsonLoader.read_json_file(
            PathConfig.CAM_SETTING_JSON_PATH)

        self.set_exposure(currentData[JsonKeyConfig.CAMERA_EXPOSURE[0]])

        if not only_expose:
            self.set_contrast(currentData[JsonKeyConfig.CAMERA_CONTRAST[0]])
            self.set_saturation(currentData[JsonKeyConfig.CAMERA_SATURATION[0]])
            self.set_brightness(currentData[JsonKeyConfig.CAMERA_BRIGHTNESS[0]])

    def list_properties(self, only_supported=False):
        result = {}
        for name, prop in self.props.items():
            if prop is None:
                continue
            value = self.video_stream.get(prop)
            if only_supported and value in (0.0, -1.0):
                continue
            result[name] = value
        return result

    def print_properties(self, only_supported=False):
        props = self.list_properties(only_supported=only_supported)

        for name, value in props.items():
            print(f"{name}: {value}")
