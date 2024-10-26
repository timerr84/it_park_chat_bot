from aiogram import Bot, Dispatcher, types, executor
#pip install aiogram==2.23.1
#pip install --force-reinstall -v "aiogram==2.23.1"
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import load_dotenv 
import os

load_dotenv()
Token = os.getenv('TOKEN')
bot = Bot(token=Token)
dp = Dispatcher(bot)

fl = 0
name = ''

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    inline_keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Да', callback_data='yes')
    button2 = types.InlineKeyboardButton('нет', callback_data='no')
    inline_keyboard.add(button1, button2)
    await message.answer('Привет! поиграем?', reply_markup=inline_keyboard)

# Обработчик нажатия Inline-кнопки Да
@dp.callback_query_handler(lambda c: c.data == 'yes')
async def process_callback_button(callback_query: types.CallbackQuery):
    global fl
    await callback_query.answer('Вы нажали кнопку Да!')
    fl = 1
    await text_message(callback_query.message)

# Обработчик нажатия Inline-кнопки Нет  
@dp.callback_query_handler(lambda c: c.data == 'no')
async def process_callback_button(callback_query: types.CallbackQuery):
    await callback_query.answer('Вы нажали кнопку Нет!')    
    await callback_query.message.answer("что бы начать заново, нажми /start")
    
@dp.message_handler()
async def text_message(message: types.Message):
    global fl
    global name
    match fl:
        case 1:
            await message.answer('как тебя зовут?')
            fl = 2
        case 2:
            name = message.text
            await message.answer(f'{name}, сколько тебе лет?')
            fl = 3
        case 3:
            try:
                age = int(message.text)
                await message.answer(f'{name}, ты родился в {2024 - age}')
                fl = 0
            except Exception:
                await message.answer(f'{name}, нужно ввести число!')

if __name__ == '__main__':
    executor.start_polling(dp)