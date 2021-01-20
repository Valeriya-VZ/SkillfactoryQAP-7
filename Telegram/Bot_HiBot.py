# Обработчик, кот. из сообщения берет username и выдает приветственное сообщение с привязкой к пользователю.

import telebot

TOKEN = 'Токен, полученный при регистрации' 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'Welcome, {message.chat.username}')

@bot.message_handler(content_types=['photo'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

bot.polling(none_stop=True)
