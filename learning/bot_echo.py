import telebot
from dotenv import load_dotenv 
import os
load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.from_user.id, 'это старт')
    
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.from_user.id, 'Это помощь')

@bot.message_handler(content_types=['text'])

#def reply_text(message):
#    bot.reply_to(message, message.text)

def send_text(message):
    bot.send_message(message.from_user.id, message.text)

bot.polling(non_stop=True)