from app.api.database_api.DataStorageGetter import DataStorageGetter
from app.api.database_api.DbCreator import Shooters, Group

from typing import *


class ShootersRepository:
    def __init__(self, dataStorageGetter: DataStorageGetter):
        self.dataStorageGetter: DataStorageGetter = dataStorageGetter

    def GetShooterByShooterID(self, shooterID: int):
        shooter = self.dataStorageGetter.session.query(
            Shooters.PlayerName,
            Shooters.PlayerSurname,
            Shooters.GroupID
        ).join(Group, Shooters.GroupID == Group.ID).filter(Shooters.ID == shooterID).first()

        return shooter

    # Получает всех стрелков.
    def GetAllShooters(self) -> List[Tuple[int, str, str]]:
        allShooters = self.dataStorageGetter.session.query(Shooters.ID, Shooters.PlayerName,
                                                           Shooters.PlayerSurname, Shooters.GroupID).join(Group,
                                                                                                          Shooters.GroupID == Group.ID).all()

        return allShooters

    # Получает всех стрелков по индексу группы. Формат вывода: (Инекс стрелка, имя стрелка, фамилия стрелка).
    def GetAllShootersByGroupId(self, groupID: int) -> List[Tuple[int, str, str]]:
        shootersInGroup = self.dataStorageGetter.session.query(Shooters.ID, Shooters.PlayerName,
                                                               Shooters.PlayerSurname).join(
            Group, Shooters.GroupID == Group.ID).filter(Group.ID == groupID).all()

        return shootersInGroup

    # Возвращает стрелка по префиксу фамилии.
    def GetShooterByPrifixSurname(self, prefixSurname: str) -> List[Tuple[int, str, str, int]]:
        shooters = self.dataStorageGetter.session.query(Shooters.ID, Shooters.PlayerName, Shooters.PlayerSurname,
                                                        Group.ID).join(Group, Shooters.GroupID == Group.ID).all()
        filtredShooters: List[Tuple[int, str, str, int]] = [(playerID, playerName, playerSurname, playerGroupName) for (
            playerID, playerName, playerSurname, playerGroupName) in shooters if
                                                            playerSurname.startswith(prefixSurname)]

        return filtredShooters

    # Добавляет стрелка.
    def CreateShooters(self, shootersName: str, shootersSurname: str, groupName: Optional[str] = None) -> bool:
        try:
            if groupName is None:
                defaultGroupName: str = "Default Group"
                group = self.dataStorageGetter.session.query(Group).filter_by(GroupName=defaultGroupName).first()

                if not group:
                    group = Group(GroupName=defaultGroupName)
                    self.dataStorageGetter.session.add(group)
                    self.dataStorageGetter.session.flush()
            else:
                group = self.dataStorageGetter.session.query(Group).filter_by(GroupName=groupName).first()

                if not group:
                    group = Group(GroupName=groupName)
                    self.dataStorageGetter.session.add(group)
                    self.dataStorageGetter.session.flush()

            shooter = Shooters(PlayerName=shootersName, PlayerSurname=shootersSurname, GroupID=group.ID)
            self.dataStorageGetter.session.add(shooter)
            self.dataStorageGetter.session.commit()
            return True
        except Exception:
            self.dataStorageGetter.session.rollback()
            return False

    # Удаляет стрелка по индексу.
    def DeleteShootersByIndex(self, shooterID: int) -> bool:
        try:
            self.dataStorageGetter.session.query(Shooters).filter(Shooters.ID == shooterID).delete()
            self.dataStorageGetter.session.commit()
            return True
        except:
            self.dataStorageGetter.session.rollback()
            return False
