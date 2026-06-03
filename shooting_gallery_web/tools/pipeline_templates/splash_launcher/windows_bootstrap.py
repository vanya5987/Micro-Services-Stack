from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation

from app.utils.validators.check_programm_running import CheckProgramRunning
from locker_config import LockerConfig

import win32gui
import win32process
import sys
import subprocess
import psutil
import os

if CheckProgramRunning.app_is_running(LockerConfig.SPLASH_LOCKER_FILE):
    sys.exit(0)

# ===================== НАСТРОЙКИ =====================
# Пути по умолчанию (для запуска под интерпретатором)
DEFAULT_APP_PATH = LockerConfig.ABS_APP_PATH
DEFAULT_GIF_PATH = LockerConfig.ABS_GIF_PATH

MIN_SPLASH_TIME = 4000
CHECK_INTERVAL = 1000
# ======================================================

# Определяем базовую директорию
if getattr(sys, 'frozen', False):
    # exe через PyInstaller → текущая папка exe
    BASE_DIR = os.path.dirname(sys.executable)
else:
    # обычный запуск под интерпретатором
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Пути к ресурсам
APP_PATH = os.path.join(LockerConfig.RELATIVE_APP_PATH.format(BASE_DIR))
GIF_PATH = os.path.join(LockerConfig.RELATIVE_GIF_PATH.format(BASE_DIR))


def process_has_window(pid):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return len(hwnds) > 0


class SplashScreen(QLabel):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint)
        self.setAlignment(Qt.AlignCenter)

        self.movie = QMovie(GIF_PATH)
        self.setMovie(self.movie)
        self.movie.start()

        self.setWindowOpacity(1.0)

        screen = QApplication.primaryScreen()
        rect = screen.availableGeometry()
        self.setGeometry(rect)
        self.movie.setScaledSize(rect.size())

        self.show()  # Показываем сразу

    def resizeEvent(self, event):
        self.movie.setScaledSize(self.size())
        super().resizeEvent(event)


def create_splash_window_build():
    app = QApplication(sys.argv)
    splash = SplashScreen()

    process = subprocess.Popen(APP_PATH)

    min_time_passed = False
    window_ready = False
    closed = False
    timers = []

    def on_min_time():
        nonlocal min_time_passed
        min_time_passed = True
        try_close()

    def check_window():
        nonlocal window_ready
        if process_has_window(process.pid):
            window_ready = True
            try_close()
        else:
            QTimer.singleShot(CHECK_INTERVAL, check_window)

    def try_close():
        nonlocal closed
        if closed:
            return
        if min_time_passed and window_ready:
            closed = True
            fade_and_close()

    def fade_and_close():
        animation = QPropertyAnimation(splash, b"windowOpacity")
        animation.setDuration(400)
        animation.setStartValue(1.0)
        animation.setEndValue(0.0)

        def on_finished():
            splash.close()
            monitor_process(process.pid)

        animation.finished.connect(on_finished)
        animation.start()
        splash.animation = animation  # держим ссылку, чтобы не удалился

    def monitor_process(pid):
        def check_alive():
            if not psutil.pid_exists(pid):
                app.quit()

        timer = QTimer()
        timer.timeout.connect(check_alive)
        timer.start(1000)
        timers.append(timer)

    # Таймеры
    QTimer.singleShot(MIN_SPLASH_TIME, on_min_time)
    QTimer.singleShot(CHECK_INTERVAL, check_window)

    sys.exit(app.exec_())

create_splash_window_build()
