from aiogram import Bot, Dispatcher
from decouple import config

Admin = [8946046965,]

token_bot = config("TOKEN")
# print(token_bot)

bot = Bot(token=token_bot)
dp = Dispatcher()