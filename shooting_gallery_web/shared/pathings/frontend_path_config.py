from fastapi import APIRouter
from fastapi.responses import JSONResponse
from shared.pathings.path_config import PathConfig
import os

router = APIRouter(
    prefix="/api/config",
    tags=["Config Paths"]
)

@router.get("/paths")
def get_static_paths():
    paths_data = {
        "FONT_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "Fonts"),
        "EXIT_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Exit.svg"),
        "UPDATE_ICON_PATH": os.path.join(PathConfig.SERVER_URL,"resources", "icons", "Update.gif"),
        "LICENCE_IMAGE_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "License_Img.png"),
        "LICENCE_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "License.svg"),
        "KEY_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Key.svg"),
        "SORT_UP_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Sort_Up.svg"),
        "SORT_DOWN_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Sort_Down.svg"),
        "LOGO_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Logo.svg"),
        "ADD_GROUP_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Add_Group.svg"),
        "SETTINGS_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Setting.svg"),
        "USER_ADD_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "User_Plus.svg"),
        "PRINTER_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Printer.svg"),
        "NOTIFICATION_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Notification.svg"),
        "WARNING_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Warning.svg"),
        "SOUND_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Sound.svg"),
        "BLANK_TEMPLATE_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Blank_Template.png"),
        "DOCUMENT_NUMBER_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "Manual", "Document_Number.png"),
        "DISABLE_SOUND_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Disable_Sound.svg"),
        "DROPDOWN_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Dropdown.svg"),
        "BULLETS_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Bullets.png"),
        "HOURGLASS_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Hourglass.png"),
        "PREVIOUS_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Previous_Button_Table.svg"),
        "NEXT_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Next_Button_Table.svg"),
        "SEARCH_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Search.svg"),
        "TITLE_ENG_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "Title", "Title_Eng.svg"),
        "POINTER_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Pointer.svg"),
        "ACCEPT_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Accept.svg"),
        "BACK_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Back.svg"),
        "DEFAULT_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Pointer.svg"),
        "BACKGROUND_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "Backgrounds", "Menu.gif"),
        "BACKGROUND_SETTINGS_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "Backgrounds", "Settings.png"),
        "BACKGROUND_HELP_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "Backgrounds", "User_Help.png"),
        "BACKGROUND_SHOOTING_SETTINGS_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "Backgrounds", "Shooting_Settings.png"),
        "BACKGROUND_LOADING_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "Backgrounds", "Loading_Screen.gif"),
        "CURSOR_NORMAL_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "Cursor", "Cursor_Normal.svg"),
        "CURSOR_CLICK_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "Cursor", "Cursor_Click.svg"),
        "TITLE_RU_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "Title", "Title_Ru.svg"),
        "COPY_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Copy.svg"),
        "QUESTION_ICON_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "icons", "Question.svg"),

        "SHOOTING_STATES_JSON_PATH": os.path.join(PathConfig.SERVER_URL, PathConfig.SHOOTING_STATES_JSON_PATH),
        "VERSION_JSON_PATH": os.path.join(PathConfig.SERVER_URL, PathConfig.VERSION_JSON_PATH),
        "CAM_SETTING_JSON_PATH": os.path.join(PathConfig.SERVER_URL, PathConfig.CAM_SETTING_JSON_PATH),
        "PROGRAM_SETTINGS_JSON_PATH": os.path.join(PathConfig.SERVER_URL, PathConfig.PROGRAM_SETTINGS_JSON_PATH),
        "DATA_BASE_PATH": os.path.join(PathConfig.SERVER_URL, PathConfig.DATA_BASE_PATH),
        "SHOOTING_SESSION_PATHS": os.path.join(PathConfig.SERVER_URL, PathConfig.SHOOTING_SESSION_PATHS),
        "LICENCE_JSON_PATH": os.path.join(PathConfig.SERVER_URL, PathConfig.LICENCE_JSON_PATH),
        "DEVELOPER_SETTINGS": os.path.join(PathConfig.SERVER_URL, PathConfig.DEVELOPER_SETTINGS),
        "BOOTSTRAP_JSON_PROGRAM_SETTINGS_PATH": os.path.join(PathConfig.SERVER_URL,
                                                             PathConfig.BOOTSTRAP_JSON_PROGRAM_SETTINGS_PATH),
        "BOOTSTRAP_JSON_DEVELOPER_SETTINGS_PATH": os.path.join(PathConfig.SERVER_URL,
                                                               PathConfig.BOOTSTRAP_JSON_DEVELOPER_SETTINGS_PATH),

        "TARGET_DIRECTORY_PATH": os.path.join(PathConfig.SERVER_URL, "resources", "Targets"),

        "VIDEO_STREAM_PAGE_PATH": f"{PathConfig.SERVER_URL}/video_page",
        "MENU_PAGE_PATH": f"{PathConfig.SERVER_URL}/menu",

        "VIDEO_STREAM_SCR_PATH": os.path.join(PathConfig.SERVER_URL, "video_stream_page.js"),
        "MENU_SCR_PATH": os.path.join(PathConfig.SERVER_URL, "menu_page.js"),
    }

    clean_paths = {key: val.replace("\\", "/") for key, val in paths_data.items()}
    return JSONResponse(content=clean_paths)

@router.get("/sounds")
def get_sound_paths():
    config_instance = PathConfig()

    shoot_sounds = {k: os.path.join(PathConfig.SERVER_URL, v) for k, v in config_instance.shoot_sounds_path.items()}
    program_sounds = {k: os.path.join(PathConfig.SERVER_URL, v) for k, v in config_instance.program_sounds_path.items()}
    ui_sounds = {k: os.path.join(PathConfig.SERVER_URL, v) for k, v in config_instance.ui_sounds_path.items()}
    game_target_sounds = {k: os.path.join(PathConfig.SERVER_URL, v) for k, v in
                          config_instance.get_game_target_sounds_paths().items()}

    sounds_data = {
        "shoot_sounds": shoot_sounds,
        "program_sounds": program_sounds,
        "ui_sounds": ui_sounds,
        "game_target_sounds": game_target_sounds
    }

    clean_sounds = {
        category: {k: v.replace("\\", "/") for k, v in items.items()}
        for category, items in sounds_data.items()
    }
    return JSONResponse(content=clean_sounds)