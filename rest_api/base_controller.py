'''



'''

from . import api
# from flask import current_app as app
from flask import request
from flask import render_template
import random

# Local import
# from .response_utils import JSON_MIME_TYPE, success_, success_json

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/result', methods=['POST'])
def result():
    return render_template('index.html', result = {'1' : '2'})
