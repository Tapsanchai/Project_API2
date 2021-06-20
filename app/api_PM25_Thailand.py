# from app import __init__
import json
import requests 

PM_25_url_TH = "http://api.airvisual.com/v2/nearest_city?lat=13.87&lon=100.55&key=eb400bfd-3588-4482-9411-5fd3d7d434a8"

def show_pm25(url_th):

    payload={}
    files={}
    headers = {}
    
    response = requests.request("GET", url_th, headers=headers, data=payload, files=files)
    result = json.loads(response.text)
    Now_AQI = result['data']['current']['pollution']['aqius']
    return Now_AQI

# if __name__ == '__main__':
#     show_pm25()
