from flask import Flask
from authman.config import Config
print(Config.ENV)
def create_app():
    app= Flask(__name__)
    app.config.from_object(Config) #Load application config
    return app

# if __name__=="__main__":
#     app.run(host="0.0.0.0",port=5001)