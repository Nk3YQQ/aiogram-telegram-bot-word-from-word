from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup

from core.connector import MongoConnector
from core.database import Database
from core.game import Game


def create_game(database: Database) -> Game:
    """
    Функция для создания экземпляра игры
    """
    return Game(database)


def create_panel(*bottoms: str) -> ReplyKeyboardMarkup:
    """
    Функция для создания панели для пользователя
    """
    list_of_bottom = []
    for bottom_name in bottoms:
        bottom = KeyboardButton(text=bottom_name)
        list_of_bottom.append(bottom)

    return ReplyKeyboardMarkup(keyboard=[list_of_bottom], resize_keyboard=True)


def create_database(host_id: str, db_name: str, collection_name: str) -> Database:
    """
    Функция для создания экземпляра базы данных
    """
    mongo = MongoConnector(host_id)
    con = mongo.connect_to_database()
    return Database(connection=con, db_name=db_name, collection_name=collection_name)


async def check_player_word(
    message: Message,
    database: Database,
    menu_bottoms: ReplyKeyboardMarkup,
    player_words: list,
    player_name: str,
    user_game: Game,
    player_states: dict,
    game: Game,
) -> None:
    """
    Функция для проверки введённых пользователем слов
    """
    if len(player_words) == len(user_game.word_info.subwords):
        await message.answer("Вы угадали все слова. Игра завершена!", reply_markup=menu_bottoms)
        database.add_score(player_name, len(player_words))
        player_words.clear()
        player_states[message.from_user.id] = game
        return

    user_word = message.text.lower()

    if message.text == "Стоп":
        await message.answer("Останавливаю игру.", reply_markup=menu_bottoms)
        database.add_score(player_name, len(player_words))
        player_words.clear()
        player_states[message.from_user.id] = game
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
