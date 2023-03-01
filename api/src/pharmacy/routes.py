""" Import module """
from flask import request, jsonify, make_response
from src.pharmacy import pharmacy
from src.models.models import Pharmacy, Drug


@pharmacy.post('/')
def register_officine() -> any:
    """
    Route for registering a pharmacy
    """
    data = request.get_json()
    officine = Pharmacy(data)
    res = officine.create()
    if res == False:
        return make_response(jsonify({"message":"Veuillez entrer un autre nom ou email"}), 200)
    
    return make_response(jsonify({"message":res}), 201)


@pharmacy.post('/login')
def login() -> any:
    """
    Route to login user
    """
    data = request.get_json()
    res = Pharmacy.login(data)
    if res == "incorrect email":
        return make_response(jsonify({"message":res}), 200)
    elif res == "incorrect password":
        return make_response(jsonify({"message":res}), 200)
    else:
        return make_response(jsonify({"data": res}), 201)


@pharmacy.get('/<idOfficine>')
def get_officine(idOfficine):
    """
    Route for returning informations about a pharmacy
    """
    res = Pharmacy.get_officine(idOfficine)
    return jsonify(res)

@pharmacy.post('/<idOfficine>/register-medoc')
def register_drugs(idOfficine):
    """
    Route for registering a drug in a pharmacy
    """
    data = request.get_json()
    drugs = Drug()
    res = drugs.saveD(data, idOfficine)
    if res == False:
        return "Impossible, vous avez déjà enregistré ce médicament"
    else:
        return jsonify(res)


@pharmacy.get('/<idOfficine>/get-all')
def get_all_drugs(idOfficine):
    """
    Route for returning all drugs in a pharmacy
    """
    res = Drug.get_all_drugs_by_officine(idOfficine)
    print(res)
    return "jsonify(res)"


@pharmacy.get('/<idOfficine>/<idMedoc>')
def get_one_drug(idOfficine, idMedoc):
    """
    Route for returning a particular drug in a pharmacy
    """
    res = Drug.get_drug_by_officine(idOfficine, idMedoc)
    if res == False:
        return "Impossible, ce médicament n'existe pas dans votre stock"
    else:
        return res
    