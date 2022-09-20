__all__ = ['register_user_commands']

from aiogram import Router
# from aiogram.dispatcher.filters.command import CommandStart
from aiogram.filters.command import CommandStart

from bot.commands.start import start


def register_user_commands(router: Router) -> None:
    # router.message.register(start, Command(commands=['start']))
    router.message.register(start, CommandStart())
