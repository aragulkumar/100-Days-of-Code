import requests

OWM_Endpoint = "api.openweathermap.org/data/2.5/forecast?"
api_key = "80e53e3e69341c39bbc3c4caa59b6b84"

weather_params = {
    "lat" : 13.072090,
    "lon" : 80.201859,
    "appid" : api_key,
}


response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)