import sys

import logging
from PyQt5.QtWidgets import QMainWindow, QApplication

from app.db.db import connect_db
from app.ui.manager import Manager
from app.ui.ui_mainwindow import Ui_MainWindow
from app.utils.log_conf import configure_logging

log = logging.getLogger(__name__)

configure_logging()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    connect_db()
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    manager = Manager(mainwindow)
    manager.setup()
    mainwindow.show()
    app.exec_()
