from app.api.database_api.DataStorageGetter import DataStorageGetter
from app.api.database_api.DbCreator import Exercise, Targets, Shooting

from app.presenters.json_presenter import JsonPresenter
from shared.pathings.path_config import PathConfig
from shared.configs.keys_configs.json_key_config import JsonKeyConfig

from typing import *


class ExerciseRepository:
    def __init__(self, dataStorageGetter: DataStorageGetter):
        self.dataStorageGetter: DataStorageGetter = dataStorageGetter
        self.json_loader = JsonPresenter.get_instance()

    # Возвращает список упражнений содержащий кортежи. Выборка по типу упражнений.
    def GetAllExerciseByExerciseType(self, exerciseType: int) -> List[Tuple[int, str, int, int, int, str, int, str]]:
        exercises = self.dataStorageGetter.session.query(Exercise.ID, Exercise.ExerciseName, Exercise.ShootersCount,
                                                         Exercise.ShotsCount, Targets.ID, Exercise.ExerciseDescription,
                                                         Exercise.ExerciseType,
                                                         Exercise.ExerciseTime, Exercise.WeaponType).join(Targets,
                                                                                                          Exercise.TargetID == Targets.ID
                                                                                                          ).filter(
            Exercise.ExerciseType == exerciseType).all()

        filtered_exercise = []
        current_data = self.json_loader.read_json_file(PathConfig.DEVELOPER_SETTINGS)

        for exercise in exercises:
            for _, weapon_type in current_data[JsonKeyConfig.WEAPON_TYPES[0]].items():
                if weapon_type[0]:
                    if weapon_type[1] == exercise[8]:
                        filtered_exercise.append(exercise)

        return filtered_exercise

    # Возвращает список упражнений содержащий кортежи
    def GetAllExercise(self) -> List[Tuple[int, str, int, int, int, str, int, str]]:
        exercises = (self.dataStorageGetter.session.query(Exercise.ID, Exercise.ExerciseName, Exercise.ShootersCount,
                                                          Exercise.ShotsCount, Targets.ID, Exercise.ExerciseDescription,
                                                          Exercise.ExerciseTime, Exercise.ExerciseType).
                     join(Targets, Exercise.TargetID == Targets.ID).all())

        return exercises

    # Возвращает кортеж дефолтного упражнения.
    def GetDefaultExercise(self, defaultExerciseID=1) -> Tuple[str, int, int, int, str, int, str]:
        defaultExercise = self.dataStorageGetter.session.query(Exercise.ID, Exercise.ExerciseName,
                                                               Exercise.ShootersCount,
                                                               Exercise.ShotsCount, Targets.ID,
                                                               Exercise.ExerciseDescription, Exercise.ExerciseType,
                                                               Exercise.ExerciseTime).join(Targets,
                                                                                           Exercise.TargetID == Targets.ID).filter(
            Exercise.ID ==
            defaultExerciseID).first()
        return defaultExercise

    # Обновляет описание упражнения по индексу упражнения.
    def UpdateExerciseDescription(self, exerciseID: int, exerciseDescription: str) -> bool:
        try:
            self.dataStorageGetter.session.query(Exercise).filter(Exercise.ID == exerciseID).update(
                {"ExerciseDescription": exerciseDescription})
            self.dataStorageGetter.session.commit()
            return True
        except Exception:
            return False

    # Обновляет кол-во стрелков и выстрелов по индексу упражнения.
    def UpdateExercisePlayerAndBulletCount(self, exerciseID: int, playerCount: int, bulletCount: int) -> bool:
        try:
            self.dataStorageGetter.session.query(Exercise).filter(Exercise.ID == exerciseID).update(
                {"ShootersCount": playerCount,
                 "ShotsCount": bulletCount})
            self.dataStorageGetter.session.commit()
            return True
        except Exception:
            return False

    # Добавляет упражнение.
    def CreateExercise(self, exerciseName: str, shootersCount: int, shootsCount: int, targetID: int,
                       exerciseDescription: str, exerciseType: int, exerciseTime: str) -> bool:
        try:
            newExercise = Exercise(ExerciseName=exerciseName, ShootersCount=shootersCount, ShotsCount=shootsCount,
                                   TargetID=targetID, ExerciseDescription=exerciseDescription,
                                   ExerciseType=exerciseType, ExerciseTime=exerciseTime)
            self.dataStorageGetter.session.add(newExercise)
            self.dataStorageGetter.session.commit()
            return True
        except:
            return False

    # Ищет все упражнения по ID стрельбы.
    def GetAllExerciseByShootingID(self, shootingID: int) -> List[int]:
        shootings = self.dataStorageGetter.session.query(Shooting.ExerciseID).filter(Shooting.ID == shootingID).all()

        return [shootingIndex[0] for shootingIndex in shootings]

    # Возвращает кортеж с текущим упражнением по индексу.
    def GetCurrentExerciseByID(self, exerciseID: int) -> Tuple[str, int, int, int, str, int, str]:
        currentExercise = self.dataStorageGetter.session.query(
            Exercise.ExerciseName,
            Exercise.ShootersCount,
            Exercise.ShotsCount,
            Targets.ID,
            Exercise.ExerciseDescription,
            Exercise.ExerciseType,
            Exercise.ExerciseTime
        ).join(Targets, Exercise.TargetID == Targets.ID).filter(Exercise.ID == exerciseID).first()

        return currentExercise
