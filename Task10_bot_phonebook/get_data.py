import random


file = open('botdatabase.csv', 'w')
newrecord = "ID_Name_Surname_PhoneNumber_Comments\n"
file.writelines(newrecord)

name_list = ['Thomas', 'Olga', 'Walter', 'Anna', 'Inna', 'John', 'Tom', 'Kate', 'Elis', 'Andrey',
             'Vladimir', 'Natalia', 'Alex', 'Gregory', 'Igor', 'Anna', 'Maria', 'Sergei', 'Anastasia']
surname_list = ['Smith', 'Harrison', 'Morris', 'Goodman', 'Petrov', 'Kulik', 'Ray', 'Gusko', 'Chong'
                'Grant', 'Sivko', 'Parks', 'Grishko', 'Parsival', 'Anderson', 'Clinton', 'Planton']


def tel_number():
    tel_number = random.randint(79000000000, 80000000000)
    return str(tel_number)


def addrand_contact():
    s = ""
    name = random.choice(name_list)
    surname = random.choice(surname_list)
    s = ' '.join([name, surname, tel_number()])
    return s


def new_contacts(number):
    for i in range(number):
        a = f'{str(i + 1)} {addrand_contact()}\n'
        file.write(a)
    file.close()

new_contacts(25)
