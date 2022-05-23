import json
import time

from flask import Blueprint, request
from flask_cors import cross_origin
from business.sensor import Sensor
from jobs.datapost import SEN_DATA

sensor_bp = Blueprint('sensor_bp',__name__)


#Sample
@sensor_bp.route('/sample', methods= ['POST'])
@cross_origin()
def sample():
    ajax_data = ""
    if request.method == "POST":
        data = request.form
        sen_type = data.get('sen_type')
        from_date = data.get('from_date')
        to_date = data.get('to_date')
        sensor = Sensor()
        if sen_type is not None and sen_type != "":
            ajax_data = sensor.getSen_ChartData(sen_type, from_date, to_date)

    return ajax_data

@sensor_bp.route('/save_data', methods= ['GET'])
@cross_origin()
def save_data():
    if request.method == "GET":
        data = request.args
        sen_data = data.get('data')
        try:
            if len(sen_data) > 0:
                print(sen_data)
                data = json.loads(sen_data)
                print(data)
                localtime = time.localtime()
                data_date = time.strftime("%Y%m%d", localtime)
                sen_data = SEN_DATA(data_date, data["time"],
                                    data["sen1"], data["sen2"], data["sen3"], data["sen4"], data["sen5"], data["sen6"],
                                    data["set1"], data["set2"], data["set3"], data["set4"], data["set5"], data["set6"],
                                    data["set7"])
                sen_data.insert_db()
        except Exception as e:
            print("ERROR:")

    return "OK"