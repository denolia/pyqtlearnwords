from app.db.db import get_words_by_user, get_headers


class TableModel:

    def get_data(self):
        table = get_words_by_user("julia_vikulina")
        return table

    def get_headers(self):
        raw_headers = get_headers()
        headers = [name[0] for name in raw_headers]

        return headers


if __name__ == '__main__':
    table = TableModel()
    print(table.get_data())
