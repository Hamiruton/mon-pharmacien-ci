from flask import request, jsonify
from src.patient import patient
from src.patient.models import User

@patient.route('/')
def index() -> str:
    return "It's a test"

@patient.post('/')
def register() -> str:
    data = request.get_json()
    user = User(data)
    user.register()
    return "Reussi"

@patient.get('/<id>')
def get_user(id):
    user = User.get_user(id)
    return user