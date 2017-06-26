import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from app.ui.manager import Manager
from app.ui.ui_mainwindow import Ui_MainWindow
from app.utils import log_conf

log = log_conf.get_logger(__name__)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    manager = Manager(mainwindow)
    manager.setup()
    mainwindow.show()
    app.exec_()
