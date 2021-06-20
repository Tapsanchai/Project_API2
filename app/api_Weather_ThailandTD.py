# from app import __init__
import requests
import json
from datetime import date

WeatherToDay_url_TH = "https://data.tmd.go.th/nwpapi/v1/forecast/area/place"

def show_weathertd(url_w_th):

    today = date.today()
    #today_for_time = datetime.today()
    #current_time = today_for_time.strftime("%X")
    value_datetime = str(str(today)+"T14:00:00")
    txt_dt = str(value_datetime)

    querystring = {"domain":"2", "province":"กรุงเทพมหานคร", "amphoe":"หลักสี่", "tambon":"ทุ่งสองห้อง", "fields":"tc,rh,rain,ws10m,cond", "starttime":""}

    if 'starttime' in querystring.keys():
        querystring['starttime'] = txt_dt
    

    headers = {
    'accept': "application/json",
    'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjIwNDk3MDI0YTkxNTk2NzRmMzgyZjM5ZGEzMjIwOTA3OWZjN2Q3MjIyNWZiZDhmMmNlODk5MzRjZjU5ZGNhZjJlZGFiZGMwODkwYzlmOTc0In0.eyJhdWQiOiIyIiwianRpIjoiMjA0OTcwMjRhOTE1OTY3NGYzODJmMzlkYTMyMjA5MDc5ZmM3ZDcyMjI1ZmJkOGYyY2U4OTkzNGNmNTlkY2FmMmVkYWJkYzA4OTBjOWY5NzQiLCJpYXQiOjE2MTg0MDA2OTgsIm5iZiI6MTYxODQwMDY5OCwiZXhwIjoxNjQ5OTM2Njk4LCJzdWIiOiIxMjYyIiwic2NvcGVzIjpbXX0.AH9lX3jbtD7YHJKS3b5SmuTNhKAaSDS7ORzr779idrZ-V4DFrMw3-ZZwbyDSbO9-EuvOr9HsJ0pWryzNX7ttot7D6eV-EKHaBipcIsPBFJsC03dCRt7b3CEPTOqXONRAoNorFJmrqs4gph0bVPk3S0Ex4AQog-7D33Ua6XMyPhj1mjzFCtFOHhtosE90ZTYKoL78H9NEMv4H5CmA1LVC0xez0lKEQcT7gf5-zR1ykqCX64hotCQ4CT9B9xqU_bopoXKtk4bPIAw7-gplldv8aaCp9vtLQcuTlzGKh0ezOZ1bb0F1eewZBvqwv74yGs7RVonCjysfe4h3xebq2AG-Bu-DG3DAtzkTVX3ECbSKqjF4SLZhoiySjbEuMwBVs7Mz41l6viIRCWgc7pl3CVI0CtuV5VBV9nc5d1Y3948kwmOHGJLamMhlfaa_nHFozZV4oef2b_CyJdCImH_miSQSzLdkBlHsVk7JFwReJdPwsYprZujx5VhOSKrliDuLZGR2fBbnMAsLrHWYaSm9nq6O1kPjsZaLM8D6TYDbaFk3qw9r1-d94lDoIf8pDDuECGZcL2nH5mYbHWYhjyszgKgQLduSVA70B7cMl4m-ivQwrMEmwgK43X-pMQSIdToETkMxulcU9EenEAgxfDDDK5wiG4NHW7c6sYNDpr3fAEExyS8",
    }

    response = requests.request("GET", url_w_th, headers=headers, params=querystring)
    json_txt_td = json.loads(response.text)

    Forecast_data_td = json_txt_td['WeatherForecasts'][0]['forecasts'][0]['data'] 
    return Forecast_data_td


# if __name__ == '__main__':
#     show_weathertd()