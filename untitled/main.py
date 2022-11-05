import telebot
import random
import win10toast

bot = telebot.TeleBot("5597383393:AAFRZrS7D0IBCYivdMUR4pg-9TXWN1V2X7c")

@bot.message_handler(commands=['start'])

def start(  ):
    mess = f'Hi, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=['photo1'])
def photo1(message):
    photo = open(f'wall ({random.randint(1,21)}).jpg', 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['photo2'])
def photo2(message):
    photo = open(f'mall ({random.randint(1,13)}).jpg', 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler()
def get_user_text(message):
    if message.text == 'Nano':
        bot.send_message(message.chat.id, 'Are you a true nano?', parse_mode="html")
    elif message.text == '/id':
        bot.send_message(message.chat.id, f'Your ID: {message.from_user.id}', parse_mode="html")
    elif message.text == 'photo':
        photo = open('54041.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'I don`t understand you', parse_mode="html")

bot.polling(none_stop=True)

plor plor