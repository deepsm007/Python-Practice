import pandas as pd
import requests
from bs4 import BeautifulSoup

# Getting data from URL
page = requests.get("https://weather.com/weather/today/l/-12.27,136.82?locale=en_US&temp=f")
soup = BeautifulSoup(page.content,'html.parser')
week = soup.find(id='LookingAhead')
items = week.find_all(class_='today-daypart-content')

# Storing required data in variables like day, temp, high-low, etc
day = [item.find(class_='today-daypart-title').getText() for item in items]
description = [item.find(class_='today-daypart-wxphrase').getText() for item in items]
high_low = [item.find(class_='today-daypart-hilo').getText() for item in items]
temp = [item.find(class_='today-daypart-temp').getText() for item in items]
precip = [item.find(class_='today-daypart-precip').getText() for item in items]

# Storing data in dictionary using panda library
weather_stuff = pd.DataFrame(
    {
     'Day': day,
     'Description':description,
     'High_Low':high_low,
     'Temperature':temp,
     'Precipitation':precip,
    }
)

print(weather_stuff)

# Storing the retrieved data in a csv file
weather_stuff.to_csv('weather.csv')






