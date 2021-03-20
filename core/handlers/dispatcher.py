import telebot
from app_my_places.settings import TELEGRAM_TOKEN

bot = telebot.TeleBot(TELEGRAM_TOKEN)

bot.set_webhook(url='https://acf0c0c5c755.ngrok.io/telegram_bot_path')

@bot.message_handler(commands=['start'])
def hand_start_messate(message):
    resp = '/start - информация о боте\n/add - добавить локацию\n/list - просмотр 10 последних локаций\n' \
           '/reset - удалить все локации\nМожно отправить локацию, чтобы просмотреть сохранённые места в радиусе 500 метров'
    bot.send_message(chat_id=message.chat.id, text=resp)

@bot.message_handler(commands=['add'])
def hand_start_messate(message):
    bot.send_message(chat_id=message.chat.id, text='command [add] is works')

@bot.message_handler(commands=['list'])
def hand_list_message(message):
    bot.send_message(chat_id=message.chat.id, text='command [list] is works')

@bot.message_handler(commands=['reset'])
def hand_reset_message(message):
    bot.send_message(chat_id=message.chat.id, text='command [reset] is works')


@bot.message_handler(content_types=['location'])
def handl_location(message):
    bot.send_message(chat_id=message.chat.id, text='command [location] is works')


def process_telegram_event(update_json):
    update = telebot.types.Update.de_json(update_json)
    bot.process_new_updates([update])

#bot = telebot.TeleBot(TELEGRAM_TOKEN)

#bot.set_webhook(url='http://faf5f0bff88a.ngrok.io')