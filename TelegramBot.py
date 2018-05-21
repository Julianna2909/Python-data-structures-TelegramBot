# -*- coding: utf-8 -*-
from datetime import time

import TelegramBotToken
import telebot

bot = telebot.TeleBot(TelegramBotToken.token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    TelegramBotToken.counter = 0
    bot.reply_to(message, "Привіт, розпочнемо вікторину? Відправ мені yes щоб почати :3")

@bot.message_handler(regexp="yes")
def quiz(message):
    bot.send_message(message.chat.id, TelegramBotToken.questions[TelegramBotToken.counter])
    @bot.message_handler(content_types=['text'])
    def solve(message):
        if message.text == TelegramBotToken.answers[TelegramBotToken.counter]:
            bot.send_message(message.chat.id, TelegramBotToken.comments[TelegramBotToken.counter])
            TelegramBotToken.counter += 1
        else:
            bot.send_message(message.chat.id, "try again")

        if(TelegramBotToken.counter >= len(TelegramBotToken.questions)):
            congrat(message)
        else:
            bot.send_message(message.chat.id, TelegramBotToken.questions[TelegramBotToken.counter])

def congrat(message):
    bot.send_message(message.chat.id, "ну і всьо")
    sticker = open('/home/julianna/KYPCOBA/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)

if __name__ == '__main__':
     bot.polling(none_stop = True)