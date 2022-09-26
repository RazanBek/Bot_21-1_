from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot.keyboards.client_kb import stop_markup
from bot.config import ADMINS, bot
from bot.database import db
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and message.from_user.id in ADMINS:
        await FSMAdmin.photo.set()
        await message.answer('фото блюда')
    else:
        await message.answer('только адиминсы могут добавить блюдо!!!')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer('название блюда?')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('описание блюда:')


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer('цена блюда?')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = f'{message.text}$'
        await bot.send_photo(message.from_user.id, data['photo'], caption=f'Name: {data["name"]}\n'
                                                                          f'Description: {data["description"]}\n'
                                                                          f'price: {data["price"]}\n')
    await state.finish()
    await message.answer('покеда неудачник!')


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('регистрация отменена')


async def complete_delete(call: types.CallbackQuery):
    await db.sql_command_delete(call.data.replace('delete ', ''))
    await call.answer(text='удалено :)', show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


def register_handlers_fsm_admin_menu(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, commands=['stop'], state='*')
    dp.register_message_handler(cancel_registration,
                                Text(equals='stop', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(complete_delete, commands=['del'])
    dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith('delete '))
