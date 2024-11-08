import os
import requests
from dotenv import load_dotenv
load_dotenv()

class weather_services:

    def __init__(self,city):

        
        self.city=city

    def data(self):

        api_key=os.getenv('WEATHER_API')
        
        response=requests.get("http://api.openweathermap.org/geo/1.0/direct?q={}&appid={}".format(self.city,api_key))

        data=response.json()

        return data
