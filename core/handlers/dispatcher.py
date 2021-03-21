import telebot
from app_my_places.settings import TELEGRAM_TOKEN, DEBUG
from core.models import User, Palaces

bot = telebot.TeleBot(TELEGRAM_TOKEN)

if DEBUG:
    url = 'https://acf0c0c5c755.ngrok.io/telegram_bot_path'
else:
    url = 'https://app-my-places.herokuapp.com/telegram_bot_path'

bot.set_webhook(url=url)

@bot.message_handler(commands=['start'])
def hand_start_messate(message):
    resp = '/start - информация о боте\n/add - добавить локацию\n/list - просмотр 10 последних локаций\n' \
           '/reset - удалить все локации\nМожно отправить локацию, чтобы просмотреть сохранённые места в радиусе 500 метров'
    bot.send_message(chat_id=message.chat.id, text=resp)

@bot.message_handler(commands=['add'])
def hand_start_messate(message):
    user = User.objects.filter(chat_id=message.chat.id)

    user = user.get() if user else User.objects.create(chat_id=message.chat.id, step=1)

    if user.step == 1:
        bot.send_message(chat_id=message.chat.id, text='Введите название для новго места')
        user.step = 2
    elif user.step == 2:
        bot.send_message(chat_id=message.chat.id, text='Отправьте локацию. Для этого нажмите Прикрепить > Геопозиция')
        user.step = 3
    elif user.step == 3:
        bot.send_message(chat_id=message.chat.id, text='Отправьте фотографию места')
        user.step = 1

    user.save()





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