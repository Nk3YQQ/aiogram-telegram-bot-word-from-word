from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from core.connector import MongoConnector
from core.database import Database


def create_panel(*bottoms):
    list_of_bottom = []
    for bottom_name in bottoms:
        bottom = KeyboardButton(text=bottom_name)
        list_of_bottom.append(bottom)

    return ReplyKeyboardMarkup(keyboard=[list_of_bottom], resize_keyboard=True)


def create_database(host_id, db_name, collection_name):
    mongo = MongoConnector(host=host_id)
    con = mongo.connect_to_database()
    return Database(connection=con, db_name=db_name, collection_name=collection_name)
