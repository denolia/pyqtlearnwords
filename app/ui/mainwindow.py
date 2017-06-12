import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

from app.ui.mainwindow_ui import Ui_MainWindow
from app.ui.manager import Manager
from app.ui.table.tabledata import TableData


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    table_data = TableData()
    manager = Manager(mainwindow, table_data)
    manager.setup()
    mainwindow.show()
    app.exec_()