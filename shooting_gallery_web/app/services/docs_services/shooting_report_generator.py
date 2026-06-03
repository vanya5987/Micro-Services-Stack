from app.services.docs_services.pdf_modules_styles import PdfModulesStyles
from shared.configs.core_configs.pdf_config import PdfConfig
from app.services.docs_services.pdf_modules import PdfModules

from app.api.database_api.DataStorageGetter import DataStorageGetter
from app.api.database_api.ShootingRepository import ShootingRepository

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Frame, Table
from reportlab.lib.units import inch
import os
from PyQt5.QtGui import QPixmap
import tempfile

class ShootingReportGenerator:
    def __init__(self, pdfConfig: PdfConfig):
        self.pdfConfig = pdfConfig
        self.pdfModulesStyles = PdfModulesStyles(self.pdfConfig)
        self.pdfModules = PdfModules(pdfConfig)
        self.directoryOutputName: str = self.pdfConfig.directoryName

        self.dataStorageGetter: DataStorageGetter = DataStorageGetter()

        os.makedirs(self.directoryOutputName, exist_ok=True)
        self.libStyles = self.pdfModulesStyles.ApplyPdfStyles()

    def GenerateReport(self, pdfIsMissing: bool = False, shootingID: int = None, is_override_path: bool = False,
                       override_path: str = "") -> str:
        image_scale: int = 3

        filepath: str = override_path if is_override_path else self.GetReportFilepath(pdfIsMissing, shootingID)

        pdfCanvas = canvas.Canvas(filepath, pagesize=letter)
        width, height = letter

        self.pdfModules.AddTitleToReport(pdfCanvas, width, height, self.pdfConfig.exercsieName)
        self.pdfModules.AddShooterInfoToReport(pdfCanvas, width, height)

        if self.pdfConfig.target and isinstance(self.pdfConfig.target, QPixmap):
            image: QPixmap = self.pdfConfig.target.toImage()
            temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
            temp_path = temp_file.name
            temp_file.close()
            image.save(temp_path, "PNG")

            self.pdfModules.AddImageToReport(
                pdfCanvas, temp_path,
                x=width / inch - (2.8 + image_scale),
                y=height / inch - (4.5 + image_scale),
                width=(2.5 + image_scale),
                height=(2 + image_scale)
            )
            os.unlink(temp_path)

        pdfCanvas.showPage()
        width, height = letter

        col_widths = [0.8 * inch, 0.8 * inch, 1.4 * inch]
        table_width = sum(col_widths)
        left_margin = (width - table_width) / 2.0
        top_margin = 1.5 * inch
        bottom_margin = 0.8 * inch

        table_data = [
            [self.pdfConfig.tableHeaders[0], self.pdfConfig.tableHeaders[1], self.pdfConfig.tableHeaders[2]]
        ]
        for i, (shot, time) in enumerate(zip(self.pdfConfig.currentPoints, self.pdfConfig.shootTimes), start=1):
            table_data.append([str(i), str(shot), time])

        shots_table = Table(table_data, colWidths=col_widths)
        self.pdfModulesStyles.ApplyTableStyle(shots_table)

        _, table_height = shots_table.wrapOn(pdfCanvas, width, height - top_margin - bottom_margin)
        y_pos = height - top_margin - table_height
        shots_table.drawOn(pdfCanvas, left_margin, y_pos)

        self.pdfModules.AddPdfFooterToReport(pdfCanvas, width)

        pdfCanvas.save()
        return filepath

    # Определяет путь к файлу.
    def GetReportFilepath(self, pdfIsMissing: bool, shootingID: int):
        if not pdfIsMissing:
            filename = f"{self.pdfConfig.playerSurname}_{self.pdfConfig.playerName}_shooting_{self.pdfConfig.shootingDateForPdfName}.pdf"
        else:
            shootingRepository: ShootingRepository = ShootingRepository(self.dataStorageGetter)
            shootings = shootingRepository.GetShootingByID(shootingID)
            filename = shootings[6]

        return os.path.join(self.directoryOutputName, filename)
