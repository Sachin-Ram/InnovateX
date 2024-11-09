from flask import Blueprint,render_template,request
import requests
from services.helloworld import helloworld
from services.weather_Services import weather_services

helloworld_ep=Blueprint("hello",__name__,template_folder="templates")
# test_ep=Blueprint("weather",__name__,template_folder="templates")

# @test_ep.route('/')

@helloworld_ep.route('/weather')
def weather():
    obj=weather_services(request.args.get("city"))
    return obj.get_lat_long()

@helloworld_ep.route('/') 
def index():
    h=helloworld("sachin")
    print(h.display_name())
    return h.display_name()
    # return "hi"

@helloworld_ep.route('/hello')
def say():
    return render_template("hello.html")
