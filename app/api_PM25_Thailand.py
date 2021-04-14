from app import __init__
from flask import json
import requests 

PM_25_url_TH = "http://api.airvisual.com/v2/city?city=Chiang Rai&state=Chiang Rai&country=Thailand&key=eb400bfd-3588-4482-9411-5fd3d7d434a8"

def show_pm25(url_th):
    
    response = requests.get(url_th)
    result = json.loads(response.text)
    Now_AQI = result['data']['current']['pollution']['aqius']
    return Now_AQI

if __name__ == '__main__':
    show_pm25()
