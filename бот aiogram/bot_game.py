from aiogram import Bot, Dispatcher, types, executor

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv 
import os

load_dotenv()
Token = os.getenv('TOKEN')
bot = Bot(token=Token)
dp = Dispatcher(bot)

player = 'X' #нужен для сохранения результата и вывод сообщения
xo = ('X', 'O') #нужен для сравнения результата

def markup_key(event): #функция для создания кнопок
    markup = InlineKeyboardMarkup(row_width=3)
    for num, text in enumerate(event): # цикла для создания кнопок
        markup.insert(InlineKeyboardButton(text, callback_data=f"{num}"))
    return markup

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    global event #глобальная переменная
    event = list(' ' * 9) #создаем список
    await message.answer('ход X', reply_markup=markup_key(event)) #отправляем сообщение и создаем кнопки

@dp.message_handler(content_types=['text'])
async def get_text(message: types.Message):
    await message.answer('для начала игры отправь команду /start')



@dp.callback_query_handler(lambda c: c.data)
async def process_callback_button(callback_query: types.CallbackQuery):
    global event, player, xo #глобальные переменные
    await callback_query.answer() #отправляем пустое сообщение, без этого не дает нормально редактировать кнопки
    
    if event[int(callback_query.data)] == ' ': #условие проверки, если пустое поле, то ставим Х или О
        event[int(callback_query.data)] = player # меняем список, ставим соответствуеющее значение
        if player == 'X':#проверка и изменение переменной на другое значение
            player = 'O'
        else:
            player = 'X'
        await callback_query.message.edit_text(f'ход {player}', reply_markup=markup_key(event)) #изменяем сообщение и кнопки
        
        if ((event[0] == event[1] == event[2] in xo) or (event[3] == event[4] == event[5] in xo) or (event[6] == event[7] == event[8] in xo) or #условие проверки выйгрыша
            (event[0] == event[3] == event[6] in xo) or (event[1] == event[4] == event[7] in xo) or (event[2] == event[5] == event[8] in xo) or 
            (event[0] == event[4] == event[8] in xo) or (event[2] == event[4] == event[6] in xo)) :
            if player == 'X': #если выйгрыш, меняем обратно значение переменной для вывода сообщения
                player = 'O'
            else:
                player = 'X'
            await  callback_query.message.answer(f'игрок {player} выйграл \nдля начала игры нажми /start')
        elif event.count(' ') == 0: #проверям, если пустых полей не остается, то выводим сообщение 
            await  callback_query.message.answer('больше нет ходов \nдля начала игры нажми /start')
    else:
        await callback_query.answer('нельзя изменить поле') #если проверка на пустое поле не прошло, то сообщаем об этом
    
if __name__ == '__main__':
    executor.start_polling(dp)  