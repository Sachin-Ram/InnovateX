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
            data = response.json()  # Parse the JSON response
            hotels = data.get("results", [])  # Extract the list of hotels (assuming it's under "results")
        else:
            print(f"Error: {response.status_code}")
            return {}

        # Extract the top 4 hotels
        top_hotels = hotels[:4]

        # Build the required JSON response
        # formatted_response = {}
        hotel_keys = ['A', 'B', 'C', 'D']

        # Build the required JSON response
        formatted_response = {}
        for i, hotel in enumerate(top_hotels):
            hotel_key = f"hotel{hotel_keys[i]}"  # Use the letters for keys
            formatted_response[f"{hotel_key}name"] = hotel.get("name", "N/A")
            formatted_response[f"{hotel_key}rating"] = hotel.get("rating", "N/A")
            
            price=hotel.get("price_range_usd", {}).get("max", "N/A")

            formatted_response[f"{hotel_key}price"] = price*80

        # Return the formatted JSON response
        return json.dumps(formatted_response, indent=4)
