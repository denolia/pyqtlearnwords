import logging
from PyQt5.QtWidgets import QMainWindow

from app.ui.ui_mainwindow import Ui_MainWindow

log = logging.getLogger(__name__)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
