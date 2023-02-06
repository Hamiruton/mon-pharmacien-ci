from src.config.db import db
from bson.objectid import ObjectId
from typing import List
from src.constants.complex_types import DICT_OF_STR


def get_on_call_pharmacy() -> List:
    phamacies = db.onCallPharmacy.find()
    list_pharma = []
    for pharma in phamacies:
        pharma['_id'] = str(pharma['_id'])
        list_pharma.append(pharma)
    
    return list_pharma


def set_on_call_pharmacy(name_state:str, list_pharmacy: List) -> None:
    db.onCallPharmacy.insert_one({
        "ville": name_state,
        "pharmacies": list_pharmacy
    })


class User:
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
        return f'<Patient {self.fullname}>'

    def register(self) -> None:
        db.users.insert_one(self.data)

    @staticmethod
    def get_user(id:str) -> DICT_OF_STR:
        user = db.users.find_one({"_id": ObjectId(id)})
        user['_id'] = str(user['_id'])
        return user
    
    @staticmethod
    def update_user(id:str, update_data:DICT_OF_STR) -> int:
        user = db.users.update_one(
            { "_id": ObjectId(id) },
            {
                "$set": update_data
            }
        )
        return user.modified_count