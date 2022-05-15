# -*- coding: utf-8 -*
from flask import Flask, render_template
from routes.sen_route import sensor_bp

app = Flask(__name__)

app.register_blueprint(sensor_bp, url_prefix='/sen_data')

@app.route('/')
def hello_world():
    return render_template('UKSmedia_v2.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
