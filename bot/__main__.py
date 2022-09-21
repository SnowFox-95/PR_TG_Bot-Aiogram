import os
import asyncio
import logging
from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
from sqlalchemy.engine import URL

from commands import register_user_commands
from commands.bot_commands import bot_commands

from db import baseModel, create_async_engine, get_session_maker, proceed_schemas
from bot.middlewares.register_check import RegisterCheck

async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    command_for_bot = []
    for cmd in bot_commands:
        command_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))

    dp = Dispatcher()
    dp.message.middleware(RegisterCheck)
    dp.callback_query.middleware(RegisterCheck)

    bot = Bot(token=os.getenv('token'))
    await bot.set_my_commands(commands=command_for_bot)

    register_user_commands(dp)

    postgres_url = URL.create(
        "posgresql+asyncpg",
        username=os.getenv("db_user"),
        host="localhost",
        database=os.getenv("db_name"),
        port=os.getenv('db_port'),
    )

    async_engine = create_async_engine(postgres_url)
    session_maker = get_session_maker(async_engine)
    await proceed_schemas(async_engine, baseModel.metadata)
    await dp.start_polling(bot, session_maker=session_maker)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
