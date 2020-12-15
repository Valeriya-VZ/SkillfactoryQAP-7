# Обработчик, кот. из сообщения берет username и выдает приветственное сообщение с привязкой к пользователю.

import telebot

TOKEN = 'Токен, полученный при регистрации' 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, {message.chat.username}")

bot.polling(none_stop=True)
