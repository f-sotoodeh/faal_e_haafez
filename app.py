import telebot
from requests import get
from lxml import html

from random import randint

TOKEN = '6878847221:AAFAiM_HYKgtpy9uQOSNs3IzbaPtECNhbsw'

bot = telebot.TeleBot(TOKEN) 

def faal():
    M1 = '//div[@class="m1"]/p/text()'
    M2 = '//div[@class="m2"]/p/text()'
    n = randint(0, 495)
    url = f'https://ganjoor.net/hafez/ghazal/sh{n}'
    doc = html.fromstring(get(url).text)
    poem = []
    for b in zip(doc.xpath(M1), doc.xpath(M2)):
        poem.append('\n'.join(b))
    return '\n\n'.join(poem)

@bot.message_handler(commands=['start'])
def start_message(message):
    welcome = 'برای گرفتن فال ابتدا نیت کنید و سپس از منو دستور /faal را انتخاب کنید.'
    bot.send_message(message.chat.id, welcome)

@bot.message_handler(commands=['faal'])
def faal_message(message):
    bot.send_message(message.chat.id, faal())


bot.infinity_polling()
