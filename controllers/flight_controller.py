from flask import Flask, request, Blueprint, jsonify
import json
import requests
from services.Flight_Services import Flight_Services

flight_ep = Blueprint("flight", __name__)

@flight_ep.route('/key')
def func():
    start_city = request.args.get("scity")
    end_city = request.args.get("ecity")

    print(start_city)
    print(end_city)

    start_place = Flight_Services(start_city)
    end_place = Flight_Services(end_city)

    s_data = start_place.fetch_id()
    e_data = end_place.fetch_id()

    return jsonify({
        "depature": s_data,
        "reach": e_data
    })


@flight_ep.route('/flightplan',methods=['GET','POST'])
def func1():
    start_city = request.form.get("scity")
    end_city = request.form.get("ecity")
    start_date=request.form.get("sdate")
    return_date=request.form.get("rdate")

    # req=request.get_json()
    # print("------------------------------------------")
    # print(req)


    # start_city = req['session']['scity']['value']
    # end_city = req['session']['ecity']['value']
    # start_date=req['session']['sdate']['value']
    # return_date=req['session']['rdate']['value']

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

    # Get the JSON data from the response and load it into a Python dictionary
    data = response.get_json()
    print(data)
    # Format the JSON data with indentation and ensure it is properly encoded
    return data
