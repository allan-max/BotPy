from pymongo import MongoClient
from src.config import ConfigurationDB


class ConnectionMongo:
   
    def __init__(self, database_name, collection_name):
        self.client = MongoClient(ConfigurationDB.connection_string)
        self.database = database_name
        self.collection = collection_name

    def get_database(self):
        return self.client[self.database]
    
    def get_collection_name(self):
        return self.get_database()[self.collection]

