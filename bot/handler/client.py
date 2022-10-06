from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.config import bot
import random
from bot.database.db import sql_command_random
from bot.parser.film import parser


# @dp.message_handler(commands=['mem'])
async def command_start(message: types.Message):
    photos = [
        'media/мем.jpg',
        'media/мем1.jpg',
        'media/мем2.jpg',
        'media/мем3.jpg',
    ]
    photo = open(random.choice(photos), 'rb')
    await bot.send_photo(message.from_user.id, photo)


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "gde napisano: harooosh!!!"
    answers = [
        "harooosh!!!",
        "harooosh!!!",
        "harooosh!!!",
        "harooosh!!!",
        "harooosh!!!",
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="skam",
        open_period=10,
        reply_markup=markup
    )


async def quiz_2(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "ochen umniy vopros"
    answers = [
        "pravilniy otvet",
        "neprvilniy otvet",
        "horoshiy otvet",
        "otlichniy otvet",
        "takoy sebe otvet",
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        open_period=10,
        reply_markup=markup
    )


async def show_random_user(message: types.Message):
    await sql_command_random(message)


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz_1'])
    dp.register_message_handler(show_random_user, commands=['get'])

#
# def register_handler_client_1(dp: Dispatcher):
#     dp.register_message_handler(quiz_2, commands=['quiz_2'])
