import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "12345678",
            database = "bookstore"
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params):
        self.cursor.execute(query, params)
        self.connection.commit()