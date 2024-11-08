from flask import Flask
from controllers.helloworld_controller import helloworld_ep

app=Flask(__name__)

app.register_blueprint(helloworld_ep)

if __name__=="__main__":

    app.run(debug=True)

