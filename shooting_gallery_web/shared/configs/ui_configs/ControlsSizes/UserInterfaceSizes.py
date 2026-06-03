from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication


class ContoursThickness:
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
    def GetCursorSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(32, 32), 0.16, 0.16)

    @classmethod
    def GetButtonBackSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(60, 60), 0.04, 0.07)

    @classmethod
    def GetButtonBackIconSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(15, 27), 0.014, 0.03)

    @classmethod
    def GetButtonSwitchSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(45, 45), 0.063, 0.063)

    @classmethod
    def GetButtonSwitchIconSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(11, 21), 0.01, 0.06)

    @classmethod
    def GetLogoSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(150, 100), 0.07, 0.08)

    @classmethod
    def GetButtonStopShootingSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(390, 60), 0.3, 0.06)

    @classmethod
    def GetCloseWindowButtonSize(cls) -> QSize:
        return cls.GetScaledSize(QSize(200, 60), 0.3, 0.06)

    @classmethod
    def GetTargetSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(206, 302), 0.1, 0.279)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetTargetTemplateSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(360, 310), 0.187, 0.287)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetPrintButtonIconSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(25, 25), 0.023, 0.033)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetSettingsButtonIconSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(35, 35), 0.0182, 0.0324)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetSettingsNumberLabelSize(cls, heightContainer) -> QSize:
        size = cls.GetScaledSize(QSize(55, 50), 0.035, 0.056)
        width = size.width()
        height = int(heightContainer * size.height() / 60)
        return QSize(width, height)

    @classmethod
    def GetShootingIconSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(70, 70), 0.0364, 0.0648)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetResultDateButtonSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(150, 50), 0.09, 0.05)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetBaseExitIconSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(30, 22), 0.016, 0.023)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetShootingExitIconSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(30, 22), 0.016, 0.023)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetExitIconRenderContainerSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(65, 50), 0.033, 0.046)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetNotificationIconSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(35, 35), 0.01822, 0.0324)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetCopyIconSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(25, 25), 0.013, 0.023)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetCopyButtonSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(45, 45), 0.023, 0.0416)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetAddGroupButton(cls) -> QSize:
        size = cls.GetScaledSize(QSize(35, 35), 0.0182, 0.0324)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetDropdownIconButton(cls) -> QSize:
        size = cls.GetScaledSize(QSize(30, 30), 0.0156, 0.0277)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetLicenseImgSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(155, 219), 0.0807, 0.203)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetLicenseIconSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(25, 25), 0.013, 0.0231)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetLanguageBoxSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(170, 50), 0.088, 0.0462)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetDropdownUpIconSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(20, 30), 0.0105, 0.028)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetHelpImgSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(458, 659), 0.238, 0.610)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetTitleImgSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(652, 324), 0.3395, 0.3)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetUpdateGifSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(100, 100), 0.05208, 0.0925)
        width = size.width()
        height = size.height()
        return QSize(width, height)

    @classmethod
    def GetDropdownSize(cls) -> QSize:
        size = cls.GetScaledSize(QSize(410, 55), 0.2135, 0.0509)
        width = size.width()
        height = size.height()
        return QSize(width, height)
