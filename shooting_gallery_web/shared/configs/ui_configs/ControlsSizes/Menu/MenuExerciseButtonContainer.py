from typing import Tuple

from PyQt5.QtWidgets import QApplication

from shared.configs.ui_configs.ControlsSizes.Menu.MenuButtonContainer import MenuButtonsContainer
from shared.configs.ui_configs.ControlsSizes.Menu.MenuFrameContainer import MenuFrameContainer


class ExerciseButtonsContainer:
    @classmethod
    def GetButtonSize(cls) -> Tuple[int, int]:
        screen = QApplication.primaryScreen()
        if screen is None:
            return 328, 65
        size = screen.size()
        width = min(328, int(0.22 * size.width()))
        height = min(65, int(0.035 * size.width()))
        return width, height

    @classmethod
    def GetButtonSpacing(cls) -> int:
        return 8

    @staticmethod
    def GetStartPosition() -> Tuple[int, int]:
        screenWidth, screenHeight = MenuFrameContainer.GetFullScreenSize()
        y_ratio = 409 / 900
        xButtons = MenuFrameContainer.GetFramePositionX()
        x = int(xButtons + MenuButtonsContainer().GetButtonSize()[0] + screenWidth * 0.02)
        y = int(screenHeight * y_ratio)
        return x, y