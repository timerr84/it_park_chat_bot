import telebot
from telebot import types
from dotenv import load_dotenv 
import os
from key_button import keyboard
load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.from_user.id, 'нажми на любую кнопку', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'да')
def send_text(message):
    bot.send_message(message.from_user.id, f'вы нажали "{message.text}"', 
                     reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(func=lambda message: True)
def send_text(message):
    bot.send_message(message.from_user.id, f'вы набрали "{message.text}"', 
                     reply_markup=types.ReplyKeyboardRemove())

bot.polling(non_stop=True)