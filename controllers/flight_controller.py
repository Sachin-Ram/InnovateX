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


@flight_ep.route('/flightplan')
def func1():
    start_city = request.args.get("scity")
    end_city = request.args.get("ecity")
    start_date=request.args.get("sdate")
    return_date=request.args.get("rdate")
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

    # Format the JSON data with indentation and ensure it is properly encoded
    return jsonify(data)
