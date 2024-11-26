from flask import render_template,Blueprint,request,make_response,jsonify
import requests
from services.weather_Services import weather_services


weather_ep=Blueprint("weather",__name__)



@weather_ep.route('/place',methods=['POST','GET'])
def func():

    # req = request.get_json()
    print("Body:", request.get_data(as_text=True))
    print("Form Data:", request.form)

    req=request.get_json()
    city=req['session']['city']['value']
    obj=weather_services(city)
    response= obj.get_weather()
    weather_data = {
            "city": response["name"],
            "temperature": round(response["main"]["temp"]),  # Convert Kelvin to Celsius
            "description": response["weather"][0]["description"],
            "windspeed": response["wind"]["speed"],
        }
    return make_response(jsonify(weather_data),200)

@weather_ep.route('/hello')
def ind():
    return "hello"


@weather_ep.route('/widget')
def  widg():
    obj1=weather_services(request.args.get("city"))
    data=obj1.extract_data()
    id,apikey=data
    print(id,apikey)
    return render_template('weather_widget.html', cityid=id, appid=apikey)