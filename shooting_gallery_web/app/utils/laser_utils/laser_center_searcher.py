from typing import Tuple, Union
import cv2
import numpy as np

class PointSearcher:
    @staticmethod
    def GetCenter(contour: np.ndarray) -> Union[Tuple[int, int], None]:
        if len(contour) > 0:
            M = cv2.moments(contour)
                
            #Инициализируем переменные по умолчанию.
            cX: Union[int, None] = None
            cY: Union[int, None] = None
                
            if M["m00"] != 0:  #Проверяем, чтобы избежать деления на ноль.
                cX = int(M["m10"] / M["m00"])  #Получаем координату X центра.
                cY = int(M["m01"] / M["m00"])  #Получаем координату Y центра.
                
            if cX is not None and cY is not None:
                return (cX, cY)
            
        return None #Если contour пуст или M["m00"] == 0, возвращаем None.