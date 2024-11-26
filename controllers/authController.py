from flask import Flask,request,Blueprint,jsonify,make_response
from services.auth import auth

auth_ep=Blueprint("auth",__name__)

@auth_ep.route("/",methods=['GET','POST'])
def func():


    print("Body:", request.get_data(as_text=True))
    print("Form Data:", request.form)

    req=request.get_json()
    email=req['session']['mail']['value']
    
    object=auth("hello",email)

    data=object.authenticate()

    if data:

        return make_response(jsonify({"status":"success"}),200)
    
    else :

        object.adduser()
        return make_response(jsonify({"status:":"failure"}),404)
    
