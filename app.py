from flask import Flask
from controllers.helloworld_controller import helloworld_ep
from controllers.weather_controller import weather_ep
from controllers.Location_Recommendation_controller import location_ep
from controllers.authController import auth_ep

app=Flask(__name__)

app.register_blueprint(helloworld_ep)
app.register_blueprint(weather_ep, url_prefix='/geocode')
app.register_blueprint(location_ep,url_prefix='/location')
app.register_blueprint(auth_ep,url_prefix="/auth")

if __name__=="__main__":

    app.run(debug=True)
