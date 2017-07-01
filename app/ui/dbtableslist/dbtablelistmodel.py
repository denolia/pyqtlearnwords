from PyQt5.QtGui import QStandardItemModel, QStandardItem

from app.db.db import get_tables_list


class DBTablesModel(QStandardItemModel):

    def __init__(self, list_view=None):
        super().__init__(list_view)

        dbtables_tuples = get_tables_list()
        dbtables = [line[0] for line in dbtables_tuples]
        for dbtable in dbtables:
            item = QStandardItem(dbtable)
            self.appendRow(item)

    def get_data(self):
        table = ['one', 'two', 'three']
        return table

