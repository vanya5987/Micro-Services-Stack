from shared.configs.core_configs.pdf_config import PdfConfig

# Библиотеки.
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import TableStyle, Table
from reportlab.lib import colors


# Библиотеки.

class PdfModulesStyles:
    def __init__(self, pdfConfig: PdfConfig):
        self.pdfConfig: PdfConfig = pdfConfig

    # Устанавливает стиль для pdf - файла.
    def ApplyPdfStyles(self):
        libStyles = getSampleStyleSheet()
        spaceAfter: int = 8  # Отступы между блоками.

        libStyles['Title'].fontSize = 24
        libStyles['Title'].leading = 28
        libStyles['Title'].alignment = 1
        libStyles['Title'].spaceAfter = 20
        libStyles['Title'].fontName = self.pdfConfig.standartFont

        libStyles.add(ParagraphStyle(name='ShooterHeader', parent=libStyles['BodyText'], fontSize=12, leading=14,
                                     fontName=self.pdfConfig.standartFont))
        libStyles.add(ParagraphStyle(name='ShooterNormalR', parent=libStyles['BodyText'], fontSize=12, leading=14,
                                     alignment=1, spaceAfter=spaceAfter,
                                     fontName=self.pdfConfig.standartFont))  # Позиционировнаие имени и ID.
        libStyles.add(ParagraphStyle(name='ShooterNormalC', parent=libStyles['BodyText'], fontSize=12, leading=14,
                                     alignment=1, spaceAfter=spaceAfter,
                                     fontName=self.pdfConfig.standartFont))  # Позиционирование слева.

        return libStyles

    # Применяет стиль к таблице.
    def ApplyTableStyle(self, shootingTable: Table):
        tableStyle = TableStyle([
            # Стили для заголовка.
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.darkblue),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), self.pdfConfig.standartFont),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),

            # Стили для тела таблицы.
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])
        shootingTable.setStyle(tableStyle)
