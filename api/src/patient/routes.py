""" Import module """
from flask import request, jsonify
from src.patient import patient
from src.models.models import User, get_on_call_pharmacy
from src.constants.url_pharmacies import URL_ABOBO, URL_COCODY, URL_YOPOUGON
from src.utils.scrap_pharmacies import web_scrap


@patient.post('/')
def register() -> str:
    """
    Route for registering data
    """
    data = request.get_json()
    user = User(data)
    user.register()
    return "Reussi"


@patient.get('/<user_id>')
def get_user(user_id):
    """
    Route for return data by user id
    """
    user = User.get_user(user_id)
    return user


@patient.put('/<user_id>')
def update_user(user_id):
    """
    Route for updating data
    """
    data_to_update = request.get_json()
    modified_user = User.update_user(user_id, data_to_update)
    return "Bien modifié" if modified_user == 1 else "La modification a échoué"


@patient.get('/on-call-pharmacy')
def get_on_call_clinic():
    """
    Route for return on call pharmacy
    """
    pharmacies = get_on_call_pharmacy()
    return jsonify(pharmacies)


@patient.post('/on-call-pharmacy')
def set_on_call_clinic():
    """
    Route for set on call pharmacy
    """
    pharmacies = {
        "abobo": URL_ABOBO,
        "cocody": URL_COCODY,
        "yopougon": URL_YOPOUGON
    }

    web_scrap(pharmacies)
    return "Ok"

@patient.get('/list-pharmacy')
def get_list_pharmacy():
    """
    Route for test with vue app
    """
    listMedocs = [
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle desdoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle desdoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle desdoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle desdoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle desdoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle desdoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle desdoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle desdoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle desdoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle desdoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle desdoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle desdoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle desdoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle desdoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle desdoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle aryzoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle aryzoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle aryzoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle aryzoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle aryzoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle aryzoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle aryzoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle aryzoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle aryzoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle aryzoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle aryzoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle aryzoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle aryzoboique"},
        {"nomC": "Medicament 1", "nomS": "Benzebol", "molecule": "De Methyle aryzoboique"},
    ]
    return jsonify(listMedocs)
    