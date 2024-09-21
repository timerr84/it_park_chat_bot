import telebot
bot = telebot.TeleBot('8051689493:AAGQB6Ec2DaFYh8JZsosDwvOjTKSoiWcW00')
name = ''
age = 0
fl_ask = 0
@bot.message_handler(content_types=['text'])

def get_start(message): 
    global fl_ask
    global age
    if message.text == '/start' and fl_ask == 0:
        bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}! познакомися? Напиши да или нет')
        fl_ask = 1
    elif message.text == 'да' and fl_ask == 1:
        bot.send_message(message.from_user.id, 'Начнем, как тебя зовут?')
        fl_ask = 0
        age = 0
        bot.register_next_step_handler(message, get_name)
    elif message.text == 'нет' and fl_ask == 1:
        bot.send_message(message.from_user.id, 'Очень жаль! Если захочешь начать общение заново нажми /start')
        fl_ask = 0
    elif fl_ask == 0:
        bot.send_message(message.from_user.id, 'Для начала общения нажми /start')
    elif fl_ask == 1:
        bot.send_message(message.from_user.id, 'Напиши да или нет')

def get_name(message):
    global name 
    name = message.text 
    bot.send_message(message.from_user.id, f'{name}, сколько тебе лет?')   
    bot.register_next_step_handler(message, get_age) 

def get_age(message):
    global age
    while age == 0:
        try:          
            age = int(message.text) 
            bot.send_message(message.from_user.id, f'тебя зовут {name}, родился в {2024 - age}')
            bot.register_next_step_handler(message, get_start)
        except Exception:
            bot.send_message(message.from_user.id, 'введите число')             

bot.polling(none_stop=True, interval=0)