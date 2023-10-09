
'''

@author: Raja CSP Raman

'''
import json
from flask import jsonify
from flask import Response

JSON_MIME_TYPE = 'application/json'

def success_(data):
    return data, 200, {'Content-Type': JSON_MIME_TYPE}

def success_json(data):
    print(f'data  :{data} ')
    # data = jsonify(data)
    content = json.dumps(data)
    # content = jsonify(content)
    return content, 200, {'Content-Type': JSON_MIME_TYPE}

def success_response(data):
    response = Response(
        json.dumps(data), status=200, mimetype=JSON_MIME_TYPE
    )
    return response 