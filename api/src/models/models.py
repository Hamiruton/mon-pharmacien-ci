"""Import module"""
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
