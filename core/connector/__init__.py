import pymongo


class MongoConnector:
    """
    Класс позволяет подключиться к базе данных MongoDB
    """

    def __init__(self, host_id: str):
        self._host_id = host_id

    def connect_to_database(self) -> pymongo.MongoClient:
        """
        Метод создаёт экземпляр подключения к базе данных
        """
        return pymongo.MongoClient(self._host_id)
