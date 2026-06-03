from app.api.database_api.DataStorageGetter import DataStorageGetter
from app.api.database_api.DbCreator import Group, Shooters

from typing import *


class GroupRepository:
    def __init__(self, dataStorageGetter: DataStorageGetter):
        self.dataStorageGetter: DataStorageGetter = dataStorageGetter

    # Возвращает словарь всех групп. Формат вывода: (Индекс группы, имя группы.)
    def GetAllGroup(self) -> List[Tuple[int, str]]:
        groups = self.dataStorageGetter.session.query(Group.ID, Group.GroupName).all()
        return groups

    # Получает имя группы по ID группы.
    def GetGroupNameByID(self, groupID: int):
        return self.dataStorageGetter.session.query(Group.GroupName).filter(Group.ID == groupID).first()[0]

    # Возвращает список групп по имени и фамилии игрока.
    def GetAllGroupsByNameAndSurname(self, playerName: str, playerSurname: str) -> Tuple[int, str]:
        groups = self.dataStorageGetter.session.query(Shooters.GroupID, Group.GroupName).join(Group,
                                                                                              Shooters.GroupID == Group.ID
                                                                                              ).filter(
            Shooters.PlayerSurname == playerSurname).filter(Shooters.PlayerName == playerName
                                                            ).filter(Shooters.GroupID == Group.ID).all()

        return groups

    # Добавляет группу по имени.
    def CreateGroupByName(self, groupName: str) -> bool:
        try:
            self.dataStorageGetter.session.add(Group(GroupName=groupName))
            self.dataStorageGetter.session.commit()
            return True
        except:
            self.dataStorageGetter.session.rollback()
            return False

    # Удаляет группу по индексу.
    def RemoveGroupByID(self, groupID: int) -> bool:
        try:
            self.dataStorageGetter.session.query(Shooters).filter(Shooters.GroupID == groupID).delete()
            self.dataStorageGetter.session.query(Group).filter(Group.ID == groupID).delete()
            self.dataStorageGetter.session.commit()
            return True
        except Exception:
            self.dataStorageGetter.session.rollback()
            return False
