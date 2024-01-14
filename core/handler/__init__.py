from aiogram.types import Message

from core.settings.bottoms import GAME_BOTTOMS, MENU_BOTTOMS
from core.settings.database import PLAYER_DATABASE, WORD_DATABASE
from core.utils.for_handler import check_player_word, create_session, create_game


class GameHandler:
    """
    Класс является прототипом обработчиков для телеграмм бота
    """

    def __init__(self):
        self._player_states: dict = {}
        self._player_info: dict = {}

    @staticmethod
    async def start(message: Message):
        """
        Метод отправляет приветственные слова пользователю
        """
        await message.answer(
            f"Привет {message.from_user.username}!", reply_markup=MENU_BOTTOMS, one_time_keyboard=True
        )

    async def menu(self, message: Message):
        """
        Метод создаёт интерфейс меню
        """
        game = create_game(database=WORD_DATABASE)
        await create_session(message, self._player_info, self._player_states, game, MENU_BOTTOMS)

    async def run(self, message: Message):
        """
        Метод запускает игру для пользователя
        """
        game = create_game(database=WORD_DATABASE)
        await create_session(message, self._player_info, self._player_states, game, MENU_BOTTOMS)
        user_game = self._player_states[message.from_user.id]
        await message.answer(str(user_game.word_info), reply_markup=GAME_BOTTOMS)

    async def check_player_word(self, message: Message):
        """
        Метод проверяет слова пользователя
        """
        game = create_game(database=WORD_DATABASE)
        await create_session(message, self._player_info, self._player_states, game)
        user_game = self._player_states[message.from_user.id]
        player_name = message.from_user.username
        player_words = self._player_info[player_name]

        await check_player_word(
            message, PLAYER_DATABASE, MENU_BOTTOMS, player_words, player_name, user_game, self._player_states, game
        )

    @staticmethod
    async def help_info(message: Message):
        """
        Метод позволяет пользователю получить подсказку для пользователя
        """
        await message.answer(
            'Для того, чтобы начать игру, нужно нажать на кнопку "Начать игру". Правила игры простые - Вам нужно '
            "будет угадать как можно больше слов. Если Вам надоест угадывать слова, то Вы можете начать на кнопку "
            '"Стоп", и Ваш результат сохранится. Для того, чтобы посмотреть Ваш максимальный результат, нажмите на '
            'кнопку "Максимальный результат".'
        )

    @staticmethod
    async def max_result(message: Message):
        """
        Метод позволяет пользователю получить максимальный результат
        """
        await message.answer(
            f"Ваш максимальный результат: {PLAYER_DATABASE.get_max_result(message.from_user.username)}."
        )
