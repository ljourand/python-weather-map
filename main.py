import requests
import os
from dotenv import load_dotenv

load_dotenv()

LANG = "en"
UNITS = os.getenv('UNITS') or "metric" # "standard", "metric" or "imperial"
API_KEY = os.getenv('API_KEY')

def getNameOfCity():
    cityName = input("enter the name of a city: ")
    return (cityName)

def getWeatherInfoOfCity(cityName):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&lang={}&units={}&appid={}".format(cityName, LANG, UNITS, API_KEY)
    response = requests.get(url)
    if (response.ok):
        result = response.json()
        return result
    else:
        error = response.json()
        raise Exception(error["message"])
    
def printWeather(weather):
    cityName = weather["name"]
    temperature = weather["main"]["temp"]
    humidity = weather["main"]["humidity"]
    unit = "°C"
    match UNITS:
        case "standard":
            unit = "K"
        case "imperial":
            unit = "°F"
        case "metric":
            unit = "°C"
    print("in {} the temperature is {}{} and the humidity is {}%.".format(cityName, temperature, unit, humidity))
    

def main():
    cityName = getNameOfCity()
    try:
        result = getWeatherInfoOfCity(cityName)
        printWeather(result)
    except Exception as error:
        print(str(error))
        exit(1)

main()