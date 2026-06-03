from app.entitys.shooting_mods import ShootingMods

import numpy as np
import cv2

class MatsCalculator:
    @staticmethod
    async def create_target_matrix_thread(frame: np.ndarray):
        return await MatsCalculator.CreateTargetFilter(frame)

    @staticmethod
    async def create_laser_matrix_thread(frame: np.ndarray, laserBrightest: int):
        return await MatsCalculator.CreateRedMask(frame, laserBrightest)

    #Создает маску для определения цели.
    @staticmethod
    async def CreateTargetFilter(frame: np.ndarray) -> np.ndarray:
        kernel = np.ones((4, 4), np.uint8)
        thresh_cleaned = cv2.morphologyEx(cv2.adaptiveThreshold(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY_INV, 21, 5), cv2.MORPH_OPEN, kernel) #Удаление шума.
        thresh_cleaned = cv2.morphologyEx(thresh_cleaned, cv2.MORPH_CLOSE, kernel) #Заполнение дыр.

        return thresh_cleaned

    #Адаптивное определение порога на основе статистики кадра
    @staticmethod
    async def CreateRedMask(frame: np.ndarray, laserBrightest: int) -> np.ndarray:
        r_channel = frame[:, :, 2]

        #Используем процентиль вместо фиксированного порога.
        threshold_value = np.percentile(r_channel, 90) #95-й процентиль яркости.
        threshold_value = max(threshold_value, laserBrightest) #Но не менее 200.

        _, brightness_mask = cv2.threshold(r_channel, threshold_value, 255, cv2.THRESH_BINARY)

        r = r_channel.astype(np.float32)
        g = np.maximum(frame[:, :, 1].astype(np.float32), 1)
        b = np.maximum(frame[:, :, 0].astype(np.float32), 1)

        red_dominance = (r > g * 1.05) & (r > b * 1.05)

        #Комбинируем маски.
        red_mask = np.uint8(brightness_mask & red_dominance) * 255

        return red_mask