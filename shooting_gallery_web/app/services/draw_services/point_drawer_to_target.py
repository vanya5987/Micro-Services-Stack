from shared.configs.docx_configs.pdf_const_config import PdfConstConfig
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPixmap, QPen, QFont
from PyQt5.QtCore import Qt
from typing import *


class PointDrawerToTarget(QWidget):
    def __init__(self):
        super().__init__()
        self.pointColor = QColor(255, 0, 0)
        self.textColor = QColor(0, 0, 255)
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(10)

    def DrawPoint(self, painter: QPainter, laserPoint: List[int], bulletNumber: int,
                  pointDiameter: int, contourThickness: float):
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(self.pointColor, contourThickness))
        painter.setBrush(Qt.NoBrush)
        x = laserPoint[0] - pointDiameter // 2
        y = laserPoint[1] - pointDiameter // 2
        painter.drawEllipse(x, y, pointDiameter, pointDiameter)

        # #Рисуем номер пули.
        # painter.setPen(self.textColor)
        # painter.setFont(self.font)
        # text_x = laserPoint[0] - 5
        # text_y = laserPoint[1] - pointDiameter - 2
        # painter.drawText(text_x, text_y, str(bulletNumber))

    def GetTargetWithPointLowRes(self, laserPoint: List[int], image: QPixmap, bulletNumber: int) -> QPixmap:
        scaled_pixmap = image.scaled(206, 274, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        painter = QPainter(scaled_pixmap)

        self.DrawPoint(painter, laserPoint, bulletNumber, pointDiameter=8, contourThickness=1.5)
        painter.end()

        return scaled_pixmap

    def GetTargetWithPointHighRes(self, laserPoint: List[int], image: QPixmap, bulletNumber: int) -> QPixmap:
        painter = QPainter(image)
        laser = [int(laserPoint[0] * (PdfConstConfig.HIGH_RESOLUTION_SCALE_COEF / 2)),
                 int(laserPoint[1] * (PdfConstConfig.HIGH_RESOLUTION_SCALE_COEF / 2))]

        self.DrawPoint(painter, laser, bulletNumber, pointDiameter=15, contourThickness=5)
        painter.end()

        return image
