from app import __init__
import requests
import json  

def show_weather(url_w_th):
    # WeatherToday
    response1 = requests.get(url_w_th)
    result1 = json.loads(response1.text)

    # Value of WeatherToday
    Now_Datetime = result1['Header']['LastBuiltDate']
    Now_City = result1['Stations'][84]['StationNameTh']
    Now_Temperature = result1['Stations'][84]['Observe']['Temperature']['Value']
    Data_WeatherToday = {"Datetime": Now_Datetime,"City": Now_City, "Tem": Now_Temperature}
    return Data_WeatherToday

def show_weatherF(url_wf_th):
    # WeatherForecast7Days
    response2 = requests.get(url_wf_th)
    result2 = json.loads(response2.text)

    # Value of WeatherForecast7Days
    Forecast = result2['Provinces'][36]['SevenDaysForecast']
    Forecast_City = result2['Provinces'][36]['ProvinceNameTh']
    Forecast_Datetime = result2['Provinces'][36]['SevenDaysForecast'][0]['Date']
    Data_WeatherForecast7Days = {"Forecast": Forecast, "Forecast_City": Forecast_City, "Forecast_Date": Forecast_Datetime}
    return Data_WeatherForecast7Days
