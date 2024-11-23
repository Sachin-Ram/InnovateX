from flask import Flask,Blueprint,request,jsonify,make_response
from services.Location_Recommendation import Location_Recommender

location_ep=Blueprint("location",__name__)

@location_ep.route('/recommend',methods=['GET','POST'])
def func():
    recommendor = Location_Recommender(data_file="/home/sachin/Innovate_X_/Dataset/updated_travel_recommendations.csv")
    data=recommendor.recommend_city(user_preferences=request.args.get("place"))
    print(data)
    loc=data.to_json()
    return jsonify(loc)


@location_ep.route('/test',methods=['GET','POST'])
def test():
    data = {'name': 'John Doe'}
    response = make_response(jsonify(data), 200)
    response.headers["ngrok-skip-browser-warning"] ="45200"
    return response

   

