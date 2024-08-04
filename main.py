from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import logging
import google.generativeai as genai
import asyncio
from keyboards import bot_language, get_audio

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f'Choose the language | kerakli tilni tanlang | выберите желаемый язык', reply_markup=bot_language)

@dp.callback_query()
async def Callback(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == "uz":
        await call.message.answer(f"Salom <b>{call.message.chat.full_name}</b>\nmen AI English Assistant botman\nme sizge ingliz tilini o'rganishingizga yordam beraman", parse_mode="HTML")
    elif call.data == "en":
        await call.message.answer(f"Hello <b>{call.message.chat.full_name}</b>\ni'm AI English Assistant Bot\n i can help you to learn english**", parse_mode="HTML")
    elif call.data == "ru":
        await call.message.answer(f"Привет <b>{call.message.chat.full_name}</b>\nя бот Английский помощник\nя могу помочь вам узнать английский**", parse_mode="HTML")

@dp.message()
async def echo(message: types.Message):
    genai.configure(api_key="")
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(message.text)
    await message.answer(response.text, parse_mode="MARKDOWN")
    

async def main():
    bot = Bot(token="")
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())