from flask import Blueprint, request
from flask_cors import cross_origin
from business.sensor import Sensor

sensor_bp = Blueprint('sensor_bp',__name__)


#Sample
@sensor_bp.route('/sample', methods= ['POST'])
@cross_origin()
def sample():
    ajax_data = ""
    if request.method == "POST":
        data = request.form
        data_type = data.get('type')
        sensor = Sensor()
        if data_type == "sen1":
            ajax_data = sensor.getSen1_ChartData()
        elif data_type == "sen2":
            ajax_data = sensor.getSen2_ChartData()
    return ajax_data