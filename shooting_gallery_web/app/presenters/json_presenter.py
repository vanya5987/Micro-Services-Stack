import threading

from app.api.json_api.json_controller import JsonController


class JsonPresenter:
    _instance = None
    _lock = threading.Lock()

    @staticmethod
    def get_instance():
        if JsonPresenter._instance is None:
            with JsonPresenter._lock:
                if JsonPresenter._instance is None:
                    JsonPresenter._instance = JsonController()

        return JsonPresenter._instance
