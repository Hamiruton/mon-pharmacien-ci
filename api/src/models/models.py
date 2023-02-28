"""Import module"""
import json
from typing import List
from bson.objectid import ObjectId
from src.config.db import get_database
from src.constants.complex_types import DICT_OF_STR

db = get_database()


def get_on_call_pharmacy() -> List:
    """
    Returns the list of on-call pharmacies and the related city
    """
    phamacies = db['onCallPharmacy'].find()
    list_pharma = []
    for pharma in phamacies:
        pharma['_id'] = str(pharma['_id'])
        list_pharma.append(pharma)

    return list_pharma


def set_on_call_pharmacy(name_state:str, list_pharmacy: List) -> None:
    """
    Insert in the "on-call pharmacy" collection, the list of on-call pharmacies and the related city
    """
    db['onCallPharmacy'].insert_one({
        "ville": name_state,
        "pharmacies": list_pharmacy
    })


class User:
    """
    In this class, methods which deal with patient data have been gathered
    """
    def __init__(self, data:DICT_OF_STR) -> None:
        self.data = {
            "fullname": data["fullname"],
            "birthday": data["birthday"],
            "sex": data["sex"],
            "email": data["email"],
            "phone": data["phone"],
            "town": data["town"],
            "password": data["password"],
            "constant": []
        }

    def __repr__(self) -> str:
        return f'<Patient {self.data["fullname"]}>'


    def register(self) -> None:
        """
        Register data in collection
        """
        db['users'].insert_one(self.data)

    @staticmethod
    def get_user(user_id:str) -> DICT_OF_STR:
        """
        Return user data according to their id
        """
        user = db['users'].find_one({"_id": ObjectId(user_id)})
        user['_id'] = str(user['_id'])
        return user

    @staticmethod
    def update_user(user_id:str, update_data:DICT_OF_STR) -> int:
        """
        Update user data according to their id
        """
        user = db['users'].update_one(
            { "_id": ObjectId(user_id) },
            {
                "$set": update_data
            }
        )
        return user.modified_count


class Pharmacy:
    """
    In this class, methods which deal with officine data have been gathered
    """
    def __init__(self, data:DICT_OF_STR) -> None:
        self.data = {
            "name": data["name"],
            "titulaire": data["titulaire"],
            "email": data["email"],
            "phone": data["phone"],
            "town": data["town"],
            "password": data["password"]
        }


    def create(self) -> any:
        """
        Register data in collection
        """
        insertion = db['officine'].insert_one(self.data)
        return insertion.acknowledged


    @staticmethod
    def update_user(officine_id:str, update_data:DICT_OF_STR) -> int:
        """
        Update officine data according to their id
        """
        officine = db['officine'].update_one(
            { "_id": ObjectId(officine_id) },
            {
                "$set": update_data
            }
        )
        return officine.modified_count
    
    
    @staticmethod
    def get_officine(officine_id:str) -> DICT_OF_STR:
        """
        Get officine data according to their id
        """
        officine = db['officine'].find_one({
            "_id": ObjectId(officine_id)
        })
        officine['_id'] = str(officine['_id'])
        del officine['password']
        return dict(officine)


class Drug:
    """
    In this class, methods which deal with drugs data have been gathered
    """
    @staticmethod
    def saveD(data:DICT_OF_STR, officine_id:str) -> bool:
        """
        Register drugs data in collection
        """
        officine_registered_same_drug = db.drugs.find_one({ # Query to find if officine has already registered this drug
            "nameMedoc": data['nameMedoc'],
            "affiliatedOf": {
                "$elemMatch": {
                    "idOf": ObjectId(officine_id)
                }
            }
        })

        drug_existed = db.drugs.find_one({
            "nameMedoc": data['nameMedoc']
        })

        if officine_registered_same_drug:
            return False
        elif drug_existed:
            insertion = db['drugs'].update_one(
                { "_id": drug_existed["_id"] },
                {
                    "$push": {
                        "affiliatedOf": {"idOf": ObjectId(officine_id), "qtyMedoc": data["qtyMedoc"]}
                    }
                }
            )
            return insertion.acknowledged
        else:
            insert_data = {
                "nameMedoc": data["nameMedoc"],
                "catMedoc": data["catMedoc"],
                "onPrescip": data["onPrescip"],
                # Spécifier les molécules du médicament
                "affiliatedOf": [
                    {
                        'idOf': ObjectId(officine_id),
                        'qtyMedoc': data["qtyMedoc"]
                    }
                ]
            }
            insertion = db['drugs'].insert_one(insert_data)
            return insertion.acknowledged


    @staticmethod
    def get_all_drugs() -> DICT_OF_STR:
        """
        Return all drugs data in collection
        """
        drugs = db['drugs'].find()
        list_drugs = []
        for drug in drugs:
            copy_drug = dict(drug)
            del copy_drug['affiliatedOf']
            drug_id = str(copy_drug['_id'])
            list_officine = Drug.get_officine_have_drugs(drug_id)
            copy_drug['_id'] = str(copy_drug['_id'])
            copy_drug['affiliatedOf'] = list_officine
            list_drugs.append(copy_drug)
        
        return list_drugs


    @staticmethod
    def get_all_drugs_by_officine(officine_id:str) -> any:
        """
        Return all drugs that an officine has by officine_id
        """
        drugs = db['drugs'].find({
            "affiliatedOf": {
                "$elemMatch": {
                    "idOf": ObjectId(officine_id)
                }
            }
        })
        list_drugs = []
        for drug in drugs:
            copy_drug = dict(drug)
            for elt in copy_drug['affiliatedOf']:
                if elt['idOf'] == ObjectId(officine_id):
                    qty = elt['qtyMedoc']
                    copy_drug['qty'] = qty
                    break
            del copy_drug['affiliatedOf']
            list_drugs.append(copy_drug)
        return list_drugs
    

    @staticmethod
    def get_drug_by_officine(officine_id:str, drug_id: str) -> any:
        """
        Return one drug data in collection for officine
        """
        drug = db['drugs'].find_one({
            "_id": ObjectId(drug_id),
            "affiliatedOf": {
                "$elemMatch": {
                    "idOf": ObjectId(officine_id)
                }
            }
        })

        if not drug:
            return False
        else:
            for elt in drug['affiliatedOf']:
                if elt['idOf'] == ObjectId(officine_id):
                    qty = elt['qtyMedoc']
                    drug['qty'] = qty
                    break
            del drug['affiliatedOf']
            drug['_id'] = str(drug['_id'])
            return drug
        
    
    @staticmethod
    def get_officine_have_drugs(drug_id:str) -> DICT_OF_STR:
        """
        Return all officines that have at least one quantity of the drug corresponding to the drug id
        """
        drug = db['drugs'].find_one({
            "_id": ObjectId(drug_id)
        })
        
        list_officine = []
        for officine in drug['affiliatedOf']:
            if officine['qtyMedoc'] > 0:
                res_of = db['officine'].find_one({"_id": officine['idOf']})
                res_of['_id'] = str(res_of['_id'])
                del res_of['password']
                list_officine.append(res_of)
        
        return list_officine