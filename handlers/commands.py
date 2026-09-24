import random
from datetime import datetime
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from config import bot
from database import db

router_commands = Router()

JOKES = [
    "— Программист, почему твой код не работает?\n— Не знаю, на моём компьютере всё работает!",
    "Существует 10 типов людей: те, кто понимают двоичную систему счисления, и те, кто её не понимают.",
    "Алгоритм — это слово, которое используют программисты, когда не хотят объяснять, что они сделали.",
    "Отладка кода — это как быть детективом в фильме про убийство, где вы одновременно и детектив, и убийца.",
    "— Сколько программистов нужно, чтобы поменять лампочку?\n— Ни одного, это аппаратная проблема!",
]

@router_commands.message(Command('start'))
async def start_handler(message: Message):
    await message.answer(text='Привет')

@router_commands.message(Command('help'))
async def help_handler(message: Message):
    await bot.send_message(chat_id=message.chat.id, text='Первый бот группы 69-2')


@router_commands.message(F.text == 'привет')
async def hello_text_handler(message: Message):
    await message.answer('hello')


@router_commands.message(Command('mem'))
async def mem_handler(message: Message):
    photo_mem = FSInputFile('media/mem.png')
    await bot.send_photo(chat_id=message.chat.id, photo=photo_mem)


@router_commands.message(Command('sticker'))
async def sticker_handler(message: Message):
    await message.answer_sticker('CAACAgIAAxkBAAMjapbjokNBT2YjOMt9wh5q_5HZtpIAAuMAA1eEbA_LD3f9g8IMvD0E')

    await message.answer_sticker('CAACAgIAAxkBAAMnapbkCM4uItEY8u7AtfAwChFY6Z0AAiqNAAJBuqlLZqmYVBFV9sw9BA')


@router_commands.message(F.sticker)
async def get_sticker_id_handler(message: Message):
    await message.answer(f'ID - этого стикера - {message.sticker.file_id}')



@router_commands.message(Command("time"))
async def time_handler(message: Message):
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    await message.answer(f"Сейчас: {now}")

@router_commands.message(Command("random"))
async def random_handler(message: Message):
    number = random.randint(1, 100)
    await message.answer(f"Твоё случайное число: {number}")

@router_commands.message(Command("joke"))
async def joke_handler(message: Message):
    joke = random.choice(JOKES)
    await message.answer(joke)

@router_commands.message(Command("orders"))
async def orders(message: Message):
    orders = await db.get_orders()

    if not orders:
        await message.answer("Заказов пока нет.")
        return

    for order in orders:
        order_id = order[0]
        size = order[1]
        address = order[2]
        photo_id = order[3]
        topping = order[4]

        caption = (
            f"Заказ №{order_id}\n"
            f"Размер: {size}\n"
            f"Начинка: {topping}\n"
            f"Адрес: {address}"
        )

        await message.answer_photo(
            photo=photo_id,
            caption=caption
        )
