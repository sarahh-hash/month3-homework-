from aiogram import Bot, Dispatcher
from decouple import config

token_bot = config("TOKEN")
# print(token_bot)

bot = Bot(token=token_bot)
dp = Dispatcher()