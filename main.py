from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import logging
import asyncio
import requests
from keyboards import bot_language

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f'Choose the language | kerakli tilni tanlang | выберите желаемый язык', reply_markup=bot_language)

@dp.callback_query()
async def Callback(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == "uz":
        await call.message.answer(f"Salom <b>{call.message.chat.full_name}</b>\nmen AI Assistant botman\nme sizge ingliz tilini o'rganishingizga yordam beraman", parse_mode="HTML")
    elif call.data == "en":
        await call.message.answer(f"Hello <b>{call.message.chat.full_name}</b>\ni'm AI Assistant Bot\n i can help you to learn english**", parse_mode="HTML")
    elif call.data == "ru":
        await call.message.answer(f"Привет <b>{call.message.chat.full_name}</b>\nя бот помощник\nя могу помочь вам узнать английский**", parse_mode="HTML")

@dp.message()
async def echo(message: types.Message):
    res = requests.get("https://gemini-api-qnmb.onrender.com/api/v1/generate?word=" + message.text)
    await message.answer(res.json())
    

async def main():
    bot = Bot(token="5904607271:AAFycN_K-pXKmue3YR8zyGYS2Q5A9MZnJzk")
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())