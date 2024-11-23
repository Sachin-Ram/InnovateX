from flask import Flask,request,Blueprint,jsonify
from services.auth import auth

auth_ep=Blueprint("auth",__name__)

@auth_ep.route("/")
def func():

    object=auth("John","john.doe@example.com")

    data=object.authenticate()

    if data:

        return jsonify({"status":"success"}),200
    
    else :

        return jsonify({"status:":"failure"}),404
