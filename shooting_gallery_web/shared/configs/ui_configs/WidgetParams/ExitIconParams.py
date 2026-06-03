from dataclasses import dataclass

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget


@dataclass
class BaseWidgetParams:
    parent: QWidget

@dataclass
class ExitIconParams(BaseWidgetParams):
    iconPath: str
    iconSize: QSize
    text: str