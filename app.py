from flask import Flask
from controllers.helloworld_controller import helloworld_ep
from controllers.weather_controller import weather_ep
from controllers.Location_Recommendation_controller import location_ep

app=Flask(__name__)

app.register_blueprint(helloworld_ep)
app.register_blueprint(weather_ep, url_prefix='/geocode')
app.register_blueprint(location_ep,url_prefix='/location')

if __name__=="__main__":

    app.run(debug=True)

