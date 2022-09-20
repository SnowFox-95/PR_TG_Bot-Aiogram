__all__ = ['register_user_commands', 'bot_commands']

from aiogram import Router
# from aiogram.dispatcher.filters.command import CommandStart
from aiogram.filters import Command
from aiogram.filters.command import CommandStart
from aiogram import F
from bot.commands.help import help_cmd
from bot.commands.start import start
from bot.commands.bot_commands import bot_commands


def register_user_commands(router: Router) -> None:
    # router.message.register(start, Command(commands=['start']))
    router.message.register(start, CommandStart())
    router.message.register(help_cmd, Command(commands=['help']))
    router.message.register(start, F.text == 'Старт')
