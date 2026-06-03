from dataclasses import dataclass, field
from typing import *

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget, QPushButton

from frontend.Utils.font_scaler_window import FontScalerWindow
from frontend.Video.VideoCaptureWorker import VideoCaptureWorker

@dataclass
class BaseWidgetParams:
    parent: QWidget

@dataclass
class ButtonWidgetParams(BaseWidgetParams):
    config: Dict[str, str]
    targetButton: Optional[QPushButton] = field(default=None)
    geometry: Optional[QRect] = field(default=None)
    fontScaler: Optional["FontScalerWindow"] = field(default=None)

@dataclass
class RegistrationWindowParams(BaseWidgetParams):
    on_accept: Callable[[], None]

@dataclass
class GroupRegistrationWindowParams(BaseWidgetParams):
    on_accept: Callable[[], None]

@dataclass
class LabeledSliderParams(BaseWidgetParams):
    text: str
    key: str
    hintText: str
    minValue: int = 0
    maxValue: int = 0
    dual: bool = False
    isSwitch: bool = False
    default: Union[int, Tuple[int, int], bool, None] = None

@dataclass
class ExercisesWindowParams(BaseWidgetParams):
    exerciseList: List[Tuple[int, str, int, int, int, str, int, str]]
    videoWorker: VideoCaptureWorker
    exerciseType: int

@dataclass
class ShootingSettingsWindowParams(BaseWidgetParams):
    videoWorker: VideoCaptureWorker
    numShooters: int
    numShots: int
    exerciseTime: str
    titleExerciseName: str
    targetPath: str
    exerciseID: int
    exerciseType: int

@dataclass
class ExercisesSingleSliderParams(BaseWidgetParams):
    text: str
    minValue: int
    maxValue: int
    default: int = None

@dataclass
class ResultWindowParams(BaseWidgetParams):
    exerciseList: List[Tuple[int, str, int, int, int, str, int, str]]

@dataclass
class ShootingWindowParams(BaseWidgetParams):
    shooters: List[Tuple[int, str]]
    targetPath: str
    titleExerciseName: str
    exerciseID: int
    exerciseType: int
