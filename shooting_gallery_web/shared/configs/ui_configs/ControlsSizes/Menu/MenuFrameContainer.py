#Контейнеры.
from shared.configs.ui_configs.ControlsSizes.Menu.MenuButtonContainer import MenuButtonsContainer
#Контейнеры.
#Библиотеки.
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication
from typing import *
#Библиотеки.

class MenuFrameContainer: #Контейнер для Canvas "МЕНЮ".
    @classmethod
    def GetFullScreenSize(cls) -> Tuple[int, int]:
        screen = QApplication.primaryScreen()
        size: QSize = screen.size()
        return size.width(), size.height()

    @classmethod
    def GetFramePositionX(cls) -> int:
        full_width = cls.GetFullScreenSize()[0]
        frame_width = MenuButtonsContainer().GetButtonSize()[0]
        return full_width // 2 - frame_width // 2

    @classmethod
    def GetFramePositionY(cls) -> int:
        full_height = cls.GetFullScreenSize()[1]
        return int(full_height * 0.4422)

    @classmethod
    def GetTitlePositionY(cls) -> int:
        full_height = cls.GetFullScreenSize()[1]
        return int(full_height * 0.08)
