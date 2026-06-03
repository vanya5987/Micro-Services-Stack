import os


class LockerConfig:
    GENERAL_LOCKER_FILE: str = "lasertag.lock"
    SPLASH_LOCKER_FILE: str = "lasertag_handler.lock"

    ABS_APP_PATH = r"C:\Users\name\Desktop\PROJECTS\PHYSICS\dist\ShootingGallery.exe"
    ABS_GIF_PATH = r"\pipeline_templates\splash_launcher\Алгкод.gif"

    RELATIVE_APP_PATH = os.path.join("{0}", "dist/ShootingGallery.exe")
    RELATIVE_GIF_PATH = os.path.join("{0}", "Алгкод.gif")
