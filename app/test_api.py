from app import __init__
import requests
import json 

PM_25_url_TH = "http://api.airvisual.com/v2/city?city=Chiang Rai&state=Chiang Rai&country=Thailand&key=eb400bfd-3588-4482-9411-5fd3d7d434a8"
response = requests.get(PM_25_url_TH)
result = json.loads(response.text)
Now_AQI = result['data']['current']['pollution']['aqius']
