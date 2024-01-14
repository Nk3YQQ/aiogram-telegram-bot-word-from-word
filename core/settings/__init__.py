from dataclasses import dataclass
from pathlib import Path

from environs import Env


@dataclass
class Bots:
    bot_token: str


@dataclass
class Settings:
    bots: Bots


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(bots=Bots(bot_token=env.str("TELEBOT_API")))


TOKEN_PATH = Path(__file__).parent.parent.parent.resolve().joinpath("token")

settings = get_settings(TOKEN_PATH)

JSON_PATH = Path(__file__).parent.parent.resolve().joinpath("data", "results.json")
