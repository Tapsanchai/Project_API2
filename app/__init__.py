from flask import Flask, render_template
import requests
import json


# ---------------------------------------------------------------------------------------------------------------------------------------------------
# AQI_PM2.5
PM_2_5_url = "http://api.airvisual.com/v2/city?city=Bangkok&state=Bangkok&country=Thailand&key=eb400bfd-3588-4482-9411-5fd3d7d434a8"

response = requests.get(PM_2_5_url)
result = json.loads(response.text)
Now_AQI = result['data']['current']['pollution']['aqius']
#print("ดัชนี AQI(PM2.5): ", Now_AQI)
# ---------------------------------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Covid19 today[thailand]
Covid19_url ="https://covid19.th-stat.com/api/open/today"
response_covid19 = requests.get(Covid19_url)
result_covid19 = json.loads(response_covid19.text)
Now_Covid19 = result_covid19
# ---------------------------------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Covid19 All World 
url_covid_all = "https://covid-19-world-data-by-zt.p.rapidapi.com/GetTotalCounts"

headers = {
    'x-rapidapi-key': "06cc87bd05msh5f606bb8f4a703ap1df09fjsn7f38f410331e",
    'x-rapidapi-host': "covid-19-world-data-by-zt.p.rapidapi.com"
    }

response_covid_World = requests.request("GET", url_covid_all, headers=headers)
Now_Covid19_all = json.loads(response_covid_World.text)
Data_Covid19_all = Now_Covid19_all['data'][0]
# ---------------------------------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------------------------------------
# WeatherToday
WeatherToday_url = "https://data.tmd.go.th/api/WeatherToday/V1/?type=json"
response1 = requests.get(WeatherToday_url)
result1 = json.loads(response1.text)

# WeatherForecast7Days
WeatherForecast7Days_url = "http://data.tmd.go.th/api/WeatherForecast7Days/V1/?type=json"
response2 = requests.get(WeatherForecast7Days_url)
result2 = json.loads(response2.text)

# Value of WeatherToday
Now_Datetime = result1['Header']['LastBuiltDate']
Now_City = result1['Stations'][84]['StationNameTh']
Now_Temperature = result1['Stations'][84]['Observe']['Temperature']['Value']
Data_WeatherToday = {"Datetime": Now_Datetime,
                     "City": Now_City, "Tem": Now_Temperature, "PM25": Now_AQI}

# Value of WeatherForecast7Days
Forecast = result2['Provinces'][36]['SevenDaysForecast']
Forecast_City = result2['Provinces'][36]['ProvinceNameTh']
Forecast_Datetime = result2['Provinces'][36]['SevenDaysForecast'][0]['Date']
Data_WeatherForecast7Days = {
    "Forecast": Forecast, "Forecast_City": Forecast_City, "Forecast_Date": Forecast_Datetime}
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

'''
for i in Forecast:
    if i == Forecast[0]:
        continue
    Datetime = i['Date']
    WeatherDescription = i['WeatherDescription']
    MaxTemperature = i['MaxTemperature']['Value']
    MinTemperature = i['MinTemperature']['Value']
    WindSpeed = i['WindSpeed']['Value']

    print("วัน/เดือน/ปี:", Datetime)
    print("จังหวัด:", Forecast_City)
    print("สภาพอากาศ:", WeatherDescription)
    print("อุณหภูมิ(สูงสุด-ต่ำสุด):", MaxTemperature, "-", MinTemperature, "°C")
    print("แรงลม:", WindSpeed, "km/h")
    print(" ")
'''
# ---------------------------------------------------------------------------------------------------------------------------------------------------

app = Flask(__name__)


@app.route("/")
def Show_Index():
    return render_template("index.html", Value_WToday=Data_WeatherToday, Value_WForcast=Data_WeatherForecast7Days, Value_Covid=Now_Covid19, Value_Covid_World=Data_Covid19_all)



if __name__ == "__main__":
    #app.debug = True
    #app.run(host='localhost', port=55)
    app.run(debug=True)
