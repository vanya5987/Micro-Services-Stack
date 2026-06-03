from app.services.docs_services.missing_pdf_generator import MissingPdfGenerator
from PyQt5.QtWidgets import QApplication
from root_path import RootDirectoryPath

import sys, os


class TestMissingPdfGenerator:
    @staticmethod
    def generate_test_pdf(shooting_id: int):
        path: str = os.path.join(RootDirectoryPath.GetRootPath(), "tests", "test.pdf")

        app = QApplication(sys.argv)
        MissingPdfGenerator(shooting_id, is_override_path=True, override_path=path)


TestMissingPdfGenerator.generate_test_pdf(156)
