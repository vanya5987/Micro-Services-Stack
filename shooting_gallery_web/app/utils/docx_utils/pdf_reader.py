from typing import *
import os
import subprocess

class PdfReader:
    @staticmethod
    def read_pdf(pdfPath: str, is_ubuntu_system: bool):
        if not os.path.exists(pdfPath):
            raise Exception("PDF file not found")

        pdfReaders: List[str] = [
            "okular", "evince", "atril", "qpdfview", "xdg-open",
            "kde-menu-pdf-manager", "pdfarranger", "firefox",
            "chromium", "google-chrome"
        ]

        specialReaders: Dict[str, List[str]] = {
            "cups-pdf": ["lpr", "-P", "PDF", pdfPath],
            "pdfgrep": ["pdfgrep", "-r", ".", pdfPath]
        }

        if is_ubuntu_system:
            for reader in pdfReaders:
                try:
                    if reader in specialReaders:
                        subprocess.run(specialReaders[reader], check=True)
                    else:
                        subprocess.run(["sudo", "-u", os.environ['USER'], "bash", "-c",
                                        f"ulimit -l unlimited && {reader} '{pdfPath}'"], check=True)
                    break
                except (subprocess.CalledProcessError, FileNotFoundError):
                    continue
            else:
                print("PDF - reader is not contains in this device!")
        else:
            for reader in pdfReaders:
                try:
                    if reader in specialReaders:
                        subprocess.run(specialReaders[reader], check=True)
                    else:
                        subprocess.run([reader, pdfPath], check=True)
                    break
                except (subprocess.CalledProcessError, FileNotFoundError):
                    continue
            else:
                print("PDF reader is not available on this device!")