from flask import Blueprint
api = Blueprint('rest_api', __name__)

from .template_controller import *
from .base_controller import *