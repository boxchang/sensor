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
        sen_type = data.get('sen_type')
        from_date = data.get('from_date')
        to_date = data.get('to_date')
        sensor = Sensor()
        if sen_type is not None and sen_type != "":
            ajax_data = sensor.getSen_ChartData(sen_type, from_date, to_date)

    return ajax_data