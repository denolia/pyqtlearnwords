from PyQt5.QtGui import QStandardItemModel, QStandardItem


class DBTablesModel(QStandardItemModel):

    def __init__(self, list_view=None):
        super().__init__(list_view)
        dbtables = ['one', 'two', 'three']

        for dbtable in dbtables:
            item = QStandardItem(dbtable)
            self.appendRow(item)

    def get_data(self):
        table = ['one', 'two', 'three']
        return table

