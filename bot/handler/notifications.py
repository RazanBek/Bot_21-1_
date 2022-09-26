import asyncio
import aioschedule
from aiogram import types, Dispatcher
from bot.config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text="хорошо")


async def go_to_sleep():
    await bot.send_message(chat_id=chat_id, text="время играть в доту")


async def schedule():
    aioschedule.every().monday.at("18:00").do(go_to_sleep)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'когда?' in word.text)