from aiogram.types import Message, ReplyKeyboardMarkup

from core.game import Game
from core.player import Player


class Session:
    """
    Класс для создания сессии для пользователя
    """

    def __init__(self, message: Message, players_info: dict, players_state: dict):
        self._message = message
        self._players_info = players_info
        self._players_state = players_state

    def check_player(self) -> bool:
        """
        Метод проверяет, находится ли пользователь в сессии или нет
        """
        if self._message.from_user.id not in self._players_state:
            return False
        return True

    async def add_player(self, game: Game, menu_panel: ReplyKeyboardMarkup | None = None):
        """
        Метод добавляет пользователя в сессию
        """
        player = Player(self._message.from_user.username)
        self._players_info[player.name] = player.user_words
        self._players_state[self._message.from_user.id] = game
        if not menu_panel:
            await self._message.answer("Ваша сессия создана.")
        else:
            await self._message.answer("Давайте преступим к игре.", reply_markup=menu_panel, one_time_keyboard=True)
