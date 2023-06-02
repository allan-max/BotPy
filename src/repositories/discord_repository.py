from src.models.db.mongodb import ConnectionMongo
from bson import ObjectId

class logsrepository:

    def __init__(self):
        self.repositorie = ConnectionMongo(
            database_name="discord-bot",
            collection_name="users-controll",
        ).get_collection_name()
    

    def add_user(self, user):
        self.repositorie.insert_many([user])
    
    def remove_user(self, user):
        self.repositorie.delete_one({'_id': user}) 
    
    def find_user_id(self, id):
        
        response_user_exists = self.repositorie.find_one({'_id': id})

        if response_user_exists:
            return True
    
        return False
        
    
    def find_all_user_id(self, id):
        
        response_users = []
        response_user_exists = self.repositorie.find_one({'ids': id})


        if response_user_exists:
            for user in self.repositorie.find({'ids': id}):
                response_users.append({
                    "_id" : user['_id'],
                    "ids" : user['ids'],
                    "message_user" : user['message_user'],
                    "author_name" : user['author_name'],
                    "guild_id" : user['guild_id'],
                    "log_type" : user['log_type'],
                    "mute_time" : user['mute_time']
                })
            
            return response_users
        
        return False
    
    def find_all_guild_id(self, id):
        
        response_users = []
        response_user_exists = self.repositorie.find_one({'guild_id': id})


        if response_user_exists:
            for user in self.repositorie.find({'guild_id': id}):
                response_users.append({
                    "ids" : user['ids'],
                    "message_user" : user['message_user'],
                    "author_name" : user['author_name'],
                    "guild_id" : user['guild_id'],
                    "log_type" : user['log_type'],
                    "mute_time" : user['mute_time']
                })
            
            return response_users
        
        return False

class reportrepository:
    
    def __init__(self):
        self.repositorie = ConnectionMongo(
            database_name="discord-bot",
            collection_name="report-repository",
        ).get_collection_name()
        
    def add_user(self, user):
        self.repositorie.insert_many([user])
    
    def remove_user(self, user):
        self.repositorie.delete_one()
    
    def find_channel_member(self, id):
        
        response_users = []
        response_user_exists = self.repositorie.find_one({'channel_member': id})

        if response_user_exists:
            for user in self.repositorie.find({'channel_member': id}):
                response_users.append({
                    "channel_staff": user['channel_staff'],
                    "channel_member": user['channel_member'],
                    "guild_id": user['guild_id'],
                    "cargo": user['cargo']
                })
            
            return response_users
        
        return False
    
    def find_user_id(self, id):
        
        response_user_exists = self.repositorie.find_one({'_id': id})

        if response_user_exists:
            return True
    
        return False
        
class roledef:

    def __init__(self):
        self.repositorie = ConnectionMongo(
            database_name="discord-bot",
            collection_name="roles",
        ).get_collection_name()
    
    def add_user(self, user):
        self.repositorie.insert_many([user])
    
    def remove_user(self, user):
        self.repositorie.delete_one({'_id': user})

    def find_role(self, id):
        
        response_user_exists = self.repositorie.find_one({'role': id})

        if response_user_exists:
            return True
        
        return False
  
    def find_guild_role(self, id):
        
        response_users = []
        response_user_exists = self.repositorie.find_one({'guild_id': id})


        if response_user_exists:
            for user in self.repositorie.find({'guild_id': id}):
                response_users.append({
                    "guild_id": user['guild_id'],
                    "role": user['role'],
                    "_id": user['_id'],
                    "author": user['author']
                })
            
            return response_users
        
        return False
    
    def find_user_id(self, id):
        
        response_user_exists = self.repositorie.find_one({'_id': id})

        if response_user_exists:
            return True
        
        return False
        
