from PyQt5.QtWidgets import QApplication
from typing import  *

class WindowFrameContainer:
    @classmethod
    def GetFullScreenSize(cls) -> Tuple[int, int]:
        screen = QApplication.primaryScreen()
        size = screen.size()
        return size.width(), size.height()

    @classmethod
    def GetTopBlockPositionY(cls) -> int:
        y = int(0.072 * cls.GetFullScreenSize()[1])
        return y

    @classmethod
    def GetTitlePosition(cls, widgetWidth: int) -> Tuple[int, int]:
        screenWidth, _ = cls.GetFullScreenSize()
        x = screenWidth // 2 - widgetWidth // 2
        y = cls.GetTopBlockPositionY()
        return x, y

    @classmethod
    def GetBackButtonPosition(cls, y: int) -> Tuple[int, int]:
        x = int(0.032 * cls.GetFullScreenSize()[1])
        return x, y

    @classmethod
    def GetSlidersBlockWidth(cls) -> int:
        screenWidth, _ = cls.GetFullScreenSize()
        return int(screenWidth * 0.33)

    @classmethod
    def GetBoxSlidersSize(cls) -> Tuple[int, int]:
        screenWidth = cls.GetFullScreenSize()[0]
        width = min(65, int(0.045 * screenWidth))
        height = min(55, int(0.035 * screenWidth))
        return width, height

    @classmethod
    def GetSlidersSize(cls) -> int:
        screenWidth = cls.GetFullScreenSize()[0]
        sliderHeight = max(38, min(50, int(0.027 * screenWidth)))
        return sliderHeight

    @classmethod
    def GetVideoBlockSize(cls) -> Tuple[int, int]:
        screenWidth, _ = cls.GetFullScreenSize()
        width = int(screenWidth * 0.5)
        height = int(width * 535 / 950)
        return width, height

    @classmethod
    def GetCombinedBlockSize(cls) -> Tuple[int, int]:
        spacing = int(cls.GetFullScreenSize()[0] * 0.04)
        width = cls.GetSlidersBlockWidth() + spacing + cls.GetVideoBlockSize()[0]
        height = int(cls.GetFullScreenSize()[1] * 0.69)
        return width, height

    @classmethod
    def GetVideoDropdownSize(cls) -> Tuple[int, int]:
        widthVideo, _ = cls.GetVideoBlockSize()
        width = widthVideo
        height = 60
        return width, height

    @classmethod
    def GetLeftBlockHelpPosition(cls) -> Tuple[int, int]:
        x = int(0.052 * cls.GetFullScreenSize()[1])
        y = int(0.3 * cls.GetFullScreenSize()[1])
        return x, y

    @classmethod
    def GetButtonHelpSize(cls) -> Tuple[int, int]:
        width = min(400, int(0.25 * cls.GetFullScreenSize()[0]))
        height = min(80, int(0.045 * cls.GetFullScreenSize()[0]))
        return width, height

    @classmethod
    def GetLeftBlockExercisesPosition(cls) -> Tuple[int, int]:
        x = int(0.052 * cls.GetFullScreenSize()[1])
        y = int(0.3 * cls.GetFullScreenSize()[1])
        return x, y

    @classmethod
    def GetMarginsExercise(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.02)
        top = int(screenH * 0.04)
        right = int(screenW * 0.04)
        bottom = int(screenH * 0.07)
        return left, top, right, bottom

    @classmethod
    def GetMarginsExerciseLeftBlock(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.007)
        top = int(screenH * 0.09)
        right = int(screenW * 0.007)
        bottom = int(screenH * 0.014)
        return left, top, right, bottom

    @classmethod
    def GetMarginsExerciseRightBlock(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.0104)
        top = int(screenH * 0.019)
        right = int(screenW * 0.0104)
        bottom = int(screenH * 0.019)
        return left, top, right, bottom

    @classmethod
    def GetSizeExercise(cls) -> Tuple[int, int]:
        width = min(460, int(cls.GetFullScreenSize()[0] * 0.29)) #460
        height = int(cls.GetFullScreenSize()[1] * 0.6)
        return width, height

    @classmethod
    def GetMarginsExerciseScroll(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.0046)
        top = int(screenH * 0.009)
        right = int(screenW * 0.0046)
        bottom = int(screenH * 0.009)
        return left, top, right, bottom

    @classmethod
    def GetSizeExerciseButton(cls) -> Tuple[int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        width = min(410, int(screenW * 0.26)) #410
        height = int(screenW * 0.03) #57
        return width, height

    @classmethod
    def GetSizeExerciseButtonResult(cls) -> Tuple[int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        width = min(366, max(270, int(screenW * 0.26)))  # 366
        height = int(screenW * 0.04)  # 75
        return width, height

    @classmethod
    def GetSizeExerciseTargetName(cls) -> Tuple[int, int]:
        width = max(400, int(cls.GetFullScreenSize()[1] * 0.8))
        height = 60
        return width, height

    @classmethod
    def GetSizeExerciseSlider(cls) -> Tuple[int, int]:
        width =int(cls.GetFullScreenSize()[1] * 0.8)
        height = 50
        return width, height

    @classmethod
    def GetWidthExerciseRideBlock(cls) -> int:
        width = int(cls.GetFullScreenSize()[0] * 0.5)
        return width

    @classmethod
    def GetSizeProccesShootingFrame(cls) -> Tuple[int, int]:
        width = int(cls.GetFullScreenSize()[0] * 0.5)
        height = int(cls.GetFullScreenSize()[1] * 0.305)
        return width, height

    @classmethod
    def GetMarginProccesShootingFrame(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.0104)
        top = int(screenH * 0.019)
        right = int(screenW * 0.0104)
        bottom = int(screenH * 0.019)
        return left, top, right, bottom

    @classmethod
    def GetMarginShootingTable(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.026)
        top = int(screenH * 0.018) #0.138
        right = int(screenW * 0.026)
        bottom = int(screenH * 0.046)
        return left, top, right, bottom

    @classmethod
    def GetMarginShootingScrollBlock(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.01) #16
        top = int(screenH * 0.01) #10
        right = int(screenW * 0.01) #16
        bottom = int(screenH * 0.01) #10
        return left, top, right, bottom

    @classmethod
    def GetSizeShootingTableLabel(cls) -> Tuple[int, int]:
        width = int(cls.GetFullScreenSize()[0] * 0.075) #140
        height = int(cls.GetFullScreenSize()[1] * 0.06) #60
        return width, height

    @classmethod
    def GetSizeShootingTableScrollBlock(cls) -> Tuple[int, int]:
        width = int(cls.GetFullScreenSize()[0] * 0.28) #500
        height = int(cls.GetFullScreenSize()[1] * 0.27) #300
        return width, height

    @classmethod
    def GetSizeResultButton(cls) -> Tuple[int, int]:
        width = min(430, int(cls.GetFullScreenSize()[0] * 0.265)) #430
        height = min(40, int(cls.GetFullScreenSize()[1] * 0.037)) #40
        return width, height

    @classmethod
    def GetSizeResultTable(cls) -> Tuple[int, int]:
        width = int(cls.GetFullScreenSize()[0] * 0.5)
        height = int(cls.GetFullScreenSize()[1] * 0.28)
        return width, height

    @classmethod
    def GetSizeSwitchBlock(cls) -> Tuple[int, int]:
        width = int(cls.GetFullScreenSize()[0] * 0.27)  # 390
        height = int(cls.GetFullScreenSize()[1] * 0.0509)  # 55
        return width, height

    @classmethod
    def GetSizeSwitch(cls) -> Tuple[int, int]:
        width = int(cls.GetFullScreenSize()[0] * 0.028)  # 55
        height = int(cls.GetFullScreenSize()[1] * 0.026)  # 28
        return width, height

    @classmethod
    def GetSizeRightBlockHelp(cls) -> Tuple[int, int]:
        width = int(cls.GetFullScreenSize()[0] * 0.3802) #730
        height = int(cls.GetFullScreenSize()[1] * 0.731) #790
        return width, height

    @classmethod
    def GetMarginShootingVideoBlock(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.0104)
        top = int(screenH * 0.0185)
        right = int(screenW * 0.0104)
        bottom = int(screenH * 0.0185)
        return left, top, right, bottom

    @classmethod
    def GetMarginShootingVideoLabels(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.104)
        top = 0
        right = int(screenW * 0.104)
        bottom = 0
        return left, top, right, bottom

    @classmethod
    def GetMarginShootingLeftBlock(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.008)
        top = int(screenH * 0.139)
        right = int(screenW * 0.008)
        bottom = int(screenH * 0.0139)
        return left, top, right, bottom

    @classmethod
    def GetMarginLabelWithIcon(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.0104)
        top = min(10, int(screenH * 0.0093))
        right = int(screenW * 0.0104)
        bottom = min(10, int(screenH * 0.0093))
        return left, top, right, bottom

    @classmethod
    def GetMarginResultCategory(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.0052)
        top = min(10, int(screenH * 0.0093))
        right = int(screenW * 0.0052)
        bottom = min(10, int(screenH * 0.0093))
        return left, top, right, bottom

    @classmethod
    def GetMarginResultRightBlock(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.0104)
        top = int(screenH * 0.0185)
        right = int(screenW * 0.0104)
        bottom = 0
        return left, top, right, bottom

    @classmethod
    def GetMarginRegistration(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.0208)
        top = int(screenH * 0.0277)
        right = int(screenW * 0.026)
        bottom = int(screenH * 0.037)
        return left, top, right, bottom

    @classmethod
    def GetMarginLicenseTop(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.0104)
        top = int(screenH * 0.0185)
        right = int(screenW * 0.0104)
        bottom = int(screenH * 0.0185)
        return left, top, right, bottom

    @classmethod
    def GetMarginLicenseBottom(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.0052)
        top = int(screenH * 0.0092)
        right = int(screenW * 0.0052)
        bottom = int(screenH * 0.0185)
        return left, top, right, bottom

    @classmethod
    def GetMarginSwitchLayout(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.0093)  # 18
        top = int(screenH * 0.0092)  # 10
        right = int(screenW * 0.0078)  # 15
        bottom = int(screenH * 0.0092)  # 10
        return left, top, right, bottom

    @classmethod
    def GetMarginInstruction(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.00025)
        top = int(screenH * 0.001)
        right = int(screenW * 0.00025)
        bottom = int(screenH * 0.001)
        return left, top, right, bottom

    @classmethod
    def GetMarginHelpWindow(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.05208) # 100
        top = int(screenH * 0.0925) # 100
        right = int(screenW * 0.05208) # 100
        bottom = int(screenH * 0.00925) # 10
        return left, top, right, bottom

    @classmethod
    def GetMarginBlockHelpWindow(cls) -> Tuple[int, int, int, int]:
        screenW, screenH = cls.GetFullScreenSize()
        left = int(screenW * 0.00781)  # 15
        top = int(screenH * 0.0138)  # 15
        right = int(screenW * 0.00781)  # 15
        bottom = int(screenH * 0.0138)  # 15
        return left, top, right, bottom