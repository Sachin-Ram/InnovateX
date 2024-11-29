from flask import Flask,Blueprint,request,jsonify,make_response
import json
import string
from services.Location_Recommendation import Location_Recommender

location_ep=Blueprint("location",__name__)

preferences=None

@location_ep.route('/recommend',methods=['GET','POST'])
def func():
    # req = request.get_json()
    print("Body:", request.get_data(as_text=True))
    print("Form Data:", request.form)
    
    req=request.get_json()
    data=req['session']['preferences']['value']
    print(data)
    if len(data)>1:
        preferences=','.join(data)
    else:
        preferences=data[0]
    recommendor = Location_Recommender()
    data=recommendor.recommend_city(user_preferences=preferences)
    # data=recommendor.recommend_city(user_preferences="beach")
    data_dict=json.loads(data.to_json())
    response_data = {}
    for idx, (key, value) in enumerate(data_dict.get('City', {}).items()):
        letter = string.ascii_uppercase[idx]  # Get the letter corresponding to the index
        response_data[f"city{letter}"] = value
    print(response_data)
    # Return as a JSON response
    return make_response(jsonify(response_data), 200)


@location_ep.route('/test',methods=['GET','POST'])
def test():

    recommendor = Location_Recommender(city_data_file="/home/sachin/Innovate_X_/Dataset/updated_travel_recommendations.csv",place_data_file="/home/sachin/Innovate_X_/Dataset/Updated_Places.csv")
    data=recommendor.recommend_places(city="Madurai",user_preferences=preferences)
    print(data)
    return jsonify(data)
    # data = {'name': 'John Doe'}
    # response = make_response(jsonify(data), 200)
    # response.headers["ngrok-skip-browser-warning"] ="45200"
    # return response

   

