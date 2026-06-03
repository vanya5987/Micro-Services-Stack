from dataclasses import dataclass
from typing import Callable
from PyQt5.QtWidgets import QWidget


@dataclass
class LicenseWindowParams:
    checkLicense: object = None
    on_accept: Callable[[], None] = None