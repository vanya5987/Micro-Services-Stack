from shared.configs.core_configs.target_config.ParentTargetContainer import ParentTargetContainer

from typing import *
import numpy as np


class PlayerFinder:
    MAX_PLAYER_COUNT: int = 5

    @staticmethod
    def find_closest_player(laser: Optional[Tuple[int, int]], centers: Dict[int, Tuple[int, int]], radii: List[int]) \
            -> Tuple[Optional[int], float]:
        closestPlayerId: Optional[int] = None
        minDistance: float = float('inf')

        for playerId, center in centers.items():
            if center is None or radii is None:
                continue

            distance: float = np.sqrt((laser[0] - center[0]) ** 2 + (laser[1] - center[1]) ** 2)

            if distance < minDistance:
                minDistance: float = distance
                closestPlayerId: int = playerId

        return closestPlayerId, minDistance

    @staticmethod
    def GetNearestPlayer(laserPoints: List[Tuple[int, int]], centers: Dict[int, Tuple[int, int]], radii: List[float]
                         ) -> Tuple[Dict[int, Tuple[Tuple[int, int], float]], Dict[int, Tuple[int, int]]]:
        playerToLaser: Dict[int, Tuple[Tuple[int, int], float]] = {}
        nearestLaserPoints: Dict[int, Tuple[int, int]] = {}

        for laserIndex in range(len(laserPoints)):
            if len(laserPoints) > len(centers):
                continue

            playerId, minDistance = PlayerFinder.find_closest_player(laserPoints[laserIndex], centers, radii)

            if playerId is not None:
                if playerId not in playerToLaser or minDistance < playerToLaser[playerId][1]:
                    playerToLaser[playerId] = (laserPoints[laserIndex], minDistance)
                    nearestLaserPoints[playerId] = laserPoints[laserIndex]

        nearestLaserPoints: Dict[int, Tuple[int, int]] = {playerId: point for playerId, point in
                                                          nearestLaserPoints.items()
                                                          if point != (0, 0)}
        return playerToLaser, nearestLaserPoints

    # Получает радиусы для каждой цели.
    @staticmethod
    def get_target_radii_handler(maxCircleDiameter: float, frameDistance: float) -> List[int]:
        radii: List[int] = []  # Радиусы для текущего ROI.

        for i in range(ParentTargetContainer.MAX_RADII_COUNT - 1):
            radii.append(int(maxCircleDiameter - (frameDistance * i)))

        radii.append(maxCircleDiameter)

        return radii
