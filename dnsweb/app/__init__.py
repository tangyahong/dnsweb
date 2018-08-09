from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

# from flask_restful import Api
# from app.api.ipTableApi import TableApi
# from app.main.apis import TableApi
from app.models import db
from flask_cors import *

# db = SQLAlchemy()
# restful_api = Api()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    db.init_app(app)
    CORS(app, supports_credentials=True)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
