from app.api.database_api.DataStorageGetter import DataStorageGetter
from app.api.database_api.DbCreator import Targets, Exercise

from typing import *


class TargetRepository:
    def __init__(self, dataStorageGetter: DataStorageGetter):
        self.dataStorageGetter: DataStorageGetter = dataStorageGetter

    def GetExerciseNameByTargetName(self, target_name: str) -> Tuple[str]:
        exercise_name = self.dataStorageGetter.session.query(
            Targets.NameTarget).filter(Targets.FileTarget == target_name).first()

        return exercise_name

    # Возвращает имя мишени и название файла мишени по индексу.
    def GetTargetByIndex(self, targetID: int) -> Tuple[str, str]:
        targetName = self.dataStorageGetter.session.query(
            Targets.NameTarget,
            Targets.FileTarget
        ).filter(Targets.ID == targetID).first()

        return targetName

    # Возвращает имена мишеней для отображения в frontend среде. Формат вывода (Индекс мишени, имя мишени).
    def GetAllTargetName(self) -> List[Tuple[int, str]]:
        targetsNames = self.dataStorageGetter.session.query(Targets.ID, Targets.NameTarget).all()

        return targetsNames

    # Возвращает имена файлов мишеней. Формат вывода (Индекс мишени, имя файла).
    def GetAlltargetFile(self) -> List[Tuple[int, str]]:
        targetsFileNames = self.dataStorageGetter.session.query(Targets.ID, Targets.FileTarget).all()

        return targetsFileNames

    # Добавляет мишень.
    def CreateTarget(self, nameTarget: str, fileTarget: str) -> bool:
        try:
            self.dataStorageGetter.session.add(Targets(NameTarget=nameTarget, FileTarget=fileTarget))
            self.dataStorageGetter.session.commit()
            return True
        except:
            return False

    # Удаляет мишень по индексу.
    def DeleteTatgetByIndex(self, targetID: int) -> bool:
        try:
            self.dataStorageGetter.session.query(Targets).filter(Targets.ID == targetID).delete()
            self.dataStorageGetter.session.query(Exercise).filter(Exercise.TargetID == targetID).delete()
            self.dataStorageGetter.session.commit()
            return True
        except Exception:
            return False
