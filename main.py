
import asyncio
import logging

from aiogram.types import BotCommand
from config import bot, dp, Admin
from handlers import commands, echo, form
from database import db


async def set_commands():
    commands_list = [
        BotCommand(command='start', description='Старт бота'),
        BotCommand(command='help', description='Помощь'),
        BotCommand(command='mem', description='Фотка мема'),
        BotCommand(command='sticker', description='Отправка стикеров'),
        BotCommand(command='add_product', description='Добавление нового товара'),
        BotCommand(command='form', description='Заказ пиццы'),
        BotCommand(command='orders', description='Все заказы'),
    ]

    await bot.set_my_commands(commands_list)


async def on_startup():
    db.create_table_db()
    await set_commands()

    for admin_id in Admin:
        await bot.send_message(
            chat_id=admin_id,
            text='Бот включен!'
        )


dp.startup.register(on_startup)
dp.include_router(router=commands.router_commands)
dp.include_router(router=form.router_form)
dp.include_router(router=echo.router_echo)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))
