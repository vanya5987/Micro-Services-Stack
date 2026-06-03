from typing import *

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication


class ModalButtonContainer:
    @classmethod
    def GetScaledSize(cls, maxSize: QSize, scaleW: float, scaleH: float) -> QSize:
        screen = QApplication.primaryScreen()
        if screen is None:
            return maxSize
        size = screen.size()
        width = min(maxSize.width(), int(size.width() * scaleW))
        height = min(maxSize.height(), int(size.height() * scaleH))
        return QSize(width, height)

    @classmethod
    def GetBaseButtonSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(320, 60), 0.17, 0.055)

    @classmethod
    def GetShootingButtonSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(220, 60), 0.17, 0.055)

    @classmethod
    def GetInputSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(363, 60), 0.189, 0.056)

    @classmethod
    def GetInputGroupSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(256, 60), 0.133, 0.056)

    @classmethod
    def GetInputKeySize(cls) -> QSize:
        return cls.GetScaledSize(QSize(363, 47), 0.189, 0.044)

    @classmethod
    def GetDescriptionSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(653, 146), 0.34, 0.135)