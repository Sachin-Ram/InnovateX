from flask import Flask, request, jsonify
from dotenv import load_dotenv
import json
import requests
import os

load_dotenv()

class Flight_Services:

    def __init__(self, city="null"):
        self.flight_apikey = os.getenv('flight_apikey')
        self.city = city

    def fetch_id(self):
        url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchAirport"
        headers = {
            "x-rapidapi-key": self.flight_apikey,
            "x-rapidapi-host": "sky-scrapper.p.rapidapi.com"
        }
        querystring = {"query": self.city, "locale": "en-US"}

        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            data = response.json()
            first_entry = data.get('data', [{}])[0]  # Safely get the first entry
            return {
                'skyId': first_entry.get('skyId', 'N/A'),
                'entityId': first_entry.get('entityId', 'N/A')
            }
        else:
            return {"error": "Failed to fetch data from the API"}

    def fetch_flight(self, origin_eid, origin_sid, dest_eid, dest_sid, start_date, return_date):
        url = "https://sky-scrapper.p.rapidapi.com/api/v2/flights/searchFlights"
        querystring = {
            "originSkyId": origin_sid,
            "destinationSkyId": dest_sid,
            "originEntityId": origin_eid,
            "destinationEntityId": dest_eid,
            "date": start_date,
            "returnDate": return_date,
            "cabinClass": "economy",
            "adults": "1",
            "currency": "INR",
            "market": "en-GB",
            "countryCode": "IN"
        }

        headers = {
            "x-rapidapi-key": self.flight_apikey,
            "x-rapidapi-host": "sky-scrapper.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            data = response.json()
            json_data = data.get("data", {})
            results = []

            for itinerary in json_data.get("itineraries", []):
                result = {
                    "itinerary_id": itinerary.get("id", "N/A"),
                    "price": itinerary.get("price", {}).get("formatted", "N/A"),
                    "legs": []
                }
                for leg in itinerary.get("legs", []):
                    leg_info = {
                        "plane_name": leg.get("carriers", {}).get("marketing", [{}])[0].get("name", "Unknown Airline"),
                        "departure_time": leg.get("departure", "N/A"),
                        "arrival_time": leg.get("arrival", "N/A"),
                        "origin": leg.get("origin", {}).get("name", "N/A"),
                        "destination": leg.get("destination", {}).get("name", "N/A"),
                    }
                    result["legs"].append(leg_info)

                results.append(result)

            # Limit results to the top 3 itineraries
            limited_results = results[:3]
            final_result = {}

            for i, data in enumerate(limited_results):
                plan_key = f"plan {i + 1}"
                first_leg = data["legs"][0]  # First leg
                last_leg = data["legs"][-1]  # Last leg
                final_result[plan_key] = {
                    "airlines": first_leg.get('plane_name', 'Unknown Airline'),
                    "price": data["price"],
                    "origin": first_leg.get('origin', 'N/A'),
                    "destination": last_leg.get('destination', 'N/A'),
                    "start_departure_time": first_leg.get('departure_time', 'N/A'),
                    "start_reach_time": first_leg.get('arrival_time', 'N/A'),
                    "end_departure_time": last_leg.get('departure_time', 'N/A'),
                    "end_arrival_time": last_leg.get('arrival_time', 'N/A')
                }

            return jsonify(final_result)

        else:
            return {"error": "Failed to fetch data from the API"}