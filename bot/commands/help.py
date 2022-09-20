from aiogram import types
from aiogram.filters import CommandObject

# region Unused import
# from aiogram.utils.keyboard import InlineKeyboardButton
# endregion

from bot.commands.bot_commands import bot_commands


async def help_cmd(message: types.Message, command: CommandObject):
    if command.args:
        for cmd in bot_commands:
            if cmd[0] == command.args:
                return await message.answer(
                    f"{cmd[0]} - {cmd[1]}\n\n{cmd[2]}"
                )
        else:
            return await message.answer('Команда не найдена')

    return help_func(message)


async def help_func(message: types.Message):
    return await message.answer(
        'Помощь и справка о боте \n'
        'Для того, чтобы получить информацию о команде используй /help <команда>'
    )


# region callback from answer message
#   async def call_help_func(call: types.CallbackQuery):
#       return await message.answer(
#           'Помощь и справка о боте \n'
#           'Для того, чтобы получить информацию о команде используй /help <команда>'
#       )
# endregion

# region callback from edit message
async def call_help_func(call: types.CallbackQuery):
    return await call.message.edit_text(
        'Помощь и справка о боте \n'
        'Для того, чтобы получить информацию о команде используй /help <команда>'
        # region don't_working
        # ,
        #
        # reply_markup=call.message.reply_markup.inline_keyboard.append(
        #    [InlineKeyboardButton(text='Назад', callback_data='clear')])
        # endregion
    )


# endregion

# region callback clear_help_func
async def clear_call_help_func(call: types.CallbackQuery):
    await call.message.edit_text(
        'Помощь и справка о боте \n'
        'Для того, чтобы получить информацию о команде используй /help <команда>'
    )
# endregion
