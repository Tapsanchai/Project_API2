from app.api_covid19 import show_covid
from app.api_PM25_Thailand import show_pm25
from app.api_Weather_Thailand import show_weather, show_weatherF
from flask import Flask, render_template, request, jsonify, json
import requests 

app = Flask(__name__)
app.config['SECRET_KEY'] ='mykey'
app.config['DEBUG'] = True


@app.route("/", methods=(['GET', 'POST']))
@app.route("/index", methods=(['GET', 'POST']))
def Show_Index():
    Covid19_url_TH ="https://covid19.th-stat.com/api/open/today"
    Covid19_url_World = "https://covid-19-world-data-by-zt.p.rapidapi.com/GetTotalCounts"
    PM_25_url_TH = "http://api.airvisual.com/v2/city?city=Chiang Rai&state=Chiang Rai&country=Thailand&key=eb400bfd-3588-4482-9411-5fd3d7d434a8"
    WeatherToday_url_TH = "https://data.tmd.go.th/api/WeatherToday/V1/?type=json"
    WeatherForecast7Days_url_TH = "http://data.tmd.go.th/api/WeatherForecast7Days/V1/?type=json"

    arguments_covid = show_covid(Covid19_url_TH,Covid19_url_World)
    arguments_pm25 = show_pm25(PM_25_url_TH)
    arguments_WeatherToday = show_weather(WeatherToday_url_TH)
    arguments_WeatherForecast7Days = show_weatherF(WeatherForecast7Days_url_TH)

    return render_template("index.html",Value_Covid=arguments_covid, Value_PM25=arguments_pm25, 
    Value_WForcast=arguments_WeatherForecast7Days, Value_WToday=arguments_WeatherToday)

if __name__ == '__main__':
    #app.debug = True
    #app.run(host='localhost', port=55)
    app.run(debug=True)
