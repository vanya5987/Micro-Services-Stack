from PyQt5.QtWidgets import QLabel
from dataclasses import dataclass

@dataclass
class CreateShooterEntity:
    name_label: QLabel
    target_label: QLabel
    score_label: QLabel
    target_hint: QLabel