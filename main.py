import telebot
import requests
import random
from telebot import types

bot = telebot.TeleBot("")

lvl1_sim = "1234567890abcdefghijklmnopqrstuvwxyz"

lvl1_sim1 = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def password1():
    global password
    password = ""
    for i in range(8):
        password += random.choice(lvl1_sim)
    return password

def password2():
    global password
    password = ""
    for i in range(16):
        password += random.choice(lvl1_sim)
    return password

def password3():
    global password
    password = ""
    for i in range(24):
        password += random.choice(lvl1_sim1)
    return password

gabela = '''Написание бота в телеграмме, с помощью которого пользователь получает пароль с определенной сложностью:
	    1 сложность:
Написание пароля с помощью 8 символов, где каждый символ буква английского алфавита или цифра.
	    2 сложность:
Написание пароля с помощью 16 символов, где каждый символ буква английского алфавита или цифра.
	    3 сложность:
Написание пароля с помощью 24 символов, где каждый символ буква английского алфавита(маленькая или большая) или цифра.
Начните генерировать пароль -> /start
 '''



@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboardmain = types.InlineKeyboardMarkup(row_width=2)
    first_button = types.InlineKeyboardButton(text="Создать пароль", callback_data="first")
    second_button = types.InlineKeyboardButton(text="Описание бота", callback_data="second")
    keyboardmain.add(first_button, second_button)
    bot.send_message(message.chat.id, "Привет я бот, помогающий создать пароль", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "mainmenu":

        keyboardmain = types.InlineKeyboardMarkup(row_width=2)
        first_button = types.InlineKeyboardButton(text="Создать пароль", callback_data="first")
        second_button = types.InlineKeyboardButton(text="Описание бота", callback_data="second")
        keyboardmain.add(first_button, second_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Привет я бот, помогающий создать пароль", reply_markup=keyboardmain)

    if call.data == "first":
        keyboard = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="1 сложность", callback_data="1")
        rele2 = types.InlineKeyboardButton(text="2 сложность", callback_data="2")
        rele3 = types.InlineKeyboardButton(text="3 сложность", callback_data="3")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(rele1, rele2, rele3, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выбери сложность пароля",reply_markup=keyboard)

    if call.data == '1':
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Выбрать заново", callback_data="first")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text = password1(), reply_markup=keyboard)

    if call.data == '2':
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Выбрать заново", callback_data="first")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=password2(), reply_markup=keyboard)

    if call.data == '3':
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Выбрать заново", callback_data="first")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=password3(), reply_markup=keyboard)

    if call.data == 'second':
        keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= gabela , reply_markup=keyboard)

if __name__ == "__main__":

    bot.polling(none_stop=True)
bot.polling()

