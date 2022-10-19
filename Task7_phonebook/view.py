def show_contact(data):
    r = data.split()
    print(
        f'=> Имя_{r[1]} Фамилия_{r[2]} Дата рождения:{r[5]} тел.:{r[3]} e-mail: {r[4]}\n')


def contacts():
    file = open('Phonebook.csv', 'r')
    for line in file:
        print(line, end='')
    file.close()


def last_add():
    file = open('Phonebook.csv', 'r')
    l = file.readlines()[-1].split()
    print('Добавлен новый контакт:')
    print(
        f'++ Имя_{l[1]} Фамилия_{l[2]} Дата рождения:{l[5]} тел.:{l[3]} e-mail: {l[4]}\n')
    file.close()