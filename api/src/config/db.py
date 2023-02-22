from pymongo import MongoClient
import os

def get_database():
    CONNECTION_STRING = os.getenv('FLASK_MONGO_URI')
    
    client = MongoClient(CONNECTION_STRING)
    db = client['pi2023db']

    if len(client.list_database_names()):
        print('DB up')
        return db


if __name__ == "__main__":
    get_database()