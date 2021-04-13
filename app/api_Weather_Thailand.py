
import requests
import json 
#from api_PM25_Thailand import * 

#WeatherToday
WeatherToday_url = "https://data.tmd.go.th/api/WeatherToday/V1/?type=json"
response1 = requests.get(WeatherToday_url)
result1 = json.loads(response1.text)

#WeatherForecast7Days
WeatherForecast7Days_url = "http://data.tmd.go.th/api/WeatherForecast7Days/V1/?type=json"
response2 = requests.get(WeatherForecast7Days_url)
result2 = json.loads(response2.text)

#Value of WeatherToday
Now_Datetime = result1['Header']['LastBuiltDate']
Now_City = result1['Stations'][2]['StationNameTh']
Now_Temperature = result1['Stations'][2]['Observe']['Temperature']['Value']

#Value of WeatherForecast7Days
Forecast = result2['Provinces'][0]['SevenDaysForecast']
Forecast_City = result2['Provinces'][0]['ProvinceNameTh']
Forecast_Datetime = result2['Provinces'][0]['SevenDaysForecast'][0]['Date']
'''
Forecast_WeatherDescription = result2['Provinces'][0]['SevenDaysForecast'][0]['WeatherDescription']
Forecast_MaxTemperature = result2['Provinces'][0]['SevenDaysForecast'][0]['MaxTemperature']['Value']
Forecast_MinTemperature = result2['Provinces'][0]['SevenDaysForecast'][0]['MinTemperature']['Value']
Forecast_WindSpeed = result2['Provinces'][0]['SevenDaysForecast'][0]['WindSpeed']['Value']
''' 

'''
print("วัน/เดือน/ปี (เวลา):", Now_Datetime)
print("จังหวัด:", Now_City)
print("อุณหภูมิปัจจุบัน:", Now_Temperature, "°C")
print(" ")
'''

for i in Forecast:
    if i == Forecast[0]:
        continue
    Datetime = i['Date']
    WeatherDescription = i['WeatherDescription']
    MaxTemperature = i['MaxTemperature']['Value']
    MinTemperature = i['MinTemperature']['Value']
    WindSpeed = i['WindSpeed']['Value']
'''
    print("วัน/เดือน/ปี:", Datetime)
    print("จังหวัด:", Forecast_City)
    print("สภาพอากาศ:", WeatherDescription)
    print("อุณหภูมิ(สูงสุด-ต่ำสุด):", MaxTemperature, "-", MinTemperature, "°C")
    print("แรงลม:", WindSpeed, "km/h")
    print(" ")
'''
