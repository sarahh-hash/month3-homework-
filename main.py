import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from config import bot, dp
from handlers import commands, echo, form
from database import db


async def set_commands():
    commands_list = [
        BotCommand(command="start", description="Старт бота"),
        BotCommand(command="help", description="Помощь"),
        BotCommand(command="mem", description="Мем"),
        BotCommand(command="sticker", description="Стикер"),
        BotCommand(command="form", description="Заказать пиццу"),
        BotCommand(command="cancel", description="Отменить анкету"),
    ]

    await bot.set_my_commands(commands_list)


async def main():
    logging.basicConfig(level=logging.INFO)

    # Создаём таблицы
    await db.init_db()

    # Команды бота
    await set_commands()

    # Подключаем handlers
    dp.include_router(commands.router_commands)
    dp.include_router(form.router_form)
    dp.include_router(echo.router_echo)

    # Запускаем бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())