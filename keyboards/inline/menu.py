from aiogram.types import  InlineKeyboardMarkup,InlineKeyboardButton


menu_start=InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="Math\n",callback_data="kinolar"),
            InlineKeyboardButton(text="Trivia\n",callback_data="qidirish"),


        ], [
            InlineKeyboardButton(text="Date\n",callback_data="pul"),
            InlineKeyboardButton(text="Random\n",callback_data="rasm"),
        ],

    ],
     resize_keyboard=True
)
""""
"""""