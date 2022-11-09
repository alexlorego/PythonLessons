import telebot
from telebot import TeleBot
from telebot import types

TOKEN = "СЮДА ВПИСАТЬ ТОКЕН"

bot = TeleBot(TOKEN)

name = ''
surname = ''
tnumber = ''
comment = ''
c_id = ''


@bot.message_handler(commands=['start'])
def start(message):
    kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton('Find Contact')
    key2 = types.KeyboardButton('Add New Contact')
    key3 = types.KeyboardButton('Delete Contact')
    key4 = types.KeyboardButton('Show all contacts')

    kboard.add(key1, key2, key3, key4)

    bot.send_message(message.chat.id, '** {0.first_name}, добро пожаловать в MyPhonebook **'.format(
        message.from_user), reply_markup=kboard)


@bot.message_handler(content_types=['text'])
def bot_menu(message):
    if message.text == 'Find Contact':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Back to Main Menu')
        kboard.add(back)

        bot.send_message(message.chat.id, 'Укажите имя, фамилию или телефон и я постараюсь вам помочь:  ',
                         reply_markup=kboard)

        bot.register_next_step_handler(message, find_contact)

    elif message.text == 'Add New Contact':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Back to Main Menu')
        kboard.add(back)
        bot.send_message(message.chat.id, 'Окей, давай добавим новый контакт. Приступим!',
                         reply_markup=kboard)
        bot.send_message(message.chat.id, "Укажи имя: ")
        bot.register_next_step_handler(message, process_name_step)

    elif message.text == 'Delete Contact':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Back to Main Menu')
        kboard.add(back)
        bot.send_message(message.chat.id, 'Удаляем контакт..',
                         reply_markup=kboard)
        bot.send_message(
            message.chat.id, "Укажи имя или фамилию, надо понять кого удаляем  ")
        bot.register_next_step_handler(message, process_del_contact)

    if message.text == 'Show all contacts':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Back to Main Menu')
        kboard.add(back)

        bot.send_message(message.chat.id, '----- Мои Контакты -----',
                         reply_markup=kboard)

        with open('botdatabase.csv', 'r', encoding='UTF-8') as db:
            db_out = db.readlines()
            for line in db_out:
                bot.send_message(message.chat.id, {line})

    elif message.text == 'no':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('Find Contact')
        key2 = types.KeyboardButton('Add New Contact')
        key3 = types.KeyboardButton('Delete Contact')
        key4 = types.KeyboardButton('Show all contacts')

        kboard.add(key1, key2, key3, key4)

        bot.send_message(message.chat.id, 'Отмена удаления. Возврат в главное меню.'.format(
            message.from_user), reply_markup=kboard)

    elif message.text == 'yes':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('Find Contact')
        key2 = types.KeyboardButton('Add New Contact')
        key3 = types.KeyboardButton('Delete Contact')
        key4 = types.KeyboardButton('Show all contacts')

        kboard.add(key1, key2, key3, key4)

        with open('botdatabase.csv', 'r', encoding='UTF-8') as file:
            db = file.readlines()

        with open('botdatabase.csv', 'w', encoding='UTF-8') as file1:
            for line in db:
                if c_id not in line:
                    file1.write(line)

        bot.send_message(message.chat.id, 'Контакт успешно удален!'.format(
            message.from_user), reply_markup=kboard)

    elif message.text == 'Back to Main Menu':
        kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('Find Contact')
        key2 = types.KeyboardButton('Add New Contact')
        key3 = types.KeyboardButton('Delete Contact')
        key4 = types.KeyboardButton('Show all contacts')

        kboard.add(key1, key2, key3, key4)

        bot.send_message(message.chat.id, '** {0.first_name}, добро пожаловать в MyPhonebook **'.format(
            message.from_user), reply_markup=kboard)


def find_contact(message):
    key_word = message.text
    find = False
    with open('botdatabase.csv', 'r', encoding='UTF-8') as database:
        for line in database:
            if key_word in line:
                bot.send_message(message.chat.id, {line})
                find = True
        if not find:
            bot.send_message(message.chat.id, "Совпадений не найдено")
            bot.register_next_step_handler(message, find_contact)


def process_name_step(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, 'А Фамилия?: ')
    bot.register_next_step_handler(message, process_surname_step)


def process_surname_step(message):
    global surname
    surname = message.text
    bot.send_message(
        message.chat.id, f'Введи номер телефона нового контакта: ')
    bot.register_next_step_handler(message, process_tnumber_step)


def process_tnumber_step(message):
    global tnumber
    tnumber = message.text
    bot.send_message(message.chat.id, f'Добавим комментарий:')
    bot.register_next_step_handler(message, process_comment_step)


def process_comment_step(message):
    global comment
    comment = message.text
    nc = ' '.join([name, surname, tnumber, f'>> {comment}'])

    with open('botdatabase.csv', 'r', encoding='UTF-8') as db:
        dbase = db.readlines()
        print(dbase)
        last = dbase[-1].split()
        next_id = f'{int(last[0]) + 1}'

    with open('botdatabase.csv', 'a+', encoding='UTF-8') as db:
        ad = f'{next_id} {nc}\n'
        db.write(ad)

    bot.send_message(message.chat.id, 'Контакт успешно добавлен!')


def process_del_contact(message):
    key_word = message.text
    find = False
    global c_id
    c_id = ''
    with open('botdatabase.csv', 'r', encoding='UTF-8') as database:
        for line in database:
            if key_word in line:
                bot.send_message(message.chat.id, {line})
                find = True
        if not find:
            bot.send_message(message.chat.id, "Совпадений не найдено")
    bot.send_message(
        message.chat.id, f'Введи ID контакта из списка, который хочешь удалить:')
    bot.register_next_step_handler(message, process_check_if)


def process_check_if(message):
    global c_id
    c_id = message.text

    kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    y = types.KeyboardButton('yes')
    n = types.KeyboardButton('no')
    kboard.add(y, n)

    bot.send_message(message.chat.id, 'Уверены, что хотите удалить указанный контакт?',
                     reply_markup=kboard)


if __name__ == '__main__':
    bot.infinity_polling()
