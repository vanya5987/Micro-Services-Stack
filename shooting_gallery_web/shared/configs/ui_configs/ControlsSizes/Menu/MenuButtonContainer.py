#Библиотеки.
from typing import *

from PyQt5.QtWidgets import QApplication


#Библиотеки.

class MenuButtonsContainer: #Контейнер для кнопок "МЕНЮ".
    @classmethod
    def GetButtonSize(cls) -> Tuple[int, int]:
        screen = QApplication.primaryScreen()
        if screen is None:
            return 380, 87
        size = screen.size()
        width = min(380, int(0.25 * size.width()))
        height = min(87, int(0.05 * size.width()))
        return width, height

    @classmethod
    def GetButtonSpacing(cls) -> int:
        return 3