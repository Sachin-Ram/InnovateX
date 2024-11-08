from flask import Blueprint,render_template
from services.helloworld import helloworld

helloworld_ep=Blueprint("hello",__name__,template_folder="templates")

@helloworld_ep.route('/') 
def index():
    h=helloworld("sachin")
    print(h.display_name())
    return h.display_name()
    # return "hi"

@helloworld_ep.route('/hello')
def say():
    return render_template("hello.html")
