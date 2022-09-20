from aiogram import types
from aiogram.utils.keyboard import (
    ReplyKeyboardBuilder, ReplyKeyboardMarkup, InlineKeyboardBuilder, InlineKeyboardMarkup, KeyboardButton,
    InlineKeyboardButton, KeyboardButtonPollType
)


async def start(message: types.Message) -> None:
    menu_bulder = ReplyKeyboardBuilder()
    menu_bulder.button(
        text='Помощь'
    )
    menu_bulder.add(
        KeyboardButton(text='Отправить контакт', request_contact=True)
    )
    menu_bulder.row(
        KeyboardButton(text='Отправить голосование', request_poll=KeyboardButtonPollType())
    )
    await message.answer(
        'Меню',
        reply_markup=menu_bulder.as_markup()
    )
