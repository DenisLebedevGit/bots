from random import randint, choice
import configparser
from requests import get
from bs4 import BeautifulSoup
from threading import Timer
from telebot import TeleBot

config = configparser.ConfigParser()
initial = config.read('setting.ini')
token = config.get('token', 'token')
webpage_url = config.get('tgname', 'website')
Bot = TeleBot(token)
id = config.get('tgname', 'id').split()


def send_compliment():
    Timer(2.0, send_compliment).start()
    message = get_random_compliment()
    for acc in id:
        Bot.send_message(acc, message)
        print(acc)
#    Bot.send_message(474010999, get_random_compliment())
#    Bot.send_message(362709557, get_random_compliment())
#    Bot.send_message(156597242, get_random_compliment())


def get_random_compliment():
    random_page_number = str(randint(1, 42))
    webpage = get(webpage_url + random_page_number).text
    tags = BeautifulSoup(webpage, 'html.parser').find_all('a')
    compliments = []
    for tag in tags:
        tag_txt = tag.get_text()
        if tag_txt == 'Назад':
            break
        compliments.append(tag_txt)
    return choice(compliments[5:])


send_compliment()
