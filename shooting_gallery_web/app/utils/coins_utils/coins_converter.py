from app.entitys.shooting_mods import ShootingMods
from typing import List, Tuple


class CoinsConverter:
    @staticmethod
    def ConvertCoins(point: int) -> int:
        counter: int = 0

        for _ in range(point, 10):
            counter += 1

        return counter

    @staticmethod
    def CheckCoinDistance(coin: int, playerId: int) -> int:
        correctCoin: int = 0
        maxCoins: int = 10

        if maxCoins > coin >= 0 and playerId:
            correctCoin: int = CoinsConverter.ConvertCoins(coin)

        return correctCoin

    @staticmethod
    def convert_coin_by_type(coins: List[int], playerId: int, shooting_mods: ShootingMods,
                             isLaserInsideContour: bool) -> Tuple[bool, int]:
        laserIsProcessed: bool = False
        validatedPoint: int = 0

        if coins:
            validatedPoint: int = CoinsConverter.CheckCoinDistance(min(coins), playerId)
            laserIsProcessed: bool = True

            if not shooting_mods.radius_mode:  # Не круглая цель.
                if not shooting_mods.circle_state:  # Не используем модель на основе радиусного вычисления.
                    if isLaserInsideContour:  # Нашли лазер в контуре.
                        if shooting_mods.idpa_mode:  # IDPA - mod.
                            validatedPoint: int = 1

                        if shooting_mods.game_mode:  # Game - mod.
                            validatedPoint: int = 1

                    if not isLaserInsideContour:  # Не нашли лазер в контуре.
                        validatedPoint: int = 0

                if shooting_mods.circle_state:  # Используем модель на основе радиусного вычисления.
                    if validatedPoint > 0:
                        validatedPoint: int = 1

            if shooting_mods.radius_mode:  # Круглая цель.
                validatedPoint: int = CoinsConverter.CheckCoinDistance(min(coins), playerId)

        return laserIsProcessed, validatedPoint
