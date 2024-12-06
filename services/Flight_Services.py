from flask import Flask,request,jsonify
from dotenv import load_dotenv
import json
import requests
load_dotenv()
import os



class Flight_Services:

    def __init__(self,city="null"):

        self.flight_apikey=os.getenv('flight_apikey')

        self.city=city

    def fetch_id(self):
        url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchAirport"
        headers = {
            "x-rapidapi-key": self.flight_apikey,
            "x-rapidapi-host": "sky-scrapper.p.rapidapi.com"
        }
        
        querystring = {"query": self.city, "locale": "en-US"}

        # Make the request to the Skyscanner API
        response = requests.get(url, headers=headers, params=querystring)

        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()  # Get the JSON data from the response
        
            try:
                # Extract the first entry's skyId and entityId
                first_entry = data.get('data', [])[0]  # Get the first item from the 'data' list
                skyId = first_entry.get('skyId', 'N/A')  # Get the skyId
                entityId = first_entry.get('entityId', 'N/A')  # Get the entityId

                # Return the extracted data as a dictionary
                return {'skyId': skyId, 'entityId': entityId}
            except (IndexError, KeyError) as e:
                # If error occurs, return an error message as dictionary
                return {"error": "Error parsing response data", "message": str(e)}
        else:
            # If the API request fails, return an error message
            return {"error": "Failed to fetch data from the API"}
        

    def fetch_flight(self,origin_eid,origin_sid,dest_eid,dest_sid,start_date,return_date):

        url = "https://sky-scrapper.p.rapidapi.com/api/v2/flights/searchFlights"

        print(origin_eid,origin_sid,dest_eid,dest_sid)

        querystring = {"originSkyId":origin_sid,"destinationSkyId":dest_sid,"originEntityId":origin_eid,"destinationEntityId":dest_eid,"date":start_date,"returnDate":return_date,"cabinClass":"economy","adults":"1","currency":"INR","market":"en-GB","countryCode":"IN"}
        print(querystring)
       # querystring={"originSkyId":"MAA","destinationSkyId":"DEL","originEntityId":"95673361","destinationEntityId":"95673498","date":"2024-12-07","cabinClass":"economy","adults":"1","sortBy":"best","currency":"USD","market":"en-US","countryCode":"US"}

        headers = {
	        "x-rapidapi-key": self.flight_apikey,
	        "x-rapidapi-host": "sky-scrapper.p.rapidapi.com"
        }

        data = requests.get(url, headers=headers, params=querystring)
        data=data.json()
        json_data=data['data']
        print("-----------------------------")
        # print(json_data)
        print("-----------------------------")
        results = []
        for itinerary in json_data["itineraries"]:
            #print(itinerary)
            result = {}
            result["itinerary_id"] = itinerary["id"]
            result["price"] = itinerary["price"]["formatted"]
        
        # Process legs
            result["legs"] = []
            for leg in itinerary["legs"]:
                leg_info = {
                    "plane_name": leg["carriers"]["marketing"][0]["name"],
                    "departure_time": leg["departure"],
                    "arrival_time": leg["arrival"],
                    "origin": leg["origin"]["name"],
                    "destination": leg["destination"]["name"]
                }
                result["legs"].append(leg_info)
        
            results.append(result)

        limited_results = results[:3]
        print(limited_results)
        final_result={}
        for i , data in enumerate(results):
            plan_key=f"plan {i+1}"
            first_leg = data['legs'][0]  # First leg
            last_leg = data['legs'][-1]  # Last leg
            final_result[plan_key]= {
                "airlines":first_leg['plane_name'],
                "price":data['price'][1:],
                "origin":first_leg['origin'],
                "destination":last_leg['origin'],
                "start_departure_time":first_leg['departure_time'],
                "start_reach_time":first_leg['arrival_time'],
                "end_departure_time":last_leg['departure_time'],
                "end_arrival_time":last_leg['arrival_time']
            }

        print(final_result)
        json_data = json.dumps(final_result, indent=4)
    
    # Return as JSON response
        return jsonify(json_data)



