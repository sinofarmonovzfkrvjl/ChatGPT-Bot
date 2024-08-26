from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import logging
import asyncio
import requests
from keyboards import bot_language
import os

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f'Choose the language | kerakli tilni tanlang | выберите желаемый язык', reply_markup=bot_language)

@dp.callback_query()
async def Callback(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == "uz":
        await call.message.answer(f"Salom <b>{call.message.chat.full_name}</b>\nmen AI Assistant botman", parse_mode="HTML")
    elif call.data == "en":
        await call.message.answer(f"Hello <b>{call.message.chat.full_name}</b>\ni'm AI Assistant Bot", parse_mode="HTML")
    elif call.data == "ru":
        await call.message.answer(f"Привет <b>{call.message.chat.full_name}</b>\nя бот помощник", parse_mode="HTML")

@dp.message()
async def echo(message: types.Message):
    res = requests.get("https://gemini-api-qnmb.onrender.com/api/v1/generate?word=" + message.text)
    await message.answer(res.json(), parse_mode="markdown")

async def main():
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())