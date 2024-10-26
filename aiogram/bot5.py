from aiogram import Bot, Dispatcher, executor, types

#pip install aiogram==2.23.1
#from aiogram.utils import executor
#pip install --force-reinstall -v "aiogram==2.23.1"

#сначала надо импортировать pip install python-dotenv
from dotenv import load_dotenv 
import os

load_dotenv()
Token = os.getenv('TOKEN')
bot = Bot(token=Token)
dp = Dispatcher(bot)

@dp.callback_query_handler(lambda c: c.data=="yes")
async def press_button(callback_query: types.CallbackQuery):    
    await callback_query.message.answer(callback_query)

@dp.callback_query_handler(lambda c: c.data=='нет')  
async def press_button(callback_query: types.CallbackQuery):
    await callback_query.message.answer(callback_query.from_user.first_name + ', ' + 'вы нажали нет')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    inline_keyboard = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton('да', callback_data='yes')
    button_2 = types.InlineKeyboardButton('нет', callback_data='нет')
    inline_keyboard.add(button_1, button_2)
    await message.answer('привет! Давай поиграем?', reply_markup=inline_keyboard)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(
        """sdkfjsldkfj
        sdfsdjfkj"""
    )

@dp.message_handler()
async def send_message(message: types.Message):    
    await message.answer(message.text + ' давай начем заново? нажми /start')


executor.start_polling(dp)