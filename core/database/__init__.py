class Database:
    """
    Класс позволяет работать с базами данных пользователей и слов
    """

    def __init__(self, connection, db_name, collection_name):
        self._db = connection[db_name]
        self._collection = self._db[collection_name]

    def _create_new_player(self, player_name, score):
        """
        Метод создаёт нового пользователя (не использовать его)
        """
        new_player = {"name": player_name, "score": [score]}
        self._db.players_scores.insert_one(new_player)

    def _insert_data_to_player(self, player_name, score):
        """
        Метод добавляет пользователя в базу данных (не использовать его)
        """
        self._collection.update_one({"name": player_name}, {"$push": {"score": score}})

    def add_score(self, player_name, score):
        """
        Метод добавляет пользователя и его результат в базу данных
        """
        player_exists = False
        current_player = list(self._collection.find({"name": player_name}))
        if current_player:
            self._insert_data_to_player(player_name, score)
            player_exists = True
        if not player_exists:
            self._create_new_player(player_name, score)

    def get_max_result(self, player_name):
        """
        Метод позволяет получить результат у пользователя
        """
        current_player = list(self._collection.find({"name": player_name}))
        if not current_player:
            return "Упс. Похоже Вы ещё не сыграли ни одно игры :("
        return max(current_player[0]["score"])

    def get_words(self):
        """
        Метод позволяет получить слова из базы данных слов
        """
        return self._collection.find()
