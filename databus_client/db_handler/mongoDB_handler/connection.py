import os
from mongoengine import connect, disconnect
from pymongo import MongoClient


class MongoDBConnection(object):

    def __init__(self,
                 server_url=None,
                 database_name=None, alias=None):
        print("Received mongo server_url                    : {}".format(server_url))
        server_url = server_url if server_url else os.getenv('MONGO_URI', server_url)
        print("Checking connection with mongo server_url    : {}".format(server_url))
        connection = connect(alias=alias, host=server_url, db=database_name)
        self.checkconnection(connection, database_name=database_name)
        print("Connected to mongo server_url                : {}".format(server_url))

    def checkconnection(self, connection=None, database_name=None):
        connection.find.client.get_database(name=database_name).list_collections()

    def disconnect(self, alias='databus_client_data'):
        disconnect(alias=alias)
