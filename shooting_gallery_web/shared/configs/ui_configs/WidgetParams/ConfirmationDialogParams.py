from dataclasses import dataclass
from typing import Callable
from PyQt5.QtWidgets import QWidget

from app.services.update_uploader.UpdateChecker import UpdateChecker

from typing import Union


@dataclass
class BaseWidgetParams:
    parent: QWidget


@dataclass
class ConfirmationDialogParams(BaseWidgetParams):
    message: str
    isError: bool
    on_accept: Callable[[], None] = None
    on_reject: Callable[[], None] = None
    on_shooting: bool = False
    showLoading: bool = False
    update_checker: Union[UpdateChecker, None] = None
    windowHeader: str = None
