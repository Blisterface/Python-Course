import sqlite3 as db

class DatabaseConnection:
    """
    manages the connection and closing of the connection to the database
    """
    def __init__(self,host):
        self.host = host
        self.connection = None


    def __enter__(self):
        self.connection = db.connect(self.host)
        return self.connection


    def __exit__(self, exc_type, exc_value, trace):
        if exc_type or exc_value or trace:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()

