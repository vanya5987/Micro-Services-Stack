from app.entitys.session_entity.player_params_entity import PlayerParams

from typing import *

class BulletsCalculator:
    def __init__(self):
        self.zeroBulletStatusShown: Dict[int, bool] = {} #Словарь для отслеживания показа статуса "нулевых пуль".

    #Проверяет, закончились ли патроны у игрока.
    def CheckBulletIsLast(self, playerId: int, player_params: Dict[int, PlayerParams]) -> bool:
        isLastShoot: bool = False
            
        if playerId in player_params and player_params[playerId].bullets > 1: #Если выстрел не последний.
            BulletsCalculator.RemoveBullet(playerId, player_params)

            isLastShoot: bool = True  
        else: #Если выстрел последний.
            if not self.zeroBulletStatusShown.get(playerId, False): #Проверяем, был ли уже показан статус "нулевых пуль" для этого игрока.
                isLastShoot: bool = True

                BulletsCalculator.RemoveBullet(playerId, player_params)

                self.zeroBulletStatusShown[playerId] = True #Помечаем, что статус был показан.

        return isLastShoot

    @staticmethod
    def RemoveBullet(playerId: int, player_params: Dict[int, PlayerParams]):
        if playerId in player_params: #Вычитаем пулю для roiIndex, если он присутствует в bulletsForPlayer.
            player_params[playerId].bullets -= 1
        else:
            if player_params[playerId].bullets < 0: #Убедитесь, что количество не стало отрицательным.
                player_params[playerId].bullets = 0  #Устанавливаем в 0, если меньше 0.
