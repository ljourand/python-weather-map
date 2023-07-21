# python-weather-map

This is a simple python program that take ask the user to enter a city and output the current temperature and humidity at this place.

The program is using the open weather map api: https://openweathermap.org/

# Requirements

You should have an open weather map api key and put it in .env file in the project with the value API_KEY.

You can also set the unit for the temperature in the .env file with the value UNITS, the possible values are:
- "standard" for kelvins
- "metric" for celsius
- "imperial" for fahrenheit

# Run the program

## With pipenv

To run the program you have to run the command: ```pipenv run py main.py```

more info on pipenv: https://packaging.python.org/en/latest/tutorials/managing-dependencies/#managing-dependencies

## Without pipenv

You need to install the following packages:
- python-dotenv
- requests

Then you can run the program with

Windows: ```py main.py```
UNIX/MacOS: ```python3 main.py```
