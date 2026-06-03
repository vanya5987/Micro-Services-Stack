from app.entitys.target_params_entity import TargetParams

import numpy as np
from typing import *

class LaserPositionChecker:
    @staticmethod
    def check_laser_position_to_radii(laser: float, center: float, border: float) -> float:
        if laser is not None and  center is not None and border is not None:
            if laser > border or laser <  center:
                return laser #Лазер находится между гранями.
            elif laser ==  center:
                return center #Лазер на центральной грани.
                
        return 0 #Возвращаем 0, если ни одно из условий не выполнилось.

    #Проверяет, что лазерная точка находится в пределах Player.
    @staticmethod
    def check_laser_position_to_player(target_entity: TargetParams, center: Tuple[int, int]) -> bool:
        if center is None or target_entity.radii is None:
            return False

        distance: float = np.sqrt((target_entity.laser[0] - center[0]) ** 2 + (target_entity.laser[1] - center[1]) ** 2)

        if distance > target_entity.radii[-1]: #Проверка на максимальный радиус.
            return False

        return True