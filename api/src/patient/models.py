from src.config.db import db
from bson.objectid import ObjectId
from typing import Dict

json_info = Dict[str, str]

def id_to_str(id:bytes) -> str:
    pass


class User:
    def __init__(self, data:json_info) -> None:
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
    def get_user(id:str) -> json_info:
        user = db.users.find_one({"_id": ObjectId(id)})
        user['_id'] = str(user['_id'])
        return user
