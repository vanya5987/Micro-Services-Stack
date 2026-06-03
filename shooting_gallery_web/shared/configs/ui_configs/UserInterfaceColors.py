# Библиотеки.
from typing import *


# Библиотеки.

class ParentButtonColors:  # Контейнер цветов всех кнопок кроме кнопки стрельбы.
    TITLE: str = "#FFFFFF"
    TITLE_DOWN: str = "#CEF4E7"
    TITLE_BORDER: str = "#26635D"
    VERSION_TEXT: str = "#FFFFFF"

    TITLE_LOADING: str = "#FFFFFF"

    BUTTON_NORMAL: str = "rgba(23, 79, 73, 0.75)"
    BUTTON_HOVER: str = "rgba(23, 79, 73, 0.95)"
    BUTTON_TEXT: str = "#FFFFFF"
    BUTTON_BORDER: str = "#4FE1D2"
    BUTTON_WARNING_BORDER: str = "#FF5454"
    BUTTON_DISABLE: str = "#808080"
    BUTTON_SHADOW: str = "#034039"  # TEST.
    BUTTONS_MENU_FONT: List[str] = ["#42C0B3", "#4FE1D2", "#4FE1D2", "#4FE1D2"]

    MODAL_BACKGROUND: str = "rgba(23, 79, 73, 0.95)"
    MODAL_MESSAGE: str = "#01A490"
    MODAL_BUTTON: str = "#174F49"
    MODAL_TEXT: str = "#FFFFFF"
    MODAL_BUTTON_HOVER: str = "#103631"
    MODAL_ICON_BORDER: str = "#FFFFFF"

    SETTINGS_TITLE: str = "#FFFFFF"
    SETTINGS_BUTTON_BACK: str = "rgba(254, 254, 254, 0.5)"
    SETTINGS_BUTTON_BACK_BORDER: str = "#174F49"
    SETTINGS_BUTTON_BACK_HOVER: str = "rgba(23, 79, 73, 0.4)"
    SETTINGS_SLIDER_TEXT: str = "#174F49"
    SETTINGS_SLIDER_LABEL: str = "rgba(254, 254, 254, 0.5)"
    SETTINGS_SLIDER: str = "#174F49"
    SETTINGS_SLIDER_HANDLE: str = "#174F49"
    SETTINGS_SLIDER_HANDLE_ACTIVE: str = "#4FE1D2"
    SETTINGS_DROPDOWN_BACKGROUND: str = "#174F49"
    SETTINGS_DROPDOWN_BACKGROUND_OPEN: str = "#47726D"
    SETTINGS_DROPDOWN_TEXT: str = "#FFFFFF"
    SETTINGS_DROPDOWN_LABEL: str = "#174F49"
    SETTINGS_DROPDOWN_LABEL_BACKGROUND: str = "rgba(254, 254, 254, 0.3)"
    SETTINGS_DROPDOWN_SELECTED: str = "#BFCECC"
    SETTINGS_DROPDOWN_SELECTED_TEXT: str = "#174F49"
    SETTINGS_VIDEO_BACKGROUND: str = "#1B5650"
    SETTINGS_SWITCH_CONTAINER: str = "#9EC1BC"
    SETTINGS_SWITCH_BORDER: str = "#174F49"
    SETTINGS_SWITCH_LABEL: str = "#FFFFFF"
    SETTINGS_SWITCH_CHECKED: str = "#00B4A2"
    SETTINGS_SWITCH_DEFAULT: str = "#D2D5DA"

    HELP_TITLE: str = "#FFFFFF"
    HELP_TEXT: str = "#FFFFFF"
    HELP_BUTTON_TEXT: str = "#174F49"

    EXERCISES_BACKGROUND: str = "rgba(23, 79, 73, 0.75)"
    EXERCISES_COLOR_TEXT: str = "#FFFFFF"
    EXERCISES_BACKGROUND_BUTTON: str = "#01A490"
    EXERCISES_BACKGROUND_BUTTON_SHOOTING: str = "rgba(254, 254, 254, 0.5)"
    EXERCISES_BACKGROUND_BUTTON_SHOOTING_TEXT: str = "#174F49"
    EXERCISES_BACKGROUND_TARGET_TEXT: str = "rgba(23, 79, 73, 0.75)"
    EXERCISES_TARGET_TEXT: str = "#FFFFFF"

    SHO0TING_SETTING_INPUT_BACKGROUND: str = "rgba(23, 79, 73, 0.75)"
    SHO0TING_SETTING_INPUT_VALUE_BACKGROUND: str = "rgba(134, 169, 170, 0.4)"
    SHO0TING_SETTING_INPUT: str = "#FFFFFF"
    SHO0TING_SETTING_INPUT_VALUE: str = "#FF5454"
    SHO0TING_SETTING_LABEL: str = "#5CE6D5"
    SHO0TING_SETTING_LABEL_BACKGROUND: str = "rgba(35, 107, 99, 0.9)"

    SHOOTING_SHOOTER: str = "#FFFFFF"
    SHOOTING_NAME_SHOOTER: str = "#4FE1D2"
    SHOOTING_BUTTON_BACKGROUND: str = "rgba(254, 254, 254, 0.5)"
    SHOOTING_BUTTON_TEXT: str = "#174F49"
    SHOOTING_BUTTON_SWITCH: str = "rgba(134, 169, 170, 0.4)"

    SHOOTING_START_TABLE_FRAME_BACKGROUND: str = "rgba(23, 79, 73, 0.75)"
    SHOOTING_START_TABLE_BACKGROUND: str = "rgba(1, 164, 144, 0.37)"

    RESULT_LABEL: str = "#FFFFFF"
    RESULT_TABLE_BUTTON_BACKGROUND: str = "#174F49"
    RESULT_TABLE_BUTTON: str = "#FFFFFF"
    RESULT_TABLE_BUTTON_HOVER: str = "#174F49"
    RESULT_TABLE_BUTTON_BACKGROUND_HOVER: str = "rgba(255, 255, 255, 0.65)"
    RESULT_TABLE: str = "rgba(23, 79, 73, 0.75)"
    RESULT_CHECKED: str = "rgba(255, 255, 255, 0.65)"
    RESULT_CHECKED_COLOR: str = "#174F49"
    RESULT_BACKGROUND_DISABLED: str = "rgba(1, 164, 144, 0.15)"
    RESULT_COLOR_DISABLED: str = "rgba(255, 255, 255, 0.24)"

    TARGET_BACKGROUND_BACKGROUND = "rgba(23, 79, 73, 230)"


