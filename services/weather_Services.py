import os
import requests
from dotenv import load_dotenv
load_dotenv()
from pathlib import Path
import json
from flask import request

# Get the path to the current directory and append the filename
file_path = (Path(__file__).parent / '../Dataset/weather_city.json').resolve()

# Open and load the JSON data
with file_path.open() as file:
    data = json.load(file)

class weather_services:

    def __init__(self,city):

        self.api_key=os.getenv('WEATHER_API')

        self.city=city

        print(self.city)

        

    def get_lat_long(self):

        response=requests.get("http://api.openweathermap.org/geo/1.0/direct?q={}&appid={}".format(self.city,self.api_key))

        data=response.json()

        return data
    
    def get_weather(self):

        # lat_long_data=self.get_lat_long()

        # latitude=lat_long_data[0]["lon"]

        # longitude=lat_long_data[0]["lat"]

        
        weather_data=requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(self.city,self.api_key))
        
        result=weather_data.json()

        return result

    def extract_data(self):

        for item in data:
            if item.get("name").lower()==self.city.lower():
                return (item.get("id"),self.api_key)
        return None


