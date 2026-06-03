from shared.pathings.path_config import PathConfig
from shared.configs.core_configs.rating_config import RatingConfig
from app.services.docs_services.result_rating_calculator import ResultRatingCalculator
from PyQt5.QtGui import QPixmap

from datetime import datetime
from typing import *
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class PdfConfig:
    def __init__(self, target: QPixmap, playerSurname: str, exercsieName: str, groupName: str, currentPoints: List[int],
                 shootTimes: List[str], playerID: int, playerName: str):
        pdfmetrics.registerFont(TTFont('Inter', os.path.join(PathConfig.FONT_PATH, "Inter_18pt-Regular.ttf")))

        self.tableHeaders: List[str] = ["Выстрел", "Очко", "Время"]
        self.shootingInfo: List[str] = ["Стрелок", "Группа", "Отстрелял патрон", "Всего очков", "Времени потрачено",
                                        "Оценка"]
        self.pageHeaders: List[str] = ["© Интерактивный лазерный тир", "Сгенерировано"]
        self.directoryName: str = PathConfig.REPORT_DIRECTORY_PATH
        self.standartFont: str = "Inter"
        self.playerSurname: str = playerSurname
        self.playerName: str = playerName
        self.rating: str = ResultRatingCalculator(RatingConfig()).get_rating_by_score(exercsieName, sum(currentPoints))

        self.currentPoints: List[int] = currentPoints
        self.shootTimes: List[str] = shootTimes

        self.target: QPixmap = target
        self.exercsieName: str = exercsieName
        self.groupName: str = groupName

        self.shootingDateForPdfName: str = f"{datetime.now().strftime('%d.%m.%Y')}_{datetime.now().strftime('%M%S')}"
