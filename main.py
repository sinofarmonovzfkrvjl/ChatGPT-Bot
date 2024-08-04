from aiogram import Bot, Dispatcher, types, executor
import logging
import google.generativeai as genai
from keyboards import bot_language
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f'Choose the language | kerakli tilni tanlang | выберите желаемый язык', reply_markup=bot_language)

@dp.message_handler()
async def main(message: types.Message):
    global text
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(message.text)
    text = response.text
    await message.answer(text=text, parse_mode="MARKDOWN")

@dp.callback_query_handler()
async def Callback(call: types.CallbackQuery):
    await call.message.delete()
    if call.data == "uz":
        await call.message.answer(f"Salom <b>{call.message.chat.full_name}</b>\nmen AI English Assistant botman\nme sizge ingliz tilini o'rganishingizga yordam beraman", parse_mode="HTML")
    elif call.data == "en":
        await call.message.answer(f"Hello <b>{call.message.chat.full_name}</b>\ni'm AI English Assistant Bot\n i can help you to learn english**", parse_mode="HTML")
    elif call.data == "ru":
        await call.message.answer(f"Привет <b>{call.message.chat.full_name}</b>\nя бот Английский помощник\nя могу помочь вам узнать английский**", parse_mode="HTML")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)