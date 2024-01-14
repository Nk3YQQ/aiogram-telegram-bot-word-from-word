class Player:
    """
    Класс, содержащий поля: имя пользователя
    и использованные слова пользователя
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.user_words = []
        self._player_states = {}
        self._player_info = {}

    def count_user_words(self) -> int:
        """
        Возвращает количество использованных
        слов пользователем
        """
        return len(self.user_words)

    def append_to_user_words(self, user_word: str) -> None:
        """
        Добавляет использованные слова
        пользователем в user_words
        """
        self.user_words.append(user_word)

    def check_user_word(self, user_word: str) -> bool:
        """
        Проверяет, использовалось ли слово,
        введённое пользользователем до этого
        """
        return user_word in self.user_words

    def __str__(self) -> str:
        return f"Имя пользователя: {self.name}. Использованные слова пользователя: " f"{', '.join(self.user_words)}"
