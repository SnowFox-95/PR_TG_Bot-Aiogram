from aiogram import types
from aiogram.utils.keyboard import (
    InlineKeyboardBuilder
)


async def setting_command(message: types.Message):
    setting_markup = InlineKeyboardBuilder()
    setting_markup.button(
        text='Яндекс',
        url='ya.ru'
    )
    setting_markup.button(
        text='Помощь',
        callback_data='help'
    )
    #region don't_working
    #setting_markup.button(
    #    text='Pay',
    #    pay=True
    #)
    #endregion

    await message.answer('Настройки', reply_markup=setting_markup.as_markup())
