import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

from core.handler import GameHandler
from core.settings import bot_settings


async def start():
    """
    Функция включает бота
    """
    bot = Bot(token=bot_settings.bots.bot_token)
    game = GameHandler()
    dp = Dispatcher()

    dp.message.register(game.start, Command(commands=["start"]))
    dp.message.register(game.menu, F.text == "Меню")
    dp.message.register(game.run, F.text == "Начать игру")
    dp.message.register(game.help_info, F.text == "Помощь")
    dp.message.register(game.max_result, F.text == "Максимальный результат")
    dp.message.register(game.check_player_word, F)
    try:
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
