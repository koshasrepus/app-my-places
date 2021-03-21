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
    elif user.step == 2:
        bot.send_message(chat_id=message.chat.id, text='Отправьте локацию. Для этого нажмите Прикрепить > Геопозиция')
    elif user.step == 3:
        bot.send_message(chat_id=message.chat.id, text='Отправьте фотографию места')

    user.save()

def get_user(message):
    user = User.objects.filter(chat_id=message.chat.id)
    if user:
        return user.get()
    return None

def check_step(message, step):
    user = get_user(message)
    if user and user.step == step:
        return True
    return False

def check_step_1(message):
    return check_step(message, 1)

@bot.message_handler(func=check_step_1)
def hand_step_add_title_place(message):
    user = get_user(message)
    Palaces.objects.create(title=message.text, user=user)
    user.step = 2
    user.save()
    bot.send_message(chat_id=message.chat.id, text='Отправьте локацию. Для этого нажмите Прикрепить > Геопозиция')

def check_step_2(message):
 return check_step(message, 2)

@bot.message_handler(func=check_step_2)
@bot.message_handler(content_types=['location'])
def hand_step_add_location(message):
    user = get_user(message)
    #places = Palaces.objects.get(user=user, place_lat=None)
    places = Palaces.objects.filter(user=user, place_lat=None)[1]
    places.place_lat = message.location.latitude
    places.place_lon = message.location.longitude
    user.step = 3
    user.save()
    bot.send_message(chat_id=message.chat.id, text='Отправьте фотографию места')

def check_step_3(message):
    return check_step(message, 3)

@bot.message_handler(func=check_step_3)
@bot.message_handler(content_types=['photo'])
def hand_ste_add_photo(message):
    user = get_user(message)
    user.step = 1
    user.save()
    bot.send_message(chat_id=message.chat.id, text='Фотография добавлена')


@bot.message_handler(commands=['list'])
def hand_list_message(message):
    bot.send_message(chat_id=message.chat.id, text='command [list] is works')

@bot.message_handler(commands=['reset'])
def hand_reset_message(message):
    bot.send_message(chat_id=message.chat.id, text='command [reset] is works')


@bot.message_handler(content_types=['location'])
def hand_location(message):
    bot.send_message(chat_id=message.chat.id, text='command [location] is works')


def process_telegram_event(update_json):
    update = telebot.types.Update.de_json(update_json)
    bot.process_new_updates([update])

#bot = telebot.TeleBot(TELEGRAM_TOKEN)

#bot.set_webhook(url='http://faf5f0bff88a.ngrok.io')