from flask import Flask, render_template, request, jsonify, json
import requests 

app = Flask(__name__)
app.config['SECRET_KEY'] ='mykey'
app.config['DEBUG'] = True

from app.api_covid19 import *
from app.api_PM25_Thailand import *
from app.api_Weather_Thailand import *




@app.route("/", methods=(['GET', 'POST']))
@app.route("/index", methods=(['GET', 'POST']))
def Show_Index():
    
    '''
    arguments_covid = show_covid(Covid19_url_TH,Covid19_url_World)
    arguments_pm25 = show_pm25(PM_25_url_TH)
    arguments_WeatherToday = show_weather(WeatherToday_url_TH)
    arguments_WeatherForecast7Days = show_weatherF(WeatherForecast7Days_url_TH)
    
    return render_template("index.html",Value_Covid=arguments_covid, Value_PM25=arguments_pm25, 
    Value_WForcast=arguments_WeatherForecast7Days, Value_WToday=arguments_WeatherToday)
    '''
    arguments_pm25 = show_pm25(PM_25_url_TH)
    return render_template('test.html',Value_PM25=arguments_pm25)

if __name__ == '__main__':
    #app.debug = True
    #app.run(host='localhost', port=55)
    app.run(debug=True)
