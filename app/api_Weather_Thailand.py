import requests
import json  

WeatherToday_url_TH = "https://data.tmd.go.th/api/WeatherToday/V1/?type=json"
WeatherForecast7Days_url_TH = "http://data.tmd.go.th/api/WeatherForecast7Days/V1/?type=json"

def show_weather(url_w_th, url_wf_th):
    # WeatherToday
    response1 = requests.get(url_w_th)
    result1 = json.loads(response1.text)

    # Value of WeatherToday
    Now_Datetime = result1['Header']['LastBuiltDate']
    Now_City = result1['Stations'][84]['StationNameTh']
    Now_Temperature = result1['Stations'][84]['Observe']['Temperature']['Value']
    Data_WeatherToday = {"Datetime": Now_Datetime,"City": Now_City, "Tem": Now_Temperature}

    # WeatherForecast7Days
    response2 = requests.get(url_wf_th)
    result2 = json.loads(response2.text)

    # Value of WeatherForecast7Days
    Forecast = result2['Provinces'][36]['SevenDaysForecast']
    Forecast_City = result2['Provinces'][36]['ProvinceNameTh']
    Forecast_Datetime = result2['Provinces'][36]['SevenDaysForecast'][0]['Date']
    Data_WeatherForecast7Days = {"Forecast": Forecast, "Forecast_City": Forecast_City, "Forecast_Date": Forecast_Datetime}
    
    json_of_value_Weather = {"Data_WeatherToday": Data_WeatherToday, "Data_WeatherForecast7Days": Data_WeatherForecast7Days}

    return json_of_value_Weather


if __name__ == '__main__':
    show_weather()
