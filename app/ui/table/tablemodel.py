class TableModel:

    def get_data(self):

        return [[l + k for l in range(5)] for k in range(5)]

if __name__ == '__main__':
    table = TableModel()
    print(table.get_data())