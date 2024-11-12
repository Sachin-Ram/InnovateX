from flask import Flask,Blueprint,request,jsonify
from services.Location_Recommendation import Location_Recommender

location_ep=Blueprint("location",__name__)

@location_ep.route('/recommend')
def func():
    recommendor = Location_Recommender(data_file="/home/sachin/Innovate_X_/Dataset/updated_travel_recommendations.csv")
    data=recommendor.recommend_city(user_preferences=request.args.get("place"))
    print(data)
    loc=data.to_json()
    return jsonify(loc)

