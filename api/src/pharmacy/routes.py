""" Import module """
from flask import request, jsonify
from src.pharmacy import pharmacy
from src.models.models import Pharmacy, Drug


@pharmacy.post('/')
def register_officine():
    """
    Route for registering a pharmacy
    """
    data = request.get_json()
    officine = Pharmacy(data)
    res = officine.create()
    print(res)
    return "res"


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
    res = Drug.get_all_by_officine(idOfficine)
    print(res)
    return "jsonify(res)"