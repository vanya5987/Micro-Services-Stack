from app.api.database_api.DataStorageGetter import DataStorageGetter
from app.api.database_api.DbCreator import Shoots, Shooting

from typing import *


class ShootsRepository:
    def __init__(self, dataStorageGetter: DataStorageGetter):
        self.dataStorageGetter: DataStorageGetter = dataStorageGetter

    # Возвращает все выстрелы по индексу стрельбы.
    def GetAllShootsByShootingIndex(self, shootingID: int) -> List[Tuple[int, int, str, int]]:
        shootings = self.dataStorageGetter.session.query(
            Shoots.BulletNumber,
            Shoots.PointsForBullet,
            Shoots.ShootingStartTime,
            Shooting.ID,
            Shoots.LaserX,
            Shoots.LaserY).join(
            Shooting, Shoots.ShootingID == Shooting.ID).filter(Shooting.ID == shootingID).all()

        return shootings

    # Создает выстрел.
    def CreateShoots(self, bulletNumber: int, pointsForBullet: int, shootingStartTime: str, shootingID: int,
                     laserX: int, laserY: int):
        existingShoot = self.dataStorageGetter.session.query(Shoots).filter_by(
            ShootingID=shootingID, BulletNumber=bulletNumber).first()

        if existingShoot is not None:
            return

        self.dataStorageGetter.session.add(Shoots(
            BulletNumber=bulletNumber,
            PointsForBullet=pointsForBullet,
            ShootingStartTime=shootingStartTime,
            ShootingID=shootingID,
            LaserX=laserX,
            LaserY=laserY
        ))

        self.dataStorageGetter.session.commit()
