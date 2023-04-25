from flask import Flask, Blueprint
from flask_restful import Api
from authman.config import Config
#print(Config.ENV)
apiv1_bp=Blueprint("apiv1",__name__,url_prefix="/api/v1")
apiv1=Api(apiv1_bp)

from authman import resource
def create_app():
    app= Flask(__name__)
    app.config.from_object(Config) #Load application config
    app.register_blueprint(apiv1_bp) #Load api v1
    return app

# if __name__=="__main__":
#     app.run(host="0.0.0.0",port=5001)