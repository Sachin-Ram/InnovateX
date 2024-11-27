from flask import Flask,request
import requests
from dotenv import load_dotenv
load_dotenv()
import os

class Hotel_Recommendation:

    def __init__(self,city):

        self.city=city

        self.api=os.getenv('hotel_api')


    def recommend(self):


        url =os.getenv('url')

        querystring = {"query":self.city}

        host=os.getenv('host')

        headers = {
	        "x-rapidapi-key": self.api,
	        "x-rapidapi-host": host
        }

        response = requests.get(url, headers=headers, params=querystring)

        print(response.json())

        return response.json()




