#!/usr/local/bin/python3
import datetime
import requests

contents = requests.get("http://api.openweathermap.org/data/2.5/weather?q=St%20Albans,GB&APPID=f44256870e8efe98c4f59aa15ee82b47")).json()
temp = contents['main']['temp']

print('weather,location=lon temperature='+str(temp))
