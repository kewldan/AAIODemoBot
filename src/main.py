import asyncio
import logging
from re import Match
from uuid import uuid1

from aaio import AAIO
from aiogram import Bot, Dispatcher, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import config

bot = Bot(config['token'], parse_mode=ParseMode.HTML)
dp = Dispatcher()
router = Router()
dp.include_router(router)
aaio = AAIO(config['merchant_id'], config['secret'], config['key'])


async def main():
    logging.basicConfig(level=logging.DEBUG)

    balance = await aaio.get_balances()
    print('Балансы:', balance)

    ips = await aaio.get_ips()
    print('IP адреса AAIO:', ips)

    await dp.start_polling(bot)


@router.message(CommandStart())
async def on_start_command(message: Message):
    builder = InlineKeyboardBuilder()

    builder.button(text='💵 Создать платёж', callback_data='create_payment')

    await message.answer('👋 Привет, этот бот демонстрирует возможности библиотеки AAIO для Python!\n'
                         '\n'
                         'Исходный код бота: https://github.com/kewldan/AAIODemoBot\n'
                         'Библиотека: https://kewldan.vercel.app/projects/aaio',
                         reply_markup=builder.as_markup())


@router.callback_query(F.data == 'create_payment')
async def on_create_payment_callback(query: CallbackQuery):
    builder = InlineKeyboardBuilder()

    order_id = str(uuid1())  # Order ID must be saved to your database, because user can get product twice

    payment_url = aaio.create_payment(100, order_id, 'Этот платёж необходим для демонстрации работы библиотеки')

    builder.button(text='💰 Перейти к оплате', url=payment_url)
    builder.button(text='🔄️ Проверить платеж', callback_data=f'check_payment_{order_id}')

    builder.adjust(1)

    await query.message.edit_text('🤖 Оплатите счёт ниже для продолжения', reply_markup=builder.as_markup())


@router.callback_query(F.data.regexp(
    r"^check_payment_([0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12})$").as_(
    "match"))
async def on_check_payment_callback(query: CallbackQuery, match: Match[str]):
    order_id = match.group(1)

    payment_info = await aaio.get_payment_info(order_id)
    if payment_info.is_success():
        await query.message.edit_text('✅ Счёт оплачен')
    else:
        await query.answer('❌ Счёт ожидает оплаты')


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
