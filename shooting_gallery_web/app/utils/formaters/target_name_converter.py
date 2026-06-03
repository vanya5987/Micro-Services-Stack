from app.api.database_api.DataStorageGetter import DataStorageGetter
from app.api.database_api.TargetRepository import TargetRepository

class TargetNameConverter:
    def __init__(self):
        data_storage_getter = DataStorageGetter()
        self.target_repository = TargetRepository(data_storage_getter)

        self.target = None

    def get_current_target(self, target_name: str):
        if self.target is None:
            self.target = self.target_repository.GetExerciseNameByTargetName(target_name)

        return self.target[0]