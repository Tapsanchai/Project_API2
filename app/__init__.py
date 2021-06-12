from flask import Flask, render_template
 
app = Flask(__name__)
app.config['SECRET_KEY'] ='mykey'
app.config['DEBUG'] = True

from .api_covid19 import *
from .api_PM25_Thailand import *
from .api_Weather_Thailand7D import *
from .api_Weather_ThailandTD import *

@app.route("/", methods=(['GET', 'POST']))
@app.route("/index", methods=(['GET', 'POST']))
def Show_Index():

    arguments_pm25 = show_pm25(PM_25_url_TH)
    arguments_covid = show_covid(Covid19_url_TH,Covid19_url_World)
    arguments_Weather7d = show_weather7d(WeatherForecast7Days_url_TH)
    arguments_Weathertd = show_weathertd(WeatherToDay_url_TH)
    '''
    arguments_covid = show_covid(Covid19_url_TH,Covid19_url_World))
    Value_WT=arguments_Weather
    return render_template("test.html",Value_Covid=arguments_covid, Value_PM25=arguments_pm25, 
    Value_WForcast=arguments_WeatherForecast7Days, Value_WToday=arguments_WeatherToday)
    '''
    return render_template("index.html",Value_PM25=arguments_pm25, Value_Covid=arguments_covid, 
    Value_WT=arguments_Weather7d, Value_WToday=arguments_Weathertd )


if __name__ == '__main__':
    #app.debug = True
    #app.run(host='localhost', port=55)
    app.run(debug=True)
