from telebot import types
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton('да'), 
                                                               types.KeyboardButton('нет'))
keyboard2 = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('да', callback_data="да"),
                                             types.InlineKeyboardButton('нет', callback_data="нет"))