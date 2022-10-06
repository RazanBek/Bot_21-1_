import asyncio
from aiogram.utils import executor
from config import dp, bot, URL
import logging
from handler import client, callback, extra, admin, fsm_admin_menu, notifications, inline
from bot.database.db import sql_create
from decouple import config


async def on_startup(_):
    await bot.set_webhook(URL)
    asyncio.create_task(notifications.schedule())
    sql_create()


async def on_shutdown(db):
    await bot.delete_webhook()

client.register_handler_client(dp)
callback.register_handlers_callback_1(dp)
# callback.register_handlers_callback_2(dp)
fsm_admin_menu.register_handlers_fsm_admin_menu(dp)
extra.register_handler_extra_game(dp)
admin.register_handlers_admin(dp)
inline.register_handlers_inline(dp)
notifications.register_handlers_notification(dp)

extra.register_handler_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    executor.start_webhook(
        dispatcher=dp,
        webhook_path="",
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host='0.0.0.0',
        port=config("PORT", default=5000)

    )
