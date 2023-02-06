from flask import request, jsonify

from src.patient import patient
from src.models.models import User, get_on_call_pharmacy

from src.constants.url_pharmacies import URL_ABOBO, URL_COCODY, URL_YOPOUGON
from src.utils.scrap_pharmacies import web_scrap


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


@patient.put('/<id>')
def update_user(id):
    data_to_update = request.get_json()
    modified_user = User.update_user(id, data_to_update)

    return "Bien modifié" if modified_user == 1 else "La modification a échoué"


@patient.get('/on-call-pharmacy')
def get_on_call_clinic():
    pharmacies = get_on_call_pharmacy()
    # print(pharmacies)
    return jsonify(pharmacies)


@patient.post('/on-call-pharmacy')
def set_on_call_clinic():
    pharmacies = {
        "abobo": URL_ABOBO,
        "cocody": URL_COCODY,
        "yopougon": URL_YOPOUGON
    }

    web_scrap(pharmacies)
    return "Ok"
