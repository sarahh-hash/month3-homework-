from aiogram import Bot, Dispatcher
from decouple import config

Admin = [6155653670, ]

token_bot = config("TOKEN")
# print(token_bot)

bot = Bot(token=token_bot)
dp = Dispatcher()
path_db = "database/sqlite3.db"
