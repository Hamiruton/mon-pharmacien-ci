""" Import module """
from flask import request, jsonify, make_response
from src.patient import patient
from src.models.models import User, get_on_call_pharmacy, Drug
from src.constants.url_pharmacies import URL_ABOBO, URL_COCODY, URL_YOPOUGON
from src.utils.scrap_pharmacies import web_scrap
from src.auth import only_patient


@patient.post('/')
@patient.post('/register')
def register() -> any:
    """
    Route for registering data
    """
    data = request.get_json()
    user = User(data)
    res = user.register()
    if res == False:
        return make_response(jsonify({"message":"Veuillez entrer un autre nom ou email"}), 200)
    else:
        return make_response(jsonify({"message":res}), 201)
    

@patient.post('/login')
def login() -> any:
    """
    Route to login user
    """
    data = request.get_json()
    res = User.login(data)
    if res == "incorrect email":
        return make_response(jsonify({"message":res}), 200)
    elif res == "incorrect password":
        return make_response(jsonify({"message":res}), 200)
    else:
        return make_response(jsonify({"data": res}), 201)


@patient.put('/<user_id>')
@only_patient
def update_user(user_id):
    """
    Route for updating data
    """
    data_to_update = request.get_json()
    modified_user = User.update_user(user_id, data_to_update)
    return "Bien modifié" if modified_user == 1 else "La modification a échoué"


@patient.get('/on-call-pharmacy')
@only_patient
def get_on_call_clinic():
    """
    Route for return on call pharmacy
    """
    pharmacies = get_on_call_pharmacy()
    return jsonify(pharmacies)


@patient.post('/on-call-pharmacy')
@only_patient
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


@patient.get('/medocs/<idMedoc>')
@only_patient
def get_all_clinic_have_drug(idMedoc:str):
    """
    Route for get all officines that have idMedoc
    """
    res = Drug.get_officine_have_drugs(drug_id=idMedoc)
    return jsonify(res)


@patient.get('/medocs')
@only_patient
def get_all_drugs():
    """
    Route for get all officines that have idMedoc
    """
    res = Drug.get_all_drugs()
    #print(res)
    return jsonify(res)


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
    