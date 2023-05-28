import os

class ConfigurationDB:
    username = os.getenv('MONGOUSERNAME')
    password = os.getenv('MONGOPASSWORD')
    connection_string = f"mongodb+srv://{username}:{password}@cluster0.x1qe3pl.mongodb.net/"


class ConfigurationAPIDiscord:
    token = os.getenv('TOKEN')

