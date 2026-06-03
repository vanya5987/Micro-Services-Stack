from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QLabel
from shared.configs.keys_configs.json_key_config import JsonKeyConfig
from shared.configs.ui_configs.TextContainer import TextContainer
from shared.configs.ui_configs.TextContainer_KZ import TextContainer_KZ
from shared.configs.keys_configs.exceptional_keys import ExceptionalKeys
from app.presenters.json_presenter import JsonPresenter
from shared.pathings.path_config import PathConfig

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QMovie
from typing import List, Dict

import subprocess
import fcntl
import sys
import os

#pkexec - UI аналог sudo, есть во всех не серверных системах.

from shared.pathings.python_config import PythonConfig
PythonConfig.set_python_paths()

BASE_DIR: str = os.path.dirname(sys.executable)
MAIN_APP_BIN: str = os.path.join(BASE_DIR, "dist", "ShootingGallery")
GIF_PATH: str = os.path.join(BASE_DIR, "Алгкод.gif")
JSON_SETTINGS_PATH: str = os.path.join(BASE_DIR, PathConfig.BOOTSTRAP_JSON_PROGRAM_SETTINGS_PATH)
JSON_SETTING = JsonPresenter.get_instance().read_json_file(JSON_SETTINGS_PATH)

if JSON_SETTING[JsonKeyConfig.LANGUAGE[0]] == ExceptionalKeys.RU_KEY:
    EXIT_MESSAGES = TextContainer.EXIT_MESSAGES
    PERMISSION_MESSAGES = TextContainer.PERMISSION_MESSAGES
    LIB_QUESTION_MESSAGES = TextContainer.LIB_QUESTION_MESSAGES
    SUCCESS_MESSAGES = TextContainer.SUCCESS_MESSAGES
else:
    EXIT_MESSAGES = TextContainer_KZ.EXIT_MESSAGES
    PERMISSION_MESSAGES = TextContainer_KZ.PERMISSION_MESSAGES
    LIB_QUESTION_MESSAGES = TextContainer_KZ.LIB_QUESTION_MESSAGES
    SUCCESS_MESSAGES = TextContainer_KZ.SUCCESS_MESSAGES

LOCK_FILE: str = "/tmp/shooting_gallery.lock"
lock_fd = None

class BaseTerminalStrategy:
    def __init__(self, libs: List[str]):
        self.libs = libs

    def build_subprocess_cmd(self, inner_cmd_str: str) -> List[str]:
        raise NotImplementedError

    def get_current_package_args(self) -> Dict[str, str]:
        return {
            "bin": "apt",
            "update_cmd": "update -qq",
            "check_cmd": ["dpkg-query", "-W", "-f=${Status}"],
            "check_marker": "installed"
        }

class GnomeTerminalStrategy(BaseTerminalStrategy):
    def build_subprocess_cmd(self, inner_cmd_str: str) -> List[str]:
        return ["gnome-terminal", "--wait", "--", "bash", "-c", inner_cmd_str]

class AstraTerminalStrategy(BaseTerminalStrategy):
    def build_subprocess_cmd(self, inner_cmd_str: str) -> List[str]:
        return ["fly-term", "-e", f"bash -c '{inner_cmd_str}'"]

class MosTerminalStrategy(BaseTerminalStrategy):
    def get_current_package_args(self) -> Dict[str, str]:
        return {
            "bin": "dnf",
            "update_cmd": "makecache -q",
            "check_cmd": ["rpm", "-q"],
            "check_marker": "zero_exit_code"
        }

    def build_subprocess_cmd(self, inner_cmd_str: str) -> List[str]:
        return ["konsole", "-e", "bash", "-c", f"{inner_cmd_str}; exit"]

UBUNTU_STRATEGY = GnomeTerminalStrategy(libs=["v4l-utils", "python3-tk"])
ASTRA_STRATEGY = AstraTerminalStrategy(libs=["v4l-utils", "python3-tk"])
MOS_STRATEGY = MosTerminalStrategy(libs=["v4l-utils"])

json_path: str = os.path.join(BASE_DIR, PathConfig.BOOTSTRAP_JSON_DEVELOPER_SETTINGS_PATH)
developer_settings = JsonPresenter.get_instance().read_json_file(json_path)
current_systems_keys = developer_settings[JsonKeyConfig.CURRENT_SYSTEM[0]]

CURRENT_STRATEGY: BaseTerminalStrategy = UBUNTU_STRATEGY
CURRENT_PACKAGE_MANAGER = {}

if current_systems_keys[JsonKeyConfig.UBUNTU_KEY]:
    CURRENT_STRATEGY = UBUNTU_STRATEGY

if current_systems_keys[JsonKeyConfig.MOS_KEY]:
    CURRENT_STRATEGY = MOS_STRATEGY

if current_systems_keys[JsonKeyConfig.ASTRA_KEY]:
    CURRENT_STRATEGY = ASTRA_STRATEGY

CURRENT_PACKAGE_MANAGER = CURRENT_STRATEGY.get_current_package_args()

