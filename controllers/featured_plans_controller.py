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
    flight_plan=request.form.get("planf")
    hotel_plan=request.form.get("planh")

    print(start_city)
    print(end_city)
    print(start_date)
    print(return_date)
    
    
    start_place = Flight_Services(start_city)
    end_place = Flight_Services(end_city)

    s_data = start_place.fetch_id()
    e_data = end_place.fetch_id()

    print(s_data.get('skyId'))
    print(s_data.get('entityId'))

    flight = Flight_Services()
    response = flight.fetch_flight(
        origin_sid=s_data.get('skyId'),
        origin_eid=s_data.get('entityId'),
        dest_eid=e_data.get('entityId'),
        dest_sid=e_data.get('skyId'),
        start_date=start_date,
        return_date=return_date
    )

    data = response
    print(data)

    # Instantiate recommendation object and fetch recommendations
    hotel_obj = Hotel_Recommendation(end_city)

    response=hotel_obj.planner()

    final_data={}

    final_data['flight_plans']=data
    final_data['hotel_plans']=response

    authobj=auth(name=name,email=email)

    authobj.add_data(final_data)

    if flight_plan or hotel_plan:  # Check if either exists
        if flight_plan and not hotel_plan:  # Only flight_plan exists
            return {"amount":int(flight_plan)}
        elif hotel_plan and not flight_plan:  # Only hotel_plan exists
            return {"amount":int(hotel_plan)}
        elif flight_plan and hotel_plan:  # Both exist
            return {"amount":int(flight_plan) + int(hotel_plan)}
# If neither exists, no return (could add a default return if needed)


    return final_data
