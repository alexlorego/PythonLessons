import get_data as gd


def new_contact():
    name = input('Введите Имя: ')
    sname = input('Фамилия: ')
    dob = input('Дата рождения: ')
    tel = input('Телефон: ')
    mail = input('Эл.почта: ')

    nc = ' '.join([name, sname, tel, mail, dob])
    file = open('Phonebook.csv', 'r')
    last = file.readlines()[-1].split()
    next_id = f'{int(last[0]) + 1}'
    file.close()

    f = open('Phonebook.csv', 'a+')
    ad = f'{next_id} {nc}\n'
    f.write(ad)
    f.close()


def new_random():
    nc = gd.addrand_contact()
    file = open('Phonebook.csv', 'r')
    last = file.readlines()[-1].split()
    next_id = f'{int(last[0]) + 1}'
    file.close()

    f = open('Phonebook.csv', 'a+')
    ad = f'{next_id} {nc}\n'
    f.write(ad)
    f.close()