LIBS: List[str] = CURRENT_STRATEGY.libs
DOWNLOAD_CMD: List[str] = ["pkexec", CURRENT_PACKAGE_MANAGER["bin"], "install", "-y"] + LIBS

def check_single_instance():
    global lock_fd
    try:
        lock_fd = open(LOCK_FILE, 'w')
        fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        lock_fd.write(str(os.getpid()))
        lock_fd.flush()
    except IOError:
        sys.exit(0)

def get_installed_packages(package_names: List[str]) -> List[str]:
    installed = []
    check_cmd = CURRENT_PACKAGE_MANAGER["check_cmd"]
    marker = CURRENT_PACKAGE_MANAGER["check_marker"]

    for pkg in package_names:
        result = subprocess.run(check_cmd + [pkg], capture_output=True, text=True)

        if marker == "zero_exit_code":
            if result.returncode == 0:
                installed.append(pkg)
        else:
            if marker in result.stdout:
                installed.append(pkg)
    return installed

def get_uninstalled_packages(package_names: List[str]) -> List[str]:
    uninstalled = []
    check_cmd = CURRENT_PACKAGE_MANAGER["check_cmd"]
    marker = CURRENT_PACKAGE_MANAGER["check_marker"]

    for pkg in package_names:
        result = subprocess.run(check_cmd + [pkg], capture_output=True, text=True)

        if marker == "zero_exit_code":
            if result.returncode != 0:
                uninstalled.append(pkg)
        else:
            if marker not in result.stdout:
                uninstalled.append(pkg)
    return uninstalled

def _ask_message_box(title: str, text: str) -> bool:
    reply = QMessageBox.question(None, title, text, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    return reply == QMessageBox.Yes

def message_box_info(title: str, text: str):
    _ = QApplication.instance() or QApplication(sys.argv)
    QMessageBox.information(None, title, text)

def exit_app(exception=None):
    if exception:
        message_box_info(EXIT_MESSAGES[0], EXIT_MESSAGES[1].format(exception))
    sys.exit(0)

def run_main_game_async():
    if os.path.exists(MAIN_APP_BIN):
        os.chmod(MAIN_APP_BIN, 0o755)
        subprocess.Popen([MAIN_APP_BIN], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def start_app():
    splash = QWidget()
    splash.setWindowFlags(
        Qt.WindowStaysOnTopHint |
        Qt.FramelessWindowHint |
        Qt.X11BypassWindowManagerHint
    )

    label = QLabel(splash)

    if os.path.exists(GIF_PATH):
        movie = QMovie(GIF_PATH)
        label.setMovie(movie)

        screen_geometry = QApplication.desktop().screenGeometry()

        splash.setGeometry(screen_geometry)
        label.setGeometry(screen_geometry)
        label.setAlignment(Qt.AlignCenter)

        label.setScaledContents(True)
        movie.frameChanged.connect(
            lambda: label.setPixmap(
                movie.currentPixmap().scaled(
                    screen_geometry.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation)))

        splash.setStyleSheet("background-color: black;")

        splash.showFullScreen()
        movie.start()

        frame_count = movie.frameCount()
        frame_delay = movie.nextFrameDelay() if movie.nextFrameDelay() > 0 else 100

        if frame_count > 0:
            one_loop_duration = frame_count * frame_delay
            total_duration = one_loop_duration * 4
        else:
            total_duration = 8000

    else:
        splash.setStyleSheet("background-color: black;")
        splash.showFullScreen()
        total_duration = 3000

    run_main_game_async()

    def clear_end_exit():
        splash.close()
        try:
            os.remove(LOCK_FILE)
        except OSError:
            pass
        sys.exit(0)

    QTimer.singleShot(total_duration, clear_end_exit)

    sys.exit(app.exec_())

if __name__ == "__main__":
    check_single_instance()

    app = QApplication(sys.argv)

    uninstalled_libs = get_uninstalled_packages(LIBS)

    if not uninstalled_libs:
        start_app()
        sys.exit(0)

    if _ask_message_box(PERMISSION_MESSAGES[0], PERMISSION_MESSAGES[1]):
        try:
            if _ask_message_box(LIB_QUESTION_MESSAGES[0], LIB_QUESTION_MESSAGES[1].format(uninstalled_libs)):
                if uninstalled_libs:
                    inner_cmd_str = (
                        f"pkexec bash -c 'set -e; "
                        f"{CURRENT_PACKAGE_MANAGER['bin']} {CURRENT_PACKAGE_MANAGER['update_cmd']} && "
                        f"{CURRENT_PACKAGE_MANAGER['bin']} install -y {' '.join(uninstalled_libs)}; exit'"
                    )
                    final_cmd = CURRENT_STRATEGY.build_subprocess_cmd(inner_cmd_str)

                    subprocess.run(final_cmd, check=True)
                    message_box_info(SUCCESS_MESSAGES[0], SUCCESS_MESSAGES[1])
                    start_app()
                else:
                    start_app()
            else:
                start_app()
        except Exception as ex:
            exit_app(ex)
    else:
        exit_app()