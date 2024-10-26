import telebot
from dotenv import load_dotenv 
import os
from key_button import keyboard2
load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))

@bot.callback_query_handler(func=lambda call: call.data == 'да')
def call_handler(call):    
    bot.send_message(call.message.chat.id, f'вы нажали {call.data}')

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.from_user.id, 'нажми на любую кнопку', reply_markup=keyboard2)


bot.polling(non_stop=True)