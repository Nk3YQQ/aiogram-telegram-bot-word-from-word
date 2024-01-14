class BasicWord:
    """
    Класс, содержащий поля: исходное слово
    и набор допустимых слов
    """

    def __init__(self, word: str, subwords: list) -> None:
        self.word = word
        self.subwords = subwords

    def check_word(self, user_input: str) -> bool:
        """
        Возвращает True, если слово есть в списке подслов
        или False, если слова нет в списке
        """
        return user_input in self.subwords

    def count_subwords(self) -> int:
        """
        Возвращает количество подслов
        в списке
        """
        return len(self.subwords)

    def __str__(self) -> str:
        return (
            f"Составьте {self.count_subwords()} слов из слова {self.word.upper()}. "
            f"Слова должны быть не короче {len(min(self.subwords, key=len))} букв"
        )
