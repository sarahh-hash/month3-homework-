from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


size_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🍕 Маленькая",
                callback_data="size:маленькая"
            ),
            InlineKeyboardButton(
                text="🍕 Средняя",
                callback_data="size:средняя"
            ),
            InlineKeyboardButton(
                text="🍕 Большая",
                callback_data="size:большая"
            )
        ]
    ]
)


topping_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🧀 Сыр",
                callback_data="topping:сыр"
            ),
            InlineKeyboardButton(
                text="🥓 Пепперони",
                callback_data="topping:пепперони"
            )
        ],
        [
            InlineKeyboardButton(
                text="🍄 Грибы",
                callback_data="topping:грибы"
            ),
            InlineKeyboardButton(
                text="🍗 Курица",
                callback_data="topping:курица"
            )
        ]
    ]
)


def delete_button(order_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🗑 Удалить",
                    callback_data=f"delete:{order_id}"
                )
            ]
        ]
    )