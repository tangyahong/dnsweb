from flask import Blueprint
from flask_cors import CORS
api = Blueprint('api', __name__)
CORS(api)
from . import upload, dns, user, decorator, beianQuery, industrial_internet, topn, flow, industry, background