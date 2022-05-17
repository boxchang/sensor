from bases.common_lib import Cursor2Dict
from bases.database import database
import json

class Sensor(object):
    def getSen_ChartData(self, sen_type, from_date, to_date):
        value_results = []
        label_results = []
        db = database()
        sql = """SELECT * FROM (
                    select concat(data_date,' ',data_time) data_time,{sen_type} from demo 
                    WHERE data_date BETWEEN STR_TO_DATE('{from_date}', '%Y/%m/%d') 
                    AND STR_TO_DATE('{to_date}', '%Y/%m/%d')
                    ORDER BY data_date DESC,data_time DESC 
                    ) A ORDER BY data_time"""
        sql = sql.format(from_date=from_date, to_date=to_date, sen_type=sen_type)
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