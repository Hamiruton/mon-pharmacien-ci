import os
import jwt
from flask import request, make_response, jsonify
from functools import wraps
from src.models.models import auth_by_id


def only_patient(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        token = None
        secret_key = os.getenv('FLASK_SECRET_KEY')
        if 'Authorization' in request.headers:
            _ = request.headers['Authorization']
            token = _.split(' ')[1]
            if token == '':
                return make_response(jsonify({"message": "Aucun token fourni"}), 401)

        try:
            data = jwt.decode(token, secret_key, algorithms=['HS256'])
            is_exist = auth_by_id('users', data['public_id'])
        except Exception as e:
            print(e)
            return make_response(jsonify({"message": "Vous ne pouvez pas accéder à cette ressource !!!"}), 401)
        
        if not is_exist:
            return make_response(jsonify({"message": "Vous ne pouvez pas accéder à cette ressource !!!"}), 401)
        
        return func(*args, **kwargs)
    
    return decorator
