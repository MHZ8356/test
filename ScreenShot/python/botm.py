from tkinter import N
from prompt_toolkit import HTML
from telebot import TeleBot
from datetime import datetime
import pytz

bot_token = "5519025046:AAHGFp0_Edvb8v0cfTk_UMyDbQ_mv6yopa4"
bot = TeleBot(bot_token, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


bot.infinity_polling()
""" try:
except:
    tz = pytz.timezone("Asia/Tehran")
    td = datetime.now(tz)
    print(f"Except: {td.strftime('%Y-%m-%d %H:%M:%S')}")
    pass
 """