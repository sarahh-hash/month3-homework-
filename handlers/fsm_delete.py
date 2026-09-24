from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database import db


router_delete = Router()


class DeleteOrder(StatesGroup):
    confirm = State()


confirm_delete_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✅ Да, удалить",
                callback_data="confirm_delete:yes"
            ),
            InlineKeyboardButton(
                text="❌ Отмена",
                callback_data="confirm_delete:no"
            )
        ]
    ]
)


# Ловим нажатие на 🗑 Удалить
@router_delete.callback_query(F.data.startswith("delete:"))
async def ask_delete_confirmation(call: CallbackQuery, state: FSMContext):
    order_id = call.data.split(":")[1]

    await state.update_data(order_id=order_id)
    await state.set_state(DeleteOrder.confirm)

    await call.message.answer(
        f"Точно удалить заказ №{order_id}?",
        reply_markup=confirm_delete_buttons
    )

    await call.answer()


# Ловим подтверждение
@router_delete.callback_query(DeleteOrder.confirm, F.data.startswith("confirm_delete:"))
async def process_delete_confirmation(call: CallbackQuery, state: FSMContext):
    answer = call.data.split(":")[1]

    if answer == "yes":
        data = await state.get_data()
        order_id = data["order_id"]

        await db.delete_order_by_id(order_id)

        await call.message.answer(f"Заказ №{order_id} удалён.")
    else:
        await call.message.answer("Удаление отменено.")

    await state.clear()
    await call.answer()