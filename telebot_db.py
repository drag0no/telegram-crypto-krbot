import sqlite3


class TelebotDB:

    def __init__(self):
        self.db_name = 'database.sqlite'
        self.create_table()

    def create_table(self):
        connect = sqlite3.connect(self.db_name)
        cursor = connect.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users
                (
                    chat_id INTEGER PRIMARY KEY UNIQUE
                )
            ''')
        connect.commit()
        cursor.close()

    def insert_chatid(self, chat_id):
        connect = sqlite3.connect(self.db_name)
        cursor = connect.cursor()
        cursor.execute('INSERT OR IGNORE INTO users (chat_id) VALUES (:chat_id)', {'chat_id': chat_id})
        connect.commit()
        cursor.close()
        connect.close()

    def delete_chatid(self, chat_id):
        connect = sqlite3.connect(self.db_name)
        cursor = connect.cursor()
        cursor.execute('DELETE FROM users WHERE chat_id = :chat_id', {'chat_id': chat_id})
        connect.commit()
        cursor.close()
        connect.close()

    def get_chatids(self):
        connect = sqlite3.connect(self.db_name)
        cursor = connect.cursor()
        chat_ids = cursor.execute('SELECT chat_id FROM users')
        chat_ids = [x[0] for x in chat_ids]
        connect.commit()
        cursor.close()
        connect.close()
        return chat_ids

# if __name__ == '__main__':
#     chatid_list = ['102668196', '202668197', '302668196']
#     db = TelebotDB()
#     db.create_table()
#     for chat_id in chatid_list:
#         db.insert_chatid(chat_id)
#     print(db.get_chatids())
