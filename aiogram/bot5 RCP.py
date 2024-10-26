from aiogram import Bot, Dispatcher, executor, types
#pip install aiogram==2.23.1
#from aiogram.utils import executor
#pip install --force-reinstall -v "aiogram==2.23.1"
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv 
import os, random, sqlite3
rand_list = ['камень' , 'ножницы', 'бумага']
game_dict = {"камень_ножницы": 'Камень бьёт ножницы, вы выиграли!',
             "ножницы_камень": 'Камень бьёт ножницы, вы проиграли!',
             "ножницы_бумага": 'Ножницы режут бумагу, вы выиграли',
             "бумага_ножницы": 'Ножницы режут бумагу, вы проиграли',
             "бумага_камень": 'Бумага кроет камень, вы выйграли!',
             "камень_бумага": 'Бумага кроет камень,вы проиграли!'}
load_dotenv()

Token = os.getenv('TOKEN')
bot = Bot(token=Token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    global choice_rand
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton('Камень', callback_data='камень'), 
        types.InlineKeyboardButton('Ножницы', callback_data='ножницы'), 
        types.InlineKeyboardButton('Бумага', callback_data='бумага'))  
    await message.answer("Привет! Выбери камень, ножницы, бумагу)", reply_markup=keyboard)
 
@dp.message_handler(commands=["help"])
async def help(message: types.Message):
   await message.answer("тут помощь")

@dp.callback_query_handler(lambda c: c.data)
async def process_callback_button(callback_query: types.CallbackQuery):
    global choice_rand
    choice_rand = random.choice(rand_list)
    await callback_query.message.answer(f'ваш выбор {callback_query.data}, бот выбрал {choice_rand}')
    if choice_rand == callback_query.data:
        await callback_query.message.answer("Ничья!")
    else:
        await bot.answer_callback_query(callback_query.id)
        key_dict = f'{callback_query.data}_{choice_rand}'
        await callback_query.message.answer(game_dict[key_dict])
    await callback_query.message.answer('Чтобы начать игру сначала, нажми /start')
 

if __name__ == "__main__":
    executor.start_polling(dp)