import cv2
import numpy as np


class FrameBrightnessCalculator:
    def __init__(self):
        self.history_brightness: float = None

    def mean_brightness_between(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        v = hsv[:, :, 2]
        mean = np.mean(v)

        if self.history_brightness is None:
            self.history_brightness = mean

            return self.history_brightness

        return (self.history_brightness + mean) / 2
