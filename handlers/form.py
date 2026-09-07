from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router_form = Router()


class PizzaForm(StatesGroup):
    size = State()
    topping = State()
    address = State()


@router_form.message(Command("form"))
async def start_form(message: Message, state: FSMContext):
    await state.set_state(PizzaForm.size)
    await message.answer(
        "Какой размер пиццы? (маленькая, средняя, большая)"
    )


@router_form.message(Command("cancel"))
async def cancel_form(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Анкета отменена.")


@router_form.message(PizzaForm.size)
async def get_size(message: Message, state: FSMContext):
    if message.text.lower() not in ["маленькая", "средняя", "большая"]:
        await message.answer(
            "Выберите размер: маленькая, средняя или большая."
        )
        return

    await state.update_data(size=message.text)
    await state.set_state(PizzaForm.topping)
    await message.answer("Какая начинка?")


@router_form.message(PizzaForm.topping)
async def get_topping(message: Message, state: FSMContext):
    await state.update_data(topping=message.text)
    await state.set_state(PizzaForm.address)
    await message.answer("Введите адрес доставки:")


@router_form.message(PizzaForm.address)
async def get_address(message: Message, state: FSMContext):
    await state.update_data(address=message.text)

    data = await state.get_data()

    await message.answer(
        f"🍕 Ваш заказ:\n"
        f"Размер: {data['size']}\n"
        f"Начинка: {data['topping']}\n"
        f"Адрес: {data['address']}"
    )

    await state.clear()