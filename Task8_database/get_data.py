import random

name_list = ['Thomas', 'Olga', 'Walter', 'Anna', 'Inna', 'John', 'Tom', 'Kate', 'Elis', 'Andrey',
             'Vladimir', 'Natalia', 'Alex', 'Gregory', 'Igor', 'Anna', 'Maria', 'Sergei', 'Anastasia']
surname_list = ['Smith', 'Harrison', 'Morris', 'Goodman', 'Petrov', 'Kulik', 'Ray', 'Gusko', 'Chong',
                'Grant', 'Sivko', 'Parks', 'Grishko', 'Parsival', 'Anderson', 'Clinton', 'Planton']
position = ['HRD1', 'HRD2', 'HRD3', 'HRD3', 'MD1', 'MD2', 'MD3', 'MD3', 'SD1', 'SD2', 'SD3', 'SD3',
            'PD1', 'PD2', 'PD3', 'PD3', 'FD1', 'FD2', 'FD3', 'FD3', 'GD4']


def add_employee():
    s = ""
    name = random.choice(name_list)
    surname = random.choice(surname_list)
    e_mail = f'{name[0]}{surname}@mypy.ru'
    pos = position.pop()
    s = ' '.join([name, surname, e_mail, pos])
    return s


def new_base():
    with open('company_employees.csv', 'a+') as file:
        for i in range(len(position)):
            a = f'{str(i + 101)} {add_employee()}\n'
            file.write(a)


def get_position(code):
    if code[-1].isdigit():
        pos = code[-1]
        dep = code.rstrip(pos)
    else:
        pos = "ген.директор"
        dep = code

    with open('departments.csv', 'r', encoding='utf-8') as data1:
        for line in data1:
            if dep in line:
                d = line.split()[1]

    with open('positions.csv', 'r', encoding='utf-8') as data2:
        p = ""
        for line in data2:
            if pos in line:
                p = line.split()[1]

    res = d + ' ' + p

    return res


def data_export():
    with open('company_employees.csv', "r") as ins:
        array = []
        lines = ins.readlines()[1:]
        for line in lines:
            pos_id = get_position(line.split()[-1])
            l = line.split()
            l[-1] = pos_id
            r = " ".join(l)
            array.append(r.split())
    return array


def create_files():
    with open('departments.csv', 'w', encoding='utf-8') as dep:
        lines = ["КОД_Структурное_подразделение \n", "GD MyPython.Co \n", "SD отдел_продаж \n", "FD отдел_финансов \n",
                 "HRD отдел_кадров \n", "MD отдел_маркетинга \n", "PD отдел_продукта \n"]
        for line in lines:
            dep.write(line)

    with open('positions.csv', 'w', encoding='utf-8') as po:
        lines = ["КОД_Позиция \n", "4 ген.директор \n","1 руководитель \n",
                 "2 менеджер \n", "3 специалист \n"]
        for line in lines:
            po.write(line)

    with open('company_employees.csv', 'w') as file:
        newrecord = "ID_Name_Surname_CorporateMail_Position\n"
        file.writelines(newrecord)

#create_files()
#new_base()

