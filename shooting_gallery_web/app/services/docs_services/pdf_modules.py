from app.services.docs_services.pdf_modules_styles import PdfModulesStyles
from shared.configs.core_configs.pdf_config import PdfConfig

from reportlab.platypus import Paragraph, Frame, Table, Image
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import datetime


class PdfModules:
    def __init__(self, pdfConfig: PdfConfig):
        self.pdfConfig: PdfConfig = pdfConfig
        self.pdfModulesStyles: PdfModulesStyles = PdfModulesStyles(self.pdfConfig)
        self.libStyles = self.pdfModulesStyles.ApplyPdfStyles()

        self.standartFont: str = pdfConfig.standartFont

    # Добавляет хэдер в отчет.
    def AddTitleToReport(self, canvas: canvas.Canvas, width: float, height: float, exerciseName: str):
        title = Paragraph(f"{exerciseName} {self.pdfConfig.shootingDateForPdfName[:10]}", self.libStyles['Title'])
        titleFrame = Frame(0, height - 1.5 * inch, width, 1.5 * inch)
        titleFrame.addFromList([title], canvas)

    # Добавляет изображение в отчет.
    def AddImageToReport(self, canvas: canvas.Canvas, imagePath: str, x: float, y: float,
                         width: float, height: float):
        image = Image(imagePath)

        if width is not None:
            image.drawWidth = (width * inch)
        if height is not None:
            image.drawHeight = (height * inch) * 1.5

        # Рисуем изображение на canvas.
        image.drawOn(canvas, (x * inch) / 1.67,  # Позиционирование картинки по X
                     (y * inch) / 10.0)  # Позиционирование картинки по Y

    # Добавляет информацию о стрелке в отчет.
    def AddShooterInfoToReport(self, canvas: canvas.Canvas, width: float, height: float):
        shooter_info = [
            Paragraph(
                f"<b>{self.pdfConfig.shootingInfo[0]}:</b> {self.pdfConfig.playerSurname} {self.pdfConfig.playerName}",
                self.libStyles['ShooterNormalR']),
            Paragraph(f"<b>{self.pdfConfig.shootingInfo[1]}:</b> {self.pdfConfig.groupName}",
                      self.libStyles['ShooterNormalR']),
            Paragraph(" ", self.libStyles['ShooterNormalC']),  # Пустая строчка.
            Paragraph(f"<b>{self.pdfConfig.shootingInfo[2]}:</b> {len(self.pdfConfig.currentPoints)}",
                      self.libStyles['ShooterNormalC']),
            Paragraph(f"<b>{self.pdfConfig.shootingInfo[3]}:</b> {sum(self.pdfConfig.currentPoints)}",
                      self.libStyles['ShooterNormalC']),
            Paragraph(f"<b>{self.pdfConfig.shootingInfo[4]}:</b> {max(self.pdfConfig.shootTimes)}",
                      self.libStyles['ShooterNormalC']),
            Paragraph(f"<b>{self.pdfConfig.shootingInfo[5]}:</b> {self.pdfConfig.rating}",
                      self.libStyles['ShooterNormalC']),
            Paragraph(" ", self.libStyles['ShooterNormalC'])  # Пустая строчка.
        ]

        shooterFrame = Frame(1 * inch, height - 4 * inch, width - 2 * inch, 3 * inch)
        shooterFrame.addFromList(shooter_info, canvas)

    # Добавляет таблицу стрельбы с временем выстрелов в отчет.
    def AddShotsTableToReport(self):
        # Создаем заголовки таблицы с новой колонкой.
        tableData = [[self.pdfConfig.tableHeaders[0], self.pdfConfig.tableHeaders[1],
                      self.pdfConfig.tableHeaders[2]]]

        for shootID, (shootScore, shootTime) in enumerate(zip(self.pdfConfig.currentPoints, self.pdfConfig.shootTimes),
                                                          start=1):
            tableData.append([str(shootID), str(shootScore), shootTime])

        # Создаем таблицу с тремя колонками.
        shotsTable = Table(tableData, colWidths=[1 * inch, 1 * inch, 1.5 * inch])
        self.pdfModulesStyles.ApplyTableStyle(shotsTable)

        return shotsTable

    # Добавляет футер в отчет.
    def AddPdfFooterToReport(self, canvas: canvas.Canvas, width: float):
        canvas.setFont(self.standartFont, 8)
        canvas.setFillColor(colors.gray)
        canvas.drawCentredString(width / 2, 0.4 * inch, self.pdfConfig.pageHeaders[0])
        canvas.drawCentredString(width / 2, 0.25 * inch,
                                 f"{self.pdfConfig.pageHeaders[1]}: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