class ComboBoxColors:  # Контейнер цветов комбобокса.
    BUTTON_NORMAL: str = "#174F49"
    BUTTON_HOVER: str = "#517B77"
    BUTTON_TEXT: str = "#FFFFFF"
    BUTTON_BORDER: str = "#4FE1D2"


class TableColors:
    LABEL: str = "rgba(254, 254, 254, 0.7)"
    TEXT: str = "#FFFFFF"
    TITLE: str = "#FFFFFF"


class ResultColors:
    GREAT_RESULT: str = "#00FF6A"
    NORMAL_RESULT: str = "#F9F7AD"
    BAD_RESULT: str = "#FF5454"


class ShootingButtonColors:  # Контейнер цветов кнопки "Стрельба".
    SHOOTING_BUTTON_NORMAL: str = "#D9EAE8"
    SHOOTING_BUTTON_HOVER: str = "#81BDB6"
    SHOOTING_BUTTON_TEXT: str = "#1A514E"


class RangeSliderColors:  # Контейнер цветов слайдера.
    SLIDER: str = "#174F49"
    SLIDER_TEXT: str = "#FFFFFF"


class ContoursColors:
    VALID_TARGET_CONTOUR_COLOR: Tuple[int, int, int] = (200, 213, 48)  # Бирюзовый.
    INVALID_TARGET_CONTOUR_COLOR: Tuple[int, int, int] = (60, 20, 220)  # Красный.
    TEST_COLOR: Tuple[int, int, int] = (0, 255, 0)  # Зеленый.
    QR_COLOR: Tuple[int, int, int] = (255, 144, 30)  # Синий.
    CALIBRATION_TEXT_COLOR: Tuple[int, int, int] = (200, 213, 48)
    ERROR_TEXT_COLOR: Tuple[int, int, int] = (255, 255, 255)
    PLAYER_INFO: Tuple[int, int, int] = (255, 255, 255)
    TEXT_BACKGROUND_COLOR: Tuple[int, int, int] = (100, 20, 20)
