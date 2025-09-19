"""
UserDAOMongo (Data Access Object for MongoDB)
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from models.user import User

class UserDAOMongo:
    def __init__(self):
        env_path = "../.env"
        load_dotenv(dotenv_path=env_path)
        db_host = os.getenv("MONGODB_HOST", "mongo")
        db_name = os.getenv("MONGODB_DB_NAME", "mydb")
        self.client = MongoClient(db_host)
        self.db = self.client[db_name]
        self.collection = self.db["users"]

    def select_all(self):
        """Select all users from MongoDB"""
        users = self.collection.find()
        return [User(str(u.get('_id')), u.get('name'), u.get('email')) for u in users]

    def insert(self, user):
        """Insert given user into MongoDB"""
        result = self.collection.insert_one({"name": user.name, "email": user.email})
        return str(result.inserted_id)

    def update(self, user):
        """Update given user in MongoDB"""
        self.collection.update_one(
            {"_id": self._to_objectid(user.id)},
            {"$set": {"name": user.name, "email": user.email}}
        )

    def delete(self, user_id):
        """Delete user from MongoDB with given user ID"""
        self.collection.delete_one({"_id": self._to_objectid(user_id)})

    def close(self):
        self.client.close()

    def _to_objectid(self, id_str):
        from bson import ObjectId
        try:
            return ObjectId(id_str)
        except Exception:
            return id_str
