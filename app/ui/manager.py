from app.ui.dbtableslist.dbtablelistmodel import DBTablesModel
from app.ui.table.tablewidget import TableWidget


class Manager:
    def __init__(self, mainwindow: 'MainWindow'):
        self.mainwindow = mainwindow
        self.table_widget = TableWidget()

        list_view = self.mainwindow.listView
        list_view.setModel(DBTablesModel(list_view))

        self.mainwindow.splitter.setStretchFactor(0, 1)
        self.mainwindow.splitter.setStretchFactor(1, 2)

        self.mainwindow.verticalLayout.addWidget(self.table_widget)

    def setup(self):
        self.table_widget.update_table()

