from telebot import TeleBot 
from Method import ti, csh

bot_token = "5519025046:AAHGFp0_Edvb8v0cfTk_UMyDbQ_mv6yopa4"
bot = TeleBot(bot_token, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام، لطفا لینک توییت خود را ارسال کنید.")


@bot.message_handler(regexp="http(?:s)?:\/\/(?:www\.)?twitter\.com\/([a-zA-Z0-9_]+)\/status\/.*")
def send_tweetdata(message):
    user_id = message.chat.id
    tweet_id = ti(message.text)
    bot.send_message(chat_id=user_id, text="لطفا کمی صبر کنید ..")
    photo = csh(tweet_id)
    bot.send_photo(user_id, photo)


bot.infinity_polling()
