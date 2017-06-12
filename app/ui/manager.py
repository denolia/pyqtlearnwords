


class Manager:
    def __init__(self, mainwindow: 'MainWindow'):
        self.mainwindow = mainwindow

    def setup(self):

        self.mainwindow.tableWidget.clear()
        self.updateTable()

    def updateTable(self):
        table = []
        self.mainwindow.tableWidget.setRowCount(2)
        self.mainwindow.tableWidget.setColumnCount(5)