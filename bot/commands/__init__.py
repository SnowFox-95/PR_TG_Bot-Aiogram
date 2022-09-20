__all__ = ['register_user_commands', 'bot_commands']

from aiogram import Router
from aiogram.filters import Command  # from aiogram.dispatcher.filters.command import CommandStart
from aiogram.filters.command import CommandStart

from aiogram import F
from bot.commands.help import help_cmd, help_func
from bot.commands.start import start
from bot.commands.bot_commands import bot_commands
from bot.commands.settings import setting_command


def register_user_commands(router: Router) -> None:
    # router.message.register(start, Command(commands=['start']))
    router.message.register(start, CommandStart())
    router.message.register(help_cmd, Command(commands=['help']))
    router.message.register(start, F.text == 'Старт')
    router.message.register(help_func, F.text == 'Помощь')
    router.message.register(setting_command, Command(commands=['settings']))
