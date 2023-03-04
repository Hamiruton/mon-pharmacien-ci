""" Import module """
from werkzeug.utils import secure_filename
from flask import request, jsonify, make_response
from src.patient import patient
from src.models.models import User, get_on_call_pharmacy, Drug, Prescription
from src.constants.url_pharmacies import URL_ABOBO, URL_COCODY, URL_YOPOUGON
from src.utils.scrap_pharmacies import web_scrap
from src.auth import token_required


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
@token_required('users')
def update_user(user_id):
    """
    Route for updating data
    """
    data_to_update = request.get_json()
    modified_user = User.update_user(user_id, data_to_update)
    return "Bien modifié" if modified_user == 1 else "La modification a échoué"


@patient.get('/on-call-pharmacy')
@token_required('users')
def get_on_call_clinic():
    """
    Route for return on call pharmacy
    """
    pharmacies = get_on_call_pharmacy()
    return jsonify(pharmacies)


@patient.post('/on-call-pharmacy')
@token_required('users')
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
@token_required('users')
def get_all_clinic_have_drug(idMedoc:str):
    """
    Route for get all officines that have idMedoc
    """
    res = Drug.get_officine_have_drugs(drug_id=idMedoc)
    return jsonify(res)


@patient.get('/medocs')
@token_required('users')
def get_all_drugs():
    """
    Route for get all officines that have idMedoc
    """
    res = Drug.get_all_drugs()
    #print(res)
    return make_response(jsonify({'data': res}), 200)


@patient.get('/medocs/name/<nameMedoc>')
#@token_required('users')
def get_affiliatedOf_by_nameMedoc(nameMedoc):
    """
    Route for get all officines that have idMedoc
    """
    res = Drug.get_affiliatedOf_by_nameMedoc(nameMedoc)
    #print(res)
    return make_response(jsonify({'data': res}), 200)

import os

@patient.post('/upload')
#@token_required('users')
def upload_file():
    """
    Route for uploading files
    """
    folder = os.getenv('FLASK_UPLOAD_FOLDER')
    if 'file' not in request.files:
        return make_response(jsonify({'message':"Pas de fichier"}), 200)
    file = request.files['file']
    if file.filename == '':
        return make_response(jsonify({'message':"Pas de fichier sélectionné"}), 200)
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.abspath(os.path.join(folder, filename))
        file.save(os.path.join(folder, filename))
        req = request.form
        #print(req)
        data = {
            "filename": filename,
            "filepath": filepath,
            "id_patient": req.get('id_patient'),
            "bon_assurance": req.get('bon_assurance'),
        }
        insert_db = Prescription.set_prescription(data)
        #print(insert_db)
        return make_response(jsonify({'path':filepath, 'insert': insert_db}), 201)
    


@patient.get('/list-pharmacy')
@token_required('users')
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
    