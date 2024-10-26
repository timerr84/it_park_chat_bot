from telebot import types, TeleBot
from dotenv import load_dotenv #сначала надо импортировать pip install python-dotenv
import os

load_dotenv()

bot = TeleBot(os.getenv('TOKEN'))

@bot.callback_query_handler(func=lambda call: True)
def handler_call(call):
    match call.data:
        case "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
            bot.send_message(call.message.chat.id, 'Начнем, как тебя зовут?')
            bot.register_next_step_handler(call.message, get_name)
                    
        case "no":
            keyboard2 = types.InlineKeyboardMarkup()    
            keyboard2.add(types.InlineKeyboardButton(text='Старт', callback_data='/start'))
            bot.send_message(call.message.chat.id, 'Очень жаль! Если захочешь начать общение заново нажми на Старт', reply_markup=keyboard2)
            
        case "/start":
            start(call.message)
        

@bot.message_handler(commands=['start'])
def start(message): 
    keyboard = types.InlineKeyboardMarkup()    
    keyboard.add(types.InlineKeyboardButton(text='Да', callback_data='yes'), types.InlineKeyboardButton(text='Нет', callback_data='no'))
    bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}! познакомися?', reply_markup=keyboard)



def get_name(message):
    global name 
    name = message.text 
    bot.send_message(message.from_user.id, f'{name}, сколько тебе лет?')   
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    try:          
        age = int(message.text) 
        bot.send_message(message.from_user.id, f'тебя зовут {name}, родился в {2024 - age}')
        bot.register_next_step_handler(message, start)
    except Exception:
        bot.send_message(message.from_user.id, 'введите число')
        bot.register_next_step_handler(message, get_age) 
def get_start(message): 
    keyboard = types.InlineKeyboardMarkup()    
    keyboard.add(types.InlineKeyboardButton(text='Да', callback_data='yes'), types.InlineKeyboardButton(text='Нет', callback_data='no'))
    bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}! познакомися?', reply_markup=keyboard)



bot.polling(none_stop=True, interval=0)