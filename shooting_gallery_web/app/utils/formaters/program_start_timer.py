from typing import *
import time
import datetime
from threading import Thread

class ProgramStartTimer:
    def __init__(self):
        self.startShootingTime = time.time()
        self.startShootingRunning = False

        self.countdownRunning = False
        self.remainingTimeInSecond = 0
        self.countdownFinished = False

    def StartCountdown(self, minutes: int = 0, seconds: int = 0) -> None:
        if self.countdownRunning:
            return

        totalSeconds = minutes * 60 + seconds
        self.remainingTimeInSecond = totalSeconds
        self.countdownFinished = False
        self.countdownRunning = True

        def countdown_loop():
            startTime = time.time()
            endTime = startTime + totalSeconds

            while self.countdownRunning and time.time() < endTime:
                self.remainingTimeInSecond = max(0, endTime - time.time())
                time.sleep(0.1)

            self.countdownRunning = False
            if time.time() >= endTime:
                self.countdownFinished = True

        Thread(target=countdown_loop, daemon=True).start()

    def GetCountdownStatus(self) -> Tuple[bool, Optional[int], Optional[int]]:
        minutes = int((self.remainingTimeInSecond % 3600) // 60)
        seconds = int(self.remainingTimeInSecond % 60)

        return (self.countdownFinished, minutes if minutes > 0 else 0,
            seconds if seconds > 0 else 0)

    def RunStartShootTimer(self):
        while self.startShootingRunning:
            time.sleep(1)

    def StartShootTimer(self):
        if not self.startShootingRunning:
            self.startShootingRunning = True
            Thread(target=self.RunStartShootTimer, daemon=True).start()

    def GetElapsedTime(self) -> Tuple[int, int]:
        elapsed = time.time() - self.startShootingTime

        return self.GetMinutesAndSecond(elapsed)

    def GetMinutesAndSecond(self, elapsed: float) -> Tuple[int, int]:
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)

        return minutes, seconds

    @staticmethod
    def GetCurrentTime() -> int:
        return int(time.time()) #Текущее время в секундах.

    @staticmethod
    def GetFormatCurrentTime()-> str:
        return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))