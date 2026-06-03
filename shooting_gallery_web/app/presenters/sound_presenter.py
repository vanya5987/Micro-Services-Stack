import threading

from app.services.sound_services.sound_player import SoundPlayer


class SoundPresenter:
    _instance = None
    _lock = threading.Lock()

    @staticmethod
    def get_instance():
        if SoundPresenter._instance is None:
            with SoundPresenter._lock:
                if SoundPresenter._instance is None:
                    SoundPresenter._instance = SoundPlayer()

        return SoundPresenter._instance
