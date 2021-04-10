
import requests
import json 

url = "http://api.airvisual.com/v2/city?city=Chiang Rai&state=Chiang Rai&country=Thailand&key=eb400bfd-3588-4482-9411-5fd3d7d434a8"

response = requests.get(url)
result = json.loads(response.text)
Now_AQI = result['data']['current']['pollution']['aqius']
#print("ดัชนี AQI(PM2.5): ", Now_AQI)

'''
Now_Datetime = result['Header']['LastBuiltDate']

print("DateTime: " + Now_Datetime)
#print(result['Stations'][2])
for key, value in result['Stations'][2].items():
    print(key, value)


for key, value in result['Stations'].items():
    print (key, value)
'''
