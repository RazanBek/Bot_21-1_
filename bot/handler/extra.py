from aiogram import types, Dispatcher
from bot.config import bot, ADMINS
import random


# @dp.message_handler(content_types=['text'])
async def echo(message: types.Message):
    if message.text.isnumeric():
        await message.answer(int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)


async def game(message: types.Message):
    if message.text.startswith('game') and message.from_user.id in ADMINS:
        emojis = ['🎯', '🎳', '🎰', '🎲', '⚽', '️🏀']
        rand_game = random.choice(emojis)
        await bot.send_dice(message.chat.id, emoji=rand_game)


def register_handler_extra_game(dp: Dispatcher):
    dp.register_message_handler(game)


def register_handler_extra(dp: Dispatcher):
    dp.message_handler(echo, content_types=['text'])
