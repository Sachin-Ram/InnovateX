from flask import Flask, Blueprint, request, make_response, jsonify
from services.Hotel_Recommendation import Hotel_Recommendation

hotel_ep = Blueprint("hotel", __name__)

@hotel_ep.route('/find', methods=['GET', 'POST'])
def func():
    # Parse the request
    req = request.get_json()
    location = req['session']['location']['value']

    # Instantiate recommendation object and fetch recommendations
    hotel_obj = Hotel_Recommendation(location)
    data = hotel_obj.recommend()  # Assuming this returns a list of dictionaries
    print(data)
    # Filter and structure the output
    keys = ["One", "Two", "Three", "Four"]
    filtered_hotels = {}

# Only consider the first 4 accommodations of type "accommodation"
    count = 0
    for item in data:
        if item["type"] == "accommodation" and count < 4:
            filtered_hotels[f"hotelName{keys[count]}"] = item["name"]
            filtered_hotels[f"hotelLink{keys[count]}"] = item["link"]
            count += 1

    print(filtered_hotels)
    return make_response(jsonify(filtered_hotels), 200)
    # Return the response
    

@hotel_ep.route('/plan',methods=['GET','POST'])

def plan():

    # req = request.get_json()
    # location = req['session']['location']['value']
    location=request.form.get("location")

    # Instantiate recommendation object and fetch recommendations
    hotel_obj = Hotel_Recommendation(location)

    response=hotel_obj.planner()

    #print(response)

    return response