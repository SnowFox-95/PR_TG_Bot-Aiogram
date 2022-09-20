from aiogram import types
from aiogram.utils.keyboard import (
    InlineKeyboardBuilder
)
from bot.commands.callback_data_states import TestCallbackData


async def setting_command(message: types.Message):
    setting_markup = InlineKeyboardBuilder()
    setting_markup.button(
        text='Яндекс',
        url='ya.ru'
    )
    setting_markup.button(
        text='Помощь',
        callback_data=TestCallbackData(text='Привет', user_id=message.from_user.id)
    )
    # region don't_working
    # setting_markup.button(
    #    text='Pay',
    #    pay=True
    # )
    # endregion

    await message.answer('Настройки', reply_markup=setting_markup.as_markup())


async def setting_callback(call: types.CallbackQuery, callback_data: TestCallbackData):
    await call.message.answer(callback_data.text + ', ' + str(callback_data.user_id))
