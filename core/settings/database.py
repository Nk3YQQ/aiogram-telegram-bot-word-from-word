from core.settings import db_settings
from core.utils.for_handler import create_database

PLAYER_DATABASE = create_database(
    host_id=db_settings.host_id, db_name=db_settings.db_name, collection_name=db_settings.players_collection
)

WORD_DATABASE = create_database(
    host_id=db_settings.host_id, db_name=db_settings.db_name, collection_name=db_settings.words_collection
)
