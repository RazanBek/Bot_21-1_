from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.config import bot


# @dp.callback_query_handler(text="button_call_1")
async def quiz_1_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_2)

    question = "skoka mne let"
    answers = [
        "0",
        "5",
        "10",
        "15",
        "20",
        "1000",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="EZ!",
        open_period=10,
        reply_markup=markup
    )


async def quiz_1_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_3")
    markup.add(button_call_2)

    question = "skoka let moey sobake"
    answers = [
        "0",
        "5",
        "10",
        "15",
        "20",
        "3",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="random",
        open_period=10,
        reply_markup=markup
    )


async def quiz_1_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_3")
    markup.add(button_call_2)

    question = "da ili net"
    answers = [
        "da",
        "net",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="random",
        open_period=10,
        reply_markup=markup
    )


async def quiz_2_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_2)

    question = "skoka let koshke"
    answers = [
        "0",
        "5",
        "8",
        "10",
        "113",
        "2",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=5,
        explanation="EZ!",
        open_period=10,
        reply_markup=markup
    )


async def quiz_2_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_3")
    markup.add(button_call_2)

    question = "skoka let moey sestre"
    answers = [
        "0",
        "51",
        "102",
        "23",
        "20",
        "25",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="random",
        open_period=10,
        reply_markup=markup
    )


async def quiz_2_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_3")
    markup.add(button_call_2)

    question = "qwerty?"
    answers = [
        "qwerty",
        "йцукен",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="random",
        open_period=10,
        reply_markup=markup
    )


def register_handlers_callback_1(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_1_2, text="button_call_1")   #lambda call: call.data == "button_call_1"
    dp.register_callback_query_handler(quiz_1_3, text="button_call_2")
    dp.register_callback_query_handler(quiz_1_4, text="button_call_3")


def register_handlers_callback_2(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2_2, text="button_call_1")   #lambda call: call.data == "button_call_1"
    dp.register_callback_query_handler(quiz_2_3, text="button_call_2")
    dp.register_callback_query_handler(quiz_2_4, text="button_call_3")