from apis.authentication import authentication_api
from apis.user_routes import  user_apis
from apis.vehicle_routes import vehicles_apis
def register_routes(app, db):

    @app.route("/", methods=["GET"])
    def welcome():
        return "Welcome to Traffic Buddy API."
    


    authentication_api(app, db)
    user_apis(app, db)
    vehicles_apis(app, db)