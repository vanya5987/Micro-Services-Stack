from app.api.database_api.DataStorageGetter import DataStorageGetter
from app.api.database_api.DbCreator import Shooting, Shooters, Exercise, Shoots

from typing import *
from datetime import datetime, timedelta


class ShootingRepository:
    def __init__(self, dataStorageGetter: DataStorageGetter):
        self.dataStorageGetter: DataStorageGetter = dataStorageGetter

    def ApplyDefaultFilters(self, query):
        return query.filter(Shooting.ShootersID != 0, Shooting.PdfFileName != "")

    # Обновляет стрельбу по следующим аргументам: Сумма поинтов, Дата стрельб, кол-во потраченных патрон, кол-во потраченного времени, имя PDF - файла.
    def UpdateCurrentShootingByOptionalID(self, shootingID: int, shooterID: int, sumPoints: int, spentBulletCount: int,
                                          spentTime: str, pdfNameFile: str, shootingDate: str) -> bool:
        try:
            self.dataStorageGetter.session.query(Shooting).filter(Shooting.ID == shootingID).update(
                {"ShootingDate": shootingDate,
                 "ShootersID": shooterID, "SumPoints": sumPoints, "BulletSpentShooting": spentBulletCount,
                 "TimeSpentShooting": spentTime, "PdfFileName": pdfNameFile})
            self.dataStorageGetter.session.commit()
            return True
        except Exception:
            return False

    # Возвращает список стрельб из кортежей по ID стрелка.
    def GetAllShootingByPlayerID(self, playerID: int) -> List[Tuple[int, int, int, int, str, int, str, str]]:
        query = self.dataStorageGetter.session.query(
            Shooting.ID, Shooters.ID, Exercise.ID, Shooting.SumPoints,
            Shooting.ShootingDate, Shooting.BulletSpentShooting,
            Shooting.TimeSpentShooting, Shooting.PdfFileName
        ).join(Shooters, Shooting.ShootersID == Shooters.ID).join(
            Exercise, Shooting.ExerciseID == Exercise.ID
        ).filter(Shooting.ShootersID == playerID)

        shootings = self.ApplyDefaultFilters(query).all()

        return shootings

    # Возвращает список стрельб из кортежей по ID стрелка, ID группы стрелка и ID упражнения.
    def GetAllShootingByOptionalID(self, playerID: int, groupID: int, exercsieID: int
                                   ) -> List[Tuple[int, int, int, int, str, int, str, str]]:
        query = self.dataStorageGetter.session.query(
            Shooting.ID, Shooters.ID, Exercise.ID, Shooting.SumPoints,
            Shooting.ShootingDate, Shooting.BulletSpentShooting,
            Shooting.TimeSpentShooting, Shooting.PdfFileName
        ).join(Shooters, Shooting.ShootersID == Shooters.ID).join(
            Exercise, Shooting.ExerciseID == Exercise.ID
        ).filter(Shooters.ID == playerID).filter(
            Shooters.GroupID == groupID).filter(
            Shooting.ExerciseID == exercsieID)

        shootings = self.ApplyDefaultFilters(query).all()

        return shootings

    # Получает все стрельбы сортируя их по скорости выполнения упражнения.
    def GetAllShootingPerShootingTime(self, playerID: int, groupID: int, exercsieID: int
                                      ) -> List[Tuple[int, int, int, int, str, int, str, str]]:
        query = self.dataStorageGetter.session.query(
            Shooting.ID, Shooters.ID, Exercise.ID, Shooting.SumPoints,
            Shooting.ShootingDate, Shooting.BulletSpentShooting,
            Shooting.TimeSpentShooting, Shooting.PdfFileName
        ).join(Shooters, Shooting.ShootersID == Shooters.ID).join(
            Exercise, Shooting.ExerciseID == Exercise.ID
        ).filter(Shooters.ID == playerID).filter(
            Shooters.GroupID == groupID).filter(
            Shooting.ExerciseID == exercsieID).order_by(
            Shooting.TimeSpentShooting.asc())

        shootings = self.ApplyDefaultFilters(query).all()

        return shootings

    # Получает все стрельбы сортируя их по кол-ву набранных очков.
    def GetAllShootingPerGettingPoints(self, playerID: int, groupID: int, exercsieID: int
                                       ) -> List[Tuple[int, int, int, int, str, int, str, str]]:
        query = self.dataStorageGetter.session.query(
            Shooting.ID, Shooters.ID, Exercise.ID, Shooting.SumPoints,
            Shooting.ShootingDate, Shooting.BulletSpentShooting,
            Shooting.TimeSpentShooting, Shooting.PdfFileName
        ).join(Shooters, Shooting.ShootersID == Shooters.ID).join(
            Exercise, Shooting.ExerciseID == Exercise.ID
        ).filter(Shooters.ID == playerID).filter(
            Shooters.GroupID == groupID).filter(
            Shooting.ExerciseID == exercsieID).order_by(
            Shooting.SumPoints.desc())

        shootings = self.ApplyDefaultFilters(query).all()
        return shootings

    # Получает все записи за указанное время по тегу (Месяц - month, Полгода - halfYear, год - year)
    def GetAllShootingPerDateTime(self, playerID: int, groupID: int, exercsieID: int, timeTag: str
                                  ) -> List[Tuple[int, int, int, int, str, int, str, str]]:  # %Y-%m-%d %H:%M:%S
        currentTime = datetime.now()
        time: str = ""

        if timeTag == "month":
            time = (currentTime - timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S')
        elif timeTag == "halfYear":
            time = (currentTime - timedelta(days=180)).strftime('%Y-%m-%d %H:%M:%S')
        elif timeTag == "year":
            time = (currentTime - timedelta(days=365)).strftime('%Y-%m-%d %H:%M:%S')

        current_time_str = currentTime.strftime('%Y-%m-%d %H:%M')

        query = self.dataStorageGetter.session.query(
            Shooting.ID, Shooters.ID, Exercise.ID, Shooting.SumPoints,
            Shooting.ShootingDate, Shooting.BulletSpentShooting,
            Shooting.TimeSpentShooting, Shooting.PdfFileName
        ).join(Shooters, Shooting.ShootersID == Shooters.ID
               ).join(Exercise, Shooting.ExerciseID == Exercise.ID
                      ).filter(Shooters.ID == playerID
                               ).filter(Shooters.GroupID == groupID
                                        ).filter(Shooting.ExerciseID == exercsieID
                                                 ).filter(Shooting.ShootingDate >= time
                                                          ).filter(Shooting.ShootingDate <= current_time_str
                                                                   ).order_by(Shooting.ShootingDate.asc())

        shootings = self.ApplyDefaultFilters(query).all()

        return shootings

    # Возвращает список стрельб по ID стрелка и ID группы.
    def GetAllShootingByGroupAndPlayer(self, playerID: int, groupID: int
                                       ) -> List[Tuple[int, int, int, int, str, int, str, str]]:
        query = self.dataStorageGetter.session.query(
            Shooting.ID, Shooters.ID, Exercise.ID, Shooting.SumPoints,
            Shooting.ShootingDate, Shooting.BulletSpentShooting,
            Shooting.TimeSpentShooting, Shooting.PdfFileName
        ).join(Shooters, Shooting.ShootersID == Shooters.ID).join(
            Exercise, Shooting.ExerciseID == Exercise.ID
        ).filter(Shooters.ID == playerID).filter(
            Shooters.GroupID == groupID)

        shootings = self.ApplyDefaultFilters(query).all()

        return shootings

    # Получает список стрельб по ID типа упражнения.
    def GetAllShootingByExerciseType(self, exerciseType: int) -> List[Tuple[int, int, int, int, str, int, str, str]]:
        exerciseTypeIsExist = self.dataStorageGetter.session.query(
            self.dataStorageGetter.session.query(Exercise)
            .filter(Exercise.ExerciseType == exerciseType).exists()
        ).scalar()

        query = self.dataStorageGetter.session.query(
            Shooting.ID, Shooters.ID, Exercise.ID, Shooting.SumPoints,
            Shooting.ShootingDate, Shooting.BulletSpentShooting,
            Shooting.TimeSpentShooting, Shooting.PdfFileName
        ).join(Shooters, Shooting.ShootersID == Shooters.ID).join(
            Exercise, Shooting.ExerciseID == Exercise.ID
        ).filter(Exercise.ExerciseType == exerciseType)

        shootings = self.ApplyDefaultFilters(query).all()

        return shootings

    # Возвращает список стрельб по ID группы.
    def GetAllShootingsByGroupID(self, groupID: int) -> List[Tuple[int, int, int, int, str, int, str, str]]:
        query = self.dataStorageGetter.session.query(
            Shooting.ID, Shooters.ID, Exercise.ID, Shooting.SumPoints,
            Shooting.ShootingDate, Shooting.BulletSpentShooting,
            Shooting.TimeSpentShooting, Shooting.PdfFileName
        ).join(Shooters, Shooting.ShootersID == Shooters.ID).join(
            Exercise, Shooting.ExerciseID == Exercise.ID
        ).filter(Shooters.GroupID == groupID)

        shootings = self.ApplyDefaultFilters(query).all()

        return shootings

    # Возвращает один кортеж с записями о стрельбе по индексу.
    def GetShootingByID(self, shootingID: int) -> Tuple[int, int, int, int, str, int, str, str]:
        query = self.dataStorageGetter.session.query(
            Shooters.ID,
            Exercise.ID,
            Shooting.SumPoints,
            Shooting.ShootingDate,
            Shooting.BulletSpentShooting,
            Shooting.TimeSpentShooting,
            Shooting.PdfFileName
        ).join(Shooters, Shooting.ShootersID == Shooters.ID).join(
            Exercise, Shooting.ExerciseID == Exercise.ID
        ).filter(Shooting.ID == shootingID)

        currentExercise = self.ApplyDefaultFilters(query).first()

        return currentExercise

    # Создание стрельбы.
    def CreateShooting(self, exerciseID: int) -> bool:
        newShooting = Shooting(ShootersID=0, ExerciseID=exerciseID, SumPoints=0, ShootingDate="",
                               BulletSpentShooting=0, TimeSpentShooting="", PdfFileName="")

        self.dataStorageGetter.session.add(newShooting)
        self.dataStorageGetter.session.commit()

        return newShooting.ID

    # Удаление стрельбы по индексу и всех зависимостей стрельбы.
    def RemoveShootingByID(self, shootingID: int) -> bool:
        try:
            self.dataStorageGetter.session.query(Shooting).filter(Shooting.ID == shootingID).delete()
            self.dataStorageGetter.session.query(Shoots).filter(Shoots.ShootingID == shootingID).delete()
            self.dataStorageGetter.session.commit()
            return True
        except:
            return False

    # Возвращает имя PDF файла из результатов стрельбы.
    def GetPdfName(self, shootingID: int) -> str:
        pdfFileName: str = self.dataStorageGetter.session.query(Shooting.PdfFileName).filter(
            Shooting.ID == shootingID).first()

        return pdfFileName[0]
