from shared.configs.core_configs.exercise_config import ExerciseContainer

from datetime import datetime
from typing import *

class StringFormat:
    #Возвращает формат времени.
    @staticmethod
    def create_time_format(minutes: int, seconds: int) -> str: #%H:%M:%S - формат вывода.
        minutes: str = StringFormat.time_formatter(minutes)
        seconds: str = StringFormat.time_formatter(seconds)

        return f"{minutes}:{seconds}"
    
    #Возвращает формат времени даты стрельб.
    @staticmethod
    def create_shooting_date() -> str:
        now = datetime.now()

        years = now.year
        months = now.month
        days = now.day
        hours = now.hour
        minutes = now.minute

        years = StringFormat.time_formatter(years)
        months = StringFormat.time_formatter(months)
        days = StringFormat.time_formatter(days)
        hours = StringFormat.time_formatter(hours)
        minutes = StringFormat.time_formatter(minutes)

        return f"{years}-{months}-{days} {hours}:{minutes}"

    #Парсит строковое время в INT.
    @staticmethod
    def parse_time_format_to_int(shootingTime: str) -> Union[Tuple[List[int], bool], None]:
        if shootingTime == ExerciseContainer.INVALID_TIME_FORMAT:
            return [0, 0], False

        parts: List[str] = shootingTime.split(":")

        if len(parts) == 2:
            return [int(parts[0]), int(parts[1])], True

    #Приводит время в строковой формат.
    @staticmethod
    def time_formatter(time: int) -> str:
        temp: str = str(time)

        if -1 < time < 10:
            temp = "0" + temp

        return temp