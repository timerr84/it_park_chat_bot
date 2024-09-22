import telebot;
bot = telebot.TeleBot(''); #тут токен бота
@bot.message_handler(content_types=['text']) #слушаем бота
def get_text(message):
    global name
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Здравствуй, мой дорогой друг!")
    elif message.text == "Привет": #проверям сообщение от пользователя
        bot.send_message(message.from_user.id, "Здравствуй, мой дорогой друг!") #отвечаем пользователю
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "напиши: Привет")
    else:
        a = message.text
        bot.send_message(message.from_user.id, f"я тебя не понимаю твою надпись '{a}' '/help'")
bot.polling(none_stop=True, interval=0)# бот постоянно будет опрашивает сервер