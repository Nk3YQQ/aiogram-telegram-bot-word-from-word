from aiogram.types import Message

from core.game import Game
from core.player import Player
from core.utils.for_handler import create_database, create_panel

menu_bottoms = create_panel("Начать игру", "Помощь", "Максимальный результат")
game_bottoms = create_panel("Стоп")
update_bottom = create_panel("Меню")


class GameHandler:
    def __init__(self):
        self._player_states = {}
        self._player_info = {}

    async def _check_player_in_session(self, message, game):
        user_id = message.from_user.id
        if user_id not in self._player_states:
            player = Player(message.from_user.username)
            self._player_info[player.name] = player.user_words
            self._player_states[user_id] = game

        await message.answer("Перемещаю в меню.", reply_markup=menu_bottoms, one_time_keyboard=True)

    @staticmethod
    async def start(message: Message):
        await message.answer(
            f"Привет {message.from_user.username}!", reply_markup=menu_bottoms, one_time_keyboard=True
        )

    async def menu(self, message: Message):
        game = Game()
        await self._check_player_in_session(message, game)

    async def run(self, message: Message):
        user_id = message.from_user.id
        if user_id not in self._player_states:
            await message.answer("Возвратитесь в меню, чтобы мы очистили кэш🙂", reply_markup=update_bottom)
            return

        user_game = self._player_states[user_id]
        await message.answer("Давай преступим к игре.")
        await message.answer(str(user_game.word_info), reply_markup=game_bottoms)

    async def check_player_word(self, message: Message):
        database = create_database(
            host_id="mongodb://localhost:27017", db_name="word_from_word", collection_name="players_scores"
        )
        user_id = message.from_user.id
        if user_id not in self._player_states:
            await message.answer("Возвратитесь в меню.", reply_markup=update_bottom)
            return

        user_game = self._player_states[user_id]
        player_name = message.from_user.username
        player_words = self._player_info[player_name]

        if len(player_words) == len(user_game.word_info.subwords):
            await message.answer("Вы угадали все слова. Игра завершена!", reply_markup=menu_bottoms)
            database.add_score(player_name, len(player_words))
            player_words.clear()
            self._player_states[user_id] = Game()
            return

        user_word = message.text.lower()

        if message.text == "Стоп":
            await message.answer("Останавливаю игру.", reply_markup=menu_bottoms)
            database.add_score(player_name, len(player_words))
            player_words.clear()
            self._player_states[user_id] = Game()
            return

        if user_word in player_words:
            await message.answer("Это слово уже использовано. Попробуйте другое.")
        elif len(user_word) < len(min(user_game.word_info.subwords, key=len)):
            await message.answer("Слишком короткое слово. Попробуйте другое.")
        elif user_game.word_info.check_word(user_word):
            player_words.append(message.text)
            await message.answer(f"Верно! Количество угаданных слов - {len(player_words)}.")
        else:
            await message.answer("Неверно. Попробуйте другое слово.")

    @staticmethod
    async def help_info(message: Message):
        await message.answer(
            'Для того, чтобы начать игру, нужно нажать на кнопку "Начать игру". Правила игры простые - Вам нужно '
            "будет угадать как можно больше слов. Если Вам надоест угадывать слова, то Вы можете начать на кнопку "
            '"Стоп", и Ваш результат сохранится. Для того, чтобы посмотреть Ваш максимальный результат, нажмите на '
            'кнопку "Максимальный результат".'
        )

    @staticmethod
    async def max_result(message: Message):
        database = create_database(
            host_id="mongodb://localhost:27017", db_name="word_from_word", collection_name="players_scores"
        )
        await message.answer(f"Ваш максимальный результат: {database.get_max_result(message.from_user.username)}.")
