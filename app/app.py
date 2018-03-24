from flask import Blueprint
from flask_restful import Api
from resources.models import *

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Add routes
api.add_resource(Books, '/')
