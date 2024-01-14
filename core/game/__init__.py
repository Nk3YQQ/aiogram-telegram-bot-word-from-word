from random import shuffle as shuffle_words

from core.basicword import BasicWord
from core.database import Database


class Game:
    """
    Класс является прототипом для создания игры
    """

    def __init__(self, word_database: Database):
        self.word_info: BasicWord = self.load_random_word(word_database)

    @staticmethod
    def load_random_word(word_database: Database) -> BasicWord:
        """
        Функция получает список слов с "jsonkeeper.com",
        выбирает случайное слово, создаёт экземпляр класса
        BasicWord и возвращает данный экземпляр
        """
        words_list = list(word_database.get_words())
        shuffle_words(words_list)
        dict_word = words_list[0]["word"]
        dict_subwords = words_list[0]["subwords"]
        word = BasicWord(dict_word, dict_subwords)
        return word
