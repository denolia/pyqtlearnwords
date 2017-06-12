from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem


class Manager:
    def __init__(self, mainwindow: 'MainWindow', table: 'TableData'):
        self.mainwindow = mainwindow
        self.table = table

    def setup(self):
        self.mainwindow.tableWidget.clear()
        self.updateTable()

    def updateTable(self):
        table = self.table.get_data()
        self.mainwindow.tableWidget.setRowCount(len(table))
        self.mainwindow.tableWidget.setColumnCount(len(table))
        self.mainwindow.tableWidget.setHorizontalHeaderLabels(["Title", "Year", "Mins", "Acquired", "Notes"])

        for n_row, row in enumerate(table):
            for n_column, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                item.setData(Qt.ToolTipRole, 'hi there')
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.mainwindow.tableWidget.setItem(n_row, n_column, item)

        self.mainwindow.tableWidget.resizeColumnsToContents()