from app import __init__
from flask import json
import requests

Covid19_url_TH ="https://covid19.th-stat.com/json/covid19v2/getTodayCases.json"
Covid19_url_World = "https://covid-19-world-data-by-zt.p.rapidapi.com/GetTotalCounts"

def show_covid(url_th, url_world):
    # Covid19 today[thailand]
    response_covid19 = requests.get(url_th)
    result_covid19 = json.loads(response_covid19.text)
    Now_Covid19 = result_covid19

    # Covid19 All World 
    headers = {
        'x-rapidapi-key': "06cc87bd05msh5f606bb8f4a703ap1df09fjsn7f38f410331e",
        'x-rapidapi-host': "covid-19-world-data-by-zt.p.rapidapi.com"
        }

    response_covid_World = requests.request("GET", url_world, headers=headers)
    Now_Covid19_all = json.loads(response_covid_World.text)
    Data_Covid19_all = Now_Covid19_all['data'][0]
    json_of_value_covid = {"Now_Covid19": Now_Covid19, "Data_Covid19_all": Data_Covid19_all}
    return(json_of_value_covid)

# if __name__ == '__main__':
#     show_covid()
    