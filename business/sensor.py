from bases.common_lib import Cursor2Dict
from bases.database import database
import json

class Sensor(object):


    def getSen1_ChartData(self):
        value_results = []
        label_results = []
        db = database()
        sql = """select data_time,sen1 from demo ORDER BY data_date,data_time DESC LIMIT 10"""
        print(sql)
        cursor = db.execute_select_sql(sql)
        for row in cursor.fetchall():
            label_results.append(row[0])
            value_results.append(row[1])
        #results = Cursor2Dict(cursor)
        results = {"LABELS": label_results, "VALUES": value_results}
        ajax_data = json.dumps(results)
        return ajax_data



# sen = Sensor()
# xx = sen.getSen1_ChartData()
# print(xx)