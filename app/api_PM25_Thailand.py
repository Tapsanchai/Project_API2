from app import __init__
import requests
import json 

def show_pm25(url_th):

    response = requests.get(url_th)
    result = json.loads(response.text)
    Now_AQI = result['data']['current']['pollution']['aqius']
    return Now_AQI