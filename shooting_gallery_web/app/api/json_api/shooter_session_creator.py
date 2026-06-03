from app.presenters.json_presenter import JsonPresenter
from shared.pathings.path_config import PathConfig

from typing import *


class ShooterSessionController:
    def __init__(self):
        self.dataLoader = JsonPresenter.get_instance()

        self.lastData: Dict[int, Dict] = {shooterID: {} for shooterID in range(1, 6)}

    def get_data_by_shooter_id(self, shooterID: int):
        jsonPath: str = PathConfig.SHOOTING_SESSION_PATHS.format(shooterID)

        return self.dataLoader.read_json_file(jsonPath)
