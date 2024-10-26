from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv 
import os

load_dotenv()
Token = os.getenv('TOKEN')

bot = Bot(token=Token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_game(message: types.Message):    
    keyboard = InlineKeyboardMarkup(row_width=3)
    global bt
    
    for i in range(9):
        bt1 = InlineKeyboardButton(i, callback_data=str(i))
        keyboard.insert(bt)
    await message.answer('привет! Давай поиграем?', reply_markup=keyboard)

@dp.callback_query_handler(lambda callback_query: callback_query)
async def bt_callback(callback_query: types.CallbackQuery):
    global bt
    await bot.edit_message_text(' sdfsdf')
    await callback_query.answer()


if __name__ == "__main__":
    executor.start_polling(dp)
