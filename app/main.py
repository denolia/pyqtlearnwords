import sys
from PyQt5.QtWidgets import QApplication

from app.db.db import connect_db
from app.ui.mainwindow import MainWindow
from app.ui.manager import Manager
from app.utils.log_conf import configure_logging

if __name__ == '__main__':
    configure_logging()
    connect_db()
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    manager = Manager(mainwindow)
    manager.setup()
    mainwindow.show()
    app.exec_()
