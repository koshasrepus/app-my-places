import telebot
from app_my_places.settings import TELEGRAM_TOKEN

bot = telebot.TeleBot(TELEGRAM_TOKEN)

bot.set_webhook(url='https://acf0c0c5c755.ngrok.io/telegram_bot_path')

@bot.message_handler(commands=['add'])
def hand_start_messate(message):
    print(message.text)
    bot.send_message(chat_id=message.chat.id, text='Hello World')

@bot.message_handler(commands=['list'])
def send_welcome(message):
    bot.reply_to(message,
                 ("Hi there, I am EchoBot.\n"
                  "I am here to echo your kind words back to you."))

def process_telegram_event(update_json):
    update = telebot.types.Update.de_json(update_json)
    bot.process_new_updates([update])

#bot = telebot.TeleBot(TELEGRAM_TOKEN)

#bot.set_webhook(url='http://faf5f0bff88a.ngrok.io')