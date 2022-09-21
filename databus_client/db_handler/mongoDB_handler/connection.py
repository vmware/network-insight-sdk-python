import os
from mongoengine import connect, disconnect


class MongoDBConnection(object):

    def __init__(self,
                 # server_url="localhost:27017",
                 server_url=None,
                 database_name="databus_client_data", alias='databus_client_data'):
        print("Received mongo server_url        : {}".format(server_url))
        server_url = server_url if server_url else os.getenv('MONGO_URI', server_url)
        print("Connected to mongo server_url    : {}".format(server_url))
        connect(alias=alias, host=server_url, db=database_name)

    def disconnect(self, alias='databus_client_data'):
        disconnect(alias=alias)
