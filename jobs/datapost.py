import requests
import time
import sys
sys.path.append("..")
from bases.database import database
from bases.settings import SLEEP_TIME, CREATE_TABLE_SQL


class SEN_DATA(object):
    data_date = ""
    data_time = ""
    sen1 = ""
    sen2 = ""
    sen3 = ""
    sen4 = ""
    sen5 = ""
    sen6 = ""
    set1 = ""
    set2 = ""
    set3 = ""
    set4 = ""
    set5 = ""
    set6 = ""
    set7 = ""
    cur = None
    conn = None

    def __init__(self, data_date, data_time, sen1, sen2, sen3, sen4, sen5, sen6,
                 set1, set2, set3, set4, set5, set6, set7):
         # 建立cursor對資料庫做操作
        self.data_date = data_date
        self.data_time = data_time
        self.sen1 = sen1
        self.sen2 = sen2
        self.sen3 = sen3
        self.sen4 = sen4
        self.sen5 = sen5
        self.sen6 = sen6
        self.set1 = set1
        self.set2 = set2
        self.set3 = set3
        self.set4 = set4
        self.set5 = set5
        self.set6 = set6
        self.set7 = set7

    def insert_db(self):
        sql = """insert into demo(data_date,data_time,sen1,sen2,sen3,sen4,sen5,sen6,set1,set2,set3,set4,set5,set6,set7) 
                 values('{data_date}','{data_time}',{sen1},{sen2},{sen3},{sen4},{sen5},{sen6},{set1},{set2},{set3},{set4},
                        {set5},{set6},{set7})"""
        sql = sql.format(data_date=self.data_date, data_time=self.data_time, sen1=self.sen1, sen2=self.sen2,
                         sen3=self.sen3, sen4=self.sen4, sen5=self.sen5, sen6=self.sen6, set1=self.set1,
                         set2=self.set2, set3=self.set3, set4=self.set4, set5=self.set5, set6=self.set6,
                         set7=self.set7)
        print(sql)
        db = database()
        db.execute_sql(sql)
        db.close_connection()

def create_table():
    db = database()
    db.execute_sql(CREATE_TABLE_SQL)
    db.close_connection()

def begin():
    create_table()

    url = "http://125.229.85.125/datapost.json"
    resp = requests.get(url=url)
    data = resp.json()
    print(data)
    print(data["time"])
    localtime = time.localtime()
    data_date = time.strftime("%Y%m%d", localtime)
    sen_data = SEN_DATA(data_date, data["time"],
                   data["sen1"], data["sen2"], data["sen3"], data["sen4"], data["sen5"], data["sen6"],
                   data["set1"], data["set2"], data["set3"], data["set4"], data["set5"], data["set6"], data["set7"])
    sen_data.insert_db()



if __name__ == '__main__':
    begin()

