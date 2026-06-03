from app.api.database_api.DataStorageGetter import DataStorageGetter
from app.api.database_api.ShootingRepository import ShootingRepository

from shared.pathings.path_config import PathConfig
from app.utils.docx_utils.pdf_reader import PdfReader
from app.utils.docx_utils.explore_opener import ExplorerOpener

from pathlib import Path
import os


class ReportOpener:
    def __init__(self):
        dataStorageGetter = DataStorageGetter()
        self.shootingRepository = ShootingRepository(dataStorageGetter)
        self.pdfReader = PdfReader()
        self.explorerOpener = ExplorerOpener()

    def GetPdfFilePath(self, shootingID: int):
        fileName: str = self.shootingRepository.GetPdfName(shootingID)
        filePath: str = os.path.join(PathConfig.REPORT_DIRECTORY_PATH, fileName)

        return filePath

    def OpenPdfFile(self, shootingID: int):
        path: str = self.GetPdfFilePath(shootingID)
        self.explorerOpener.open_pdf_folder(path)
