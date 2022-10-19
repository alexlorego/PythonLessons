import random
from datetime import datetime as DT
from datetime import timedelta

file = open('Phonebook.csv', 'w')
newrecord = "ID_Name_Surname_PhoneNumber_email_DateOfBirth\n"
file.writelines(newrecord)

name_list = ['Thomas', 'Olga', 'Walter', 'Anna', 'Inna', 'John', 'Tom', 'Kate', 'Elis', 'Andrey',
             'Vladimir', 'Natalia', 'Alex', 'Gregory', 'Igor', 'Anna', 'Maria', 'Sergei', 'Anastasia']
surname_list = ['Smith', 'Harrison', 'Morris', 'Goodman', 'Petrov', 'Kulik', 'Ray', 'Gusko', 'Chong'
                'Grant', 'Sivko', 'Parks', 'Grishko', 'Parsival', 'Anderson', 'Clinton', 'Planton']
e_mail_list = ['@gmail.com', '@yandex.ru', '@mail.ru']


def tel_number():
    tel_number = random.randint(79000000000, 80000000000)
    return str(tel_number)


def get_random_date():
    start_dt = DT.strptime('01.01.1960', '%d.%m.%Y')
    end_dt = DT.strptime('01.01.2002', '%d.%m.%Y')
    delta = end_dt - start_dt
    time_format = "%Y-%m-%d"
    dob = start_dt + timedelta(random.randint(0, delta.days))
    return f'{dob:{time_format}}'


def addrand_contact():
    s = ""
    name = random.choice(name_list)
    surname = random.choice(surname_list)
    e_mail = f'{name[0]}{surname}{random.choice(e_mail_list)}'
    s = ' '.join([name, surname, tel_number(), e_mail, get_random_date()])
    return s


def new_contacts(number):
    for i in range(number):
        a = f'{str(i + 1)} {addrand_contact()}\n'
        file.write(a)
    file.close()


new_contacts(50)
