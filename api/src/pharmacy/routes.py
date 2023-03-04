""" Import module """
from flask import request, jsonify, make_response
from src.pharmacy import pharmacy
from src.models.models import Pharmacy, Drug, Molecule, Prescription
from src.auth import token_required


@pharmacy.post('/')
@pharmacy.post('/register')
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
@token_required('officine')
def get_officine(idOfficine):
    """
    Route for returning informations about a pharmacy
    """
    res = Pharmacy.get_officine(idOfficine)
    return jsonify(res)

@pharmacy.post('/<idOfficine>/register-medoc')
@token_required('officine')
def register_drugs(idOfficine):
    """
    Route for registering a drug in a pharmacy
    """
    data = request.get_json()
    drugs = Drug()
    res = drugs.saveD(data, idOfficine)
    if res == False:
        return make_response({"message": "Impossible, vous avez déjà enregistré ce médicament"}, 200)
    else:
        return make_response({"data": res}, 201)


@pharmacy.get('/<idOfficine>/get-all')
@token_required('officine')
def get_all_drugs(idOfficine):
    """
    Route for returning all drugs in a pharmacy
    """
    res = Drug.get_all_drugs_by_officine(idOfficine)
    if res == False:
        return make_response(jsonify({"message": "Aucun médicament en stock"}), 200)
    return make_response(jsonify({"data": res}), 200)


@pharmacy.get('/<idOfficine>/<idMedoc>')
@token_required('officine')
def get_one_drug(idOfficine, idMedoc):
    """
    Route for returning a particular drug in a pharmacy
    """
    res = Drug.get_drug_by_officine(idOfficine, idMedoc)
    if res == False:
        return make_response(jsonify({"message": "Impossible, ce médicament n'existe pas dans votre stock"}), 404)
    else:
        return make_response(jsonify({"data": res}), 200)
    

@pharmacy.get('/stock/<idOfficine>')
@token_required('officine')
def get_one_cat_drugs(idOfficine):
    """
    Route for returning all drugs categories an officine has
    """
    res = Drug.get_cat_drugs_by_officine(idOfficine)
    if res == False:
        return make_response(jsonify({"message": "Impossible, Vous n'avez pas de stock"}), 404)
    else:
        return make_response(jsonify({"data": res}), 200)
    

@pharmacy.get('/molecules/get-all')
def get_all_mol():
    """
    Route for returning all molecules in db
    """
    res = Molecule.get_all_mol()
    if res == False:
        return make_response(jsonify({"message": "Il n'existe aucune molécule enregistrée"}), 404)
    else:
        return make_response(jsonify({"data": res}), 200)
    

@pharmacy.get('/stock/<idOfficine>/<categName>')
def get_all_drugs_by_categ(idOfficine, categName):
    """
    Route for returning all drugs according to drugs categories
    """
    res = Drug.get_drugs_by_cat_drugs_for_officine(idOfficine, categName)
    if res == False:
        return make_response(jsonify({"message": f"Il n'existe aucune médicament enregistrée dans {categName}"}), 404)
    else:
        return make_response(jsonify({"data": res}), 200)
    

@pharmacy.get('/categDrugs/get-all')
def get_all_cat_drugs():
    """
    Route for returning all drugs according to drugs categories
    """
    res = Drug.get_all_cat_drugs()
    if res == False:
        return make_response(jsonify({"message": f"Pas de catégorie"}), 404)
    else:
        return make_response(jsonify({"data": res}), 200)
    

@pharmacy.get('/molecule/<idMol>')
def get_mol_by_id(idMol):
    """
    Route for returning a name of molecule by its id
    """
    res = Molecule.get_name_mol_by_id(idMol)
    if res == False:
        return make_response(jsonify({"message": f"Non trouvé"}), 200)
    else:
        return make_response(jsonify({"data": res}), 200)
    

@pharmacy.get('/prescription/get-all')
def get_all_prescription():
    """
    Route for ...
    """
    res = Prescription.get_all_prescription()
    #"print(res)
    return make_response(jsonify({"data": res}), 200)
    

