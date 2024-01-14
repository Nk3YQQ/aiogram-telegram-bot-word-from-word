import pymongo


class MongoConnector:
    def __init__(self, host):
        self._host = host

    def connect_to_database(self):
        return pymongo.MongoClient(self._host)
