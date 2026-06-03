from PyQt5.QtWidgets import QWidget

from app.api.database_api.DataStorageGetter import DataStorageGetter
from app.api.database_api.ShootingRepository import ShootingRepository
from app.api.database_api.ShootsRepository import ShootsRepository
from app.api.database_api.ExerciseRepository import ExerciseRepository
from app.api.database_api.ShootersRepository import ShootersRepository
from app.api.database_api.GroupRepository import GroupRepository
from app.api.database_api.TargetRepository import TargetRepository

from shared.pathings.path_config import PathConfig
from app.services.draw_services.point_drawer_to_target import PointDrawerToTarget
from shared.configs.core_configs.pdf_config import PdfConfig
from app.services.docs_services.shooting_report_generator import ShootingReportGenerator

from PyQt5.QtGui import QPixmap
import os

from typing import *


class MissingPdfGenerator(QWidget):
    def __init__(self, shootingID: int, is_override_path: bool = False, override_path: str = ""):
        super().__init__()

        dataStorageGetter = DataStorageGetter()
        shootsRepository = ShootsRepository(dataStorageGetter)
        shootingRepository = ShootingRepository(dataStorageGetter)
        exerciseRepository = ExerciseRepository(dataStorageGetter)
        shooterRepository = ShootersRepository(dataStorageGetter)
        groupRepository = GroupRepository(dataStorageGetter)
        targetRepository = TargetRepository(dataStorageGetter)

        shootings = shootingRepository.GetShootingByID(shootingID)
        shoots = shootsRepository.GetAllShootsByShootingIndex(shootingID)
        shooter = shooterRepository.GetShooterByShooterID(shootings[0])
        exercise = exerciseRepository.GetCurrentExerciseByID(shootings[1])
        _, target_name = targetRepository.GetTargetByIndex(exercise[3])

        laserPoints: List[List[int]] = [[laserX, laserY] for _, _, _, _, laserX, laserY in shoots]
        target: QPixmap = QPixmap(os.path.join(PathConfig.PRINT_TARGETS, target_name))

        for laserPointIndex in range(len(laserPoints)):
            target = PointDrawerToTarget().GetTargetWithPointHighRes(laserPoints[laserPointIndex], target,
                                                                     laserPointIndex + 1)

        playerSurname: str = shooter[1]
        exerciseName: str = exercise[0]
        groupName: str = groupRepository.GetGroupNameByID(shooter[2])
        currentPoint: List[int] = [pointForBullet for _, pointForBullet, _, _, _, _ in shoots]
        shootTimes: List[str] = [shootingTime for _, _, shootingTime, _, _, _ in shoots]
        playerID: int = shootings[0]
        playerName: str = shooter[0]
        pdfConfig: PdfConfig = PdfConfig(target=target, playerSurname=playerSurname, exercsieName=exerciseName,
                                         groupName=groupName,
                                         currentPoints=currentPoint, shootTimes=shootTimes, playerID=playerID,
                                         playerName=playerName)
        pdfGenerator = ShootingReportGenerator(pdfConfig)
        pdfGenerator.GenerateReport(pdfIsMissing=True, shootingID=shootingID, is_override_path=is_override_path,
                                    override_path=override_path)
