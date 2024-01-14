from random import shuffle as shuffle_words

from core.basicword import BasicWord
from core.utils.for_handler import create_database


class Game:
    def __init__(self):
        self.word_info = self.load_random_word()

    @staticmethod
    def load_random_word() -> BasicWord:
        """
        Функция получает список слов с "jsonkeeper.com",
        выбирает случайное слово, создаёт экземпляр класса
        BasicWord и возвращает данный экземпляр
        """
        database = create_database(
            host_id="mongodb://localhost:27017", db_name="word_from_word", collection_name="words"
        )
        words_list = list(database.get_words())
        shuffle_words(words_list)
        dict_word = words_list[0]["word"]
        dict_subwords = words_list[0]["subwords"]
        word = BasicWord(dict_word, dict_subwords)
        return word
