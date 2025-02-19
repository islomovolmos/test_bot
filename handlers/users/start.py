from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from keyboards.inline.menu import menu_start
from random import randint
import requests
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer('assalomu aleykum  ',reply_markup=menu_start)


@dp.message_handler(text="kinolar")
async def random(message: types.Message) :
    url=f"http://numbersapi.com/{randint(1,10000)}"
    request=requests.get(url)
    await message.answer(request.content)


@dp.message_handler(text="qidirish")
async def random(message: types.Message) :
    url=f"http://numbersapi.com/{randint(1,10000)}"
    request=requests.get(url)
    await message.answer(request.content)

@dp.message_handler(text="pul")
async def random(message: types.Message) :
    url=f"http://numbersapi.com/{randint(1,10000)}"
    request=requests.get(url)
    await message.answer(request.content)


@dp.message_handler(text="rasm")
async def random(message: types.Message) :
    url=f"http://numbersapi.com/{randint(1,10000)}"
    request=requests.get(url)
    await message.answer(request.content)


























@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = f"Hello, *{message.from_user.full_name}*!\n\n"
    text += "```NUMBERS API```\n\n"
    text += "*- What tales do your metrics tell?*\n"
    text += "*- Bring your metrics and dates to life.*\n"
    text += "*- An API BOT for interesting facts about numbers.*\n"
    text += "*- Let your statistics tell tales and dates come to life.*\n"
    await message.answer(text=text, parse_mode="Markdown", reply_markup=menu_start)

@dp.callback_query_handler(text="go_back")
async def go_back(call: types.callback_query):
    await call.message.edit_text("You are back in main menu 🎯", reply_markup=menu_start)








# from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandStart
# from urllib3 import request
# from keyboards.inline.menu import menu_start
# from loader import dp
# from random import randint
#
#
#
#
#
#
# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menu_start)
#
# @dp.message_handler(content_types=types.ContentType.VIDEO)
# async def message_video(message:types.Message):
#     fail_id = message.video.file_id
#     await message.answer(fail_id)
#
# @dp.callback_query_handler(text="kinolar")
# async def message_video(call: types.CallbackQuery):
#     url = f"http://numbersapi.com/#42 "
#     await call.message.answer(url)
#
# @dp.callback_query_handler(text="rasm")
# async def message_video(call: types.CallbackQuery):
#     url = "http://numbersapi.com/#0/trivia:~:text=0%201%202,temperature%20old%20the"
#     await call.message.answer(url)























