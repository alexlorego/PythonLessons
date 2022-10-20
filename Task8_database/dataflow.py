dep_codes = {"1": "SD",
             "2": "FD",
             "3": "HRD",
             "4": "MD",
             "5": "PD"}


def new_employee():
    name = input('Введите Имя: ')
    sname = input('Фамилия: ')
    mail = f'{name[0]}{sname}@mypy.ru'
    d = input(
        'Выберите отдел: Продаж(1)|Финансов(2)|Кадров(3)|Маркетинга(4)|Продукта(5) ^')
    while int(d) not in range(1, 5):
        d = input('Выберите одну из отделов: ')
    d_code = dep_codes[d]

    p = input(
        'Выберите позицию в отделе: Руководитель(1)|Менеджер(2)|Специалист(3) ^')
    while int(p) not in range(1, 4):
        p = input('Выберите доступную позицию: ')

    dp_code = f'{d_code}{p}'

    nemp = ' '.join([name, sname, mail, dp_code])
    file = open('company_employees.csv', 'r')
    last = file.readlines()[-1].split()
    next_id = f'{int(last[0]) + 1}'
    file.close()

    f = open('company_employees.csv', 'a+')
    ad = f'{next_id} {nemp}\n'
    f.write(ad)
    f.close()


def del_employee(id):
    with open('company_employees.csv', 'r') as file:
        db = file.readlines()

    with open('company_employees.csv', 'w') as file1:
        for line in db:
            if id not in line:
                file1.write(line)


def yn_check():
    list_yes = ["yes", "y", "да", "д", "YES", "Y", "ДА", "Д",
                "+", "++", "+++", "++++", "++++", "конечно", "КОНЕЧНО"]
    test = str(
        input('Вы действительно хотите удалить этого сотрудника? [да/нет]: ')).lower()
    if test in list_yes:
        return True
    else:
        return False
