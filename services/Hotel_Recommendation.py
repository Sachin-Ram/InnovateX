import requests
import json
import os

class Hotel_Recommendation:

    def __init__(self, city):
        self.city = city
        self.api = os.getenv('hotel_api')

    def recommend(self):
        url = os.getenv('url')
        querystring = {"query": self.city}
        host = os.getenv('host')
        headers = {
            "x-rapidapi-key": self.api,
            "x-rapidapi-host": host
        }

        response = requests.get(url, headers=headers, params=querystring)
        print(response.json())
        return response.json()

    def planner(self):
        url = "https://tripadvisor-scraper.p.rapidapi.com/hotels/list"
        querystring = {"query": self.city, "page": "1"}

        headers = {
            "x-rapidapi-key": self.api,
            "x-rapidapi-host": "tripadvisor-scraper.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

    # Check for a successful response
        if response.status_code == 200:
            data = response.json()  
            hotels = data.get("results", [])  
        else:
            print(f"Error: {response.status_code}")
            return {"error": "Failed to fetch hotel data"}
        
        sorted_hotels = sorted(hotels, key=lambda x: x.get("rating", 0), reverse=True)
        top_hotels = sorted_hotels[:4]

        exchange_rate = 83 #to convert the USD to INR

        formatted_response = {}
        for i, hotel in enumerate(top_hotels):
            plan_key = f"plan {i + 1}" 
            price_in_usd = hotel.get("price_range_usd", {}).get("max", "N/A")
        
            if price_in_usd != "N/A":
                price_in_inr = round(float(price_in_usd) * exchange_rate, 2)

            formatted_response[plan_key] = {
                "name": hotel.get("name", "N/A"),
                "rating": hotel.get("rating", "N/A"),
                "price": price_in_inr
            }

        return formatted_response
