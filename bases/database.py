from sqlite3 import Error
import MySQLdb

from bases.settings import *


class database:
    conn = None
    cur = None

    def execute_sql(self, sql):
        self.conn = self.create_connection()
        self.cur = self.conn.cursor()
        self.cur.execute(sql)
        self.conn.commit()

    def execute_select_sql(self, sql):
        self.conn = self.create_connection()
        cur = self.conn.cursor()
        cur.execute(sql)
        return cur

    def close_connection(self):
        self.conn.close()

    def create_connection(self):
        try:
            if self.conn is None:
                conn = MySQLdb.connect(host=DB_HOST,  # your host, usually localhost
                                       user=DB_USER,  # your username
                                       passwd=DB_PASSWORD,  # your password
                                       db=DB_DATABASE,
                                       port=DB_PORT, use_unicode=True, charset="utf8")  # name of the data base

            return conn
        except Error as e:
            print(e)

        return None
