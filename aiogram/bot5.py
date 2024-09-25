from aiogram import Bot, Dispatcher, executor, types
#pip install aiogram==2.23.1
#from aiogram.utils import executor
#pip install --force-reinstall -v "aiogram==2.23.1"
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv 
import os

load_dotenv()
Token = os.getenv('TOKEN')
bot = Bot(token=Token)
dp = Dispatcher(bot)
 
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Привет!")
   dp.message_handler()
async def echo(message: types.Message):
   await message.answer(message.text)
 
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)

#https://surik00.gitbooks.io/aiogram-lessons/content/chapter5.html