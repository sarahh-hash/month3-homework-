from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database import db
from handlers.button import size_buttons, topping_buttons


router_form = Router()


class PizzaForm(StatesGroup):
    size = State()
    topping = State()
    address = State()
    photo = State()


@router_form.message(Command("form"))
async def start_form(message: Message, state: FSMContext):
    await state.set_state(PizzaForm.size)

    await message.answer(
        "Выберите размер пиццы:",
        reply_markup=size_buttons
    )


@router_form.message(Command("cancel"))
async def cancel_form(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Анкета отменена.")


# Выбор размера кнопкой
@router_form.callback_query(PizzaForm.size, F.data.startswith("size:"))
async def get_size(callback: CallbackQuery, state: FSMContext):

    size = callback.data.split(":")[1]

    await state.update_data(size=size)

    await state.set_state(PizzaForm.topping)

    await callback.message.edit_text(
        "Выберите начинку:",
        reply_markup=topping_buttons
    )

    await callback.answer()


# Выбор начинки кнопкой
@router_form.callback_query(PizzaForm.topping, F.data.startswith("topping:"))
async def get_topping(callback: CallbackQuery, state: FSMContext):

    topping = callback.data.split(":")[1]

    await state.update_data(topping=topping)

    await state.set_state(PizzaForm.address)

    await callback.message.edit_text(
        "Введите адрес доставки:"
    )

    await callback.answer()


@router_form.message(PizzaForm.address)
async def get_address(message: Message, state: FSMContext):

    await state.update_data(address=message.text)

    await state.set_state(PizzaForm.photo)

    await message.answer(
        "Теперь отправьте фотографию:"
    )


@router_form.message(PizzaForm.photo, F.photo)
async def get_photo(message: Message, state: FSMContext):
    data = await state.get_data()

    photo_id = message.photo[-1].file_id

    order_id = await db.add_order(
        data["size"],
        data["address"],
        photo_id
    )

    await db.add_order_details(
        order_id,
        data["topping"]
    )

    await message.answer(
        f"Ваш заказ сохранён!\n\n"
        f"Размер: {data['size']}\n"
        f"Начинка: {data['topping']}\n"
        f"Адрес: {data['address']}"
    )

    await state.clear()