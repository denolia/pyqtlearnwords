from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from app.ui.table.tablemodel import TableModel


class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        self.model = TableModel()

    def update_table(self):
        table = self.model.get_data()
        self.setRowCount(len(table))

        headers = self.model.get_headers()
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)

        for n_row, row in enumerate(table):
            for n_column, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                item.setData(Qt.ToolTipRole, headers[n_column])
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.setItem(n_row, n_column, item)

        self.resizeColumnsToContents()
