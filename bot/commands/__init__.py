__all__ = ['register_user_commands', 'bot_commands']


from aiogram import Router
from aiogram.filters import Command
# region bugs aiogram 3.x.b2
# from aiogram.dispatcher.filters.command import CommandStart
# endregion
from aiogram.filters.command import CommandStart

from aiogram import F
from bot.commands.help import help_cmd, help_func, call_help_func, clear_call_help_func
from bot.commands.start import start
from bot.commands.bot_commands import bot_commands
from bot.commands.settings import setting_command, setting_callback
from bot.commands.callback_data_states import TestCallbackData
from bot.middlewares.register_check import RegisterCheck

def register_user_commands(router: Router) -> None:
    # region message_register
    # router.message.register(start, Command(commands=['start']))
    router.message.register(start, CommandStart())
    router.message.register(help_cmd, Command(commands=['help']))
    router.message.register(start, F.text == 'Старт')
    router.message.register(help_func, F.text == 'Помощь')
    router.message.register(setting_command, Command(commands=['settings']))
    # endregion

    # region callback_register
    router.callback_query.register(call_help_func, F.data == 'help')
    router.callback_query.register(clear_call_help_func, F.data == 'clear')
    router.callback_query.register(setting_callback, TestCallbackData.filter())
    # endregion

    router.message.register(RegisterCheck)
    router.callback_query.register(RegisterCheck)