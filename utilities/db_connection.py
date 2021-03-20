import sqlite3
import constants.common_constants as constatnts


class DbInstance:
    conn = None

    def __init__(self):
        self.conn = sqlite3.connect(constatnts.DB_PATH)

    def get_connection(self):
        return self.conn
