from app import __init__
from flask import json
import requests

WeatherForecast7Days_url_TH = "https://data.tmd.go.th/nwpapi/v1/forecast/location/daily/place"

def show_weather7d(url_wf_th):
    querystring = {"province":u"กรุงเทพมหานคร", "amphoe":u"หลักสี่", "tambon":u"ทุ่งสองห้อง", "fields":"tc_max,tc_min,rh,rain,ws10m,cond", "duration":"7"}

    headers = {
        'accept': "application/json",
        'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjIwNDk3MDI0YTkxNTk2NzRmMzgyZjM5ZGEzMjIwOTA3OWZjN2Q3MjIyNWZiZDhmMmNlODk5MzRjZjU5ZGNhZjJlZGFiZGMwODkwYzlmOTc0In0.eyJhdWQiOiIyIiwianRpIjoiMjA0OTcwMjRhOTE1OTY3NGYzODJmMzlkYTMyMjA5MDc5ZmM3ZDcyMjI1ZmJkOGYyY2U4OTkzNGNmNTlkY2FmMmVkYWJkYzA4OTBjOWY5NzQiLCJpYXQiOjE2MTg0MDA2OTgsIm5iZiI6MTYxODQwMDY5OCwiZXhwIjoxNjQ5OTM2Njk4LCJzdWIiOiIxMjYyIiwic2NvcGVzIjpbXX0.AH9lX3jbtD7YHJKS3b5SmuTNhKAaSDS7ORzr779idrZ-V4DFrMw3-ZZwbyDSbO9-EuvOr9HsJ0pWryzNX7ttot7D6eV-EKHaBipcIsPBFJsC03dCRt7b3CEPTOqXONRAoNorFJmrqs4gph0bVPk3S0Ex4AQog-7D33Ua6XMyPhj1mjzFCtFOHhtosE90ZTYKoL78H9NEMv4H5CmA1LVC0xez0lKEQcT7gf5-zR1ykqCX64hotCQ4CT9B9xqU_bopoXKtk4bPIAw7-gplldv8aaCp9vtLQcuTlzGKh0ezOZ1bb0F1eewZBvqwv74yGs7RVonCjysfe4h3xebq2AG-Bu-DG3DAtzkTVX3ECbSKqjF4SLZhoiySjbEuMwBVs7Mz41l6viIRCWgc7pl3CVI0CtuV5VBV9nc5d1Y3948kwmOHGJLamMhlfaa_nHFozZV4oef2b_CyJdCImH_miSQSzLdkBlHsVk7JFwReJdPwsYprZujx5VhOSKrliDuLZGR2fBbnMAsLrHWYaSm9nq6O1kPjsZaLM8D6TYDbaFk3qw9r1-d94lDoIf8pDDuECGZcL2nH5mYbHWYhjyszgKgQLduSVA70B7cMl4m-ivQwrMEmwgK43X-pMQSIdToETkMxulcU9EenEAgxfDDDK5wiG4NHW7c6sYNDpr3fAEExyS8",
        }

    response = requests.request("GET", url_wf_th, headers=headers, params=querystring)
    json_txt_7d = json.loads(response.text)
    Forecast_city = json_txt_7d['WeatherForecasts'][0]['location']['province']
    Forecast_amphoe = json_txt_7d['WeatherForecasts'][0]['location']['amphoe']
    Forecast_tambon = json_txt_7d['WeatherForecasts'][0]['location']['tambon']
    Forecast_data7d = json_txt_7d['WeatherForecasts'][0]['forecasts'] 
    Forecast_all_data = {"Forecast_city": Forecast_city, "Forecast_amphoe": Forecast_amphoe, 
    "Forecast_tambon": Forecast_tambon, "Forecast_data7d": Forecast_data7d}
    return Forecast_all_data

# if __name__ == '__main__':
#     show_weather7d()