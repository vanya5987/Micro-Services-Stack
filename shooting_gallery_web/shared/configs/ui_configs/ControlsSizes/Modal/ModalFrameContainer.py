from typing import *

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication


class ModalFrameContainer:
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
    def GetFullScreenSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(780, 370), 0.406, 0.342)

    @classmethod
    def GetMessageSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(755, 170), 0.393, 0.157)

    @classmethod
    def GetFullScreenRegistrationSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(810, 490), 0.421, 0.453)

    @classmethod
    def GetFullScreenGroupRegistrationSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(810, 420), 0.421, 0.388)

    @classmethod
    def GetFullScreenLicenseSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(780, 670), 0.406, 0.62)

    @classmethod
    def GetInstructionDialogSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(544, 700), 0.283, 0.6481)