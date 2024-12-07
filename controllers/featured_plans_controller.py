from flask import Flask,request,Blueprint
from services.Flight_Services import Flight_Services
from services.Hotel_Recommendation import Hotel_Recommendation
from controllers.authController import auth


featured_plan_ep=Blueprint("featured_plan",__name__)

@featured_plan_ep.route("/fetch",methods=['GET','POST'])

def function():

    start_city = request.form.get("scity")
    end_city = request.form.get("ecity")
    start_date=request.form.get("sdate")
    return_date=request.form.get("rdate")
    name=request.form.get("name")
    email=request.form.get("email")

    print(start_city)
    print(end_city)
    print(start_date)
    print(return_date)
    
    
    start_place = Flight_Services(start_city)
    end_place = Flight_Services(end_city)

    s_data = start_place.fetch_id()
    e_data = end_place.fetch_id()

    print(s_data['skyId'])
    print(s_data['entityId'])

    flight = Flight_Services()
    response = flight.fetch_flight(
        origin_sid=s_data['skyId'],
        origin_eid=s_data['entityId'],
        dest_eid=e_data['entityId'],
        dest_sid=e_data['skyId'],
        start_date=start_date,
        return_date=return_date
    )

    data = response.get_json()
    print(data)

    # Instantiate recommendation object and fetch recommendations
    hotel_obj = Hotel_Recommendation(end_city)

    response=hotel_obj.planner()

    final_data={}

    final_data['flight_plans']=data
    final_data['hotel_plans']=response

    authobj=auth(name=name,email=email)

    authobj.add_data(final_data)

    return final_data
