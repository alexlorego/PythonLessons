import view as v
import sys
from filter_db import search as s
from filter_db import dep_choice as dc
from filter_db import pos_choice as pc
from get_data import data_export as de
from dataflow import new_employee as ne
from dataflow import yn_check as yn
from dataflow import del_employee as delemp


def main_menu():
    print('--- База сотрудников MyPython.Co ---')
    print('1 - Найти сотрудника\n'
          '2 - Сортировать по отделам\n'
          '3 - Сортировать по должностям\n'
          '4 - Вывести всю базу на экран\n'
          '5 - Добавить сотрудника\n'
          '6 - Удалить сотрудника\n'
          '7 - Выход')

    opt = int(input('Выберите опцию: '))
    while opt not in range(1, 8):
        opt = int(input('Выберите одну из доступных опций: '))

    if opt == 1:
        find = input(
            'Поиск сотрудника. Укажите имя, фамилию или ID для поиска:  ')
        v.show_data(s(find))

    elif opt == 2:
        v.show_dep()
        var = input('Выберите отдел: ')
        while int(var) not in range(1, 6):
            var = int(input('Повторите выбор: '))
        filter_dep = dc(var)
        v.show_data(s(filter_dep))

    elif opt == 3:
        v.show_pos()
        var = input('Выберите позицию: ')
        while int(var) not in range(1, 5):
            var = int(input('Повторите выбор: '))
        filter_pos = pc(var)
        v.show_data(s(filter_pos))

    elif opt == 4:
        v.show_data(de())

    elif opt == 5:
        ne()
        print("**Новый сотрудник успешно добавлен в базу компании**")

    elif opt == 6:
        find = input(
            'Укажите ID сотрудника для удаления:  ')
        v.show_data(s(find))
        if yn() == True:
            delemp(find)
            print("**Сотрудник успешно удален из базы компании**")
        else:
            main_menu()

    if opt == 7:
        sys.exit()


def start():
    while True:
        main_menu()
