from dataclasses import dataclass
from pathlib import Path

from environs import Env


@dataclass
class Bots:
    """
    Дата класс для бота
    """

    bot_token: str


@dataclass
class Database:
    """
    Дата класс для базы данных
    """

    host_id: str
    db_name: str
    players_collection: str
    words_collection: str


@dataclass
class BotSettings:
    """
    Дата класс для создания настроек для бота
    """

    bots: Bots


def get_bot_settings(path: str) -> BotSettings:
    env = Env()
    env.read_env(path)

    return BotSettings(bots=Bots(bot_token=env.str("TELEBOT_API")))


def get_db_settings(path: str) -> Database:
    env = Env()
    env.read_env(path)

    return Database(
        host_id=env.str("HOST_ID"),
        db_name=env.str("DB_NAME"),
        players_collection=env.str("PLAYERS_COLLECTION"),
        words_collection=env.str("WORDS_COLLECTION"),
    )


TOKEN_PATH = Path(__file__).parent.parent.parent.resolve().joinpath("token")
bot_settings = get_bot_settings(TOKEN_PATH)

DATABASE_PATH = Path(__file__).parent.parent.parent.resolve().joinpath("db_info")
db_settings = get_db_settings(DATABASE_PATH)
