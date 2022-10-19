import view
import find_contact as fc
import sys
import add_contact as ac


def main_menu():
    print('--- Welcome to PythonPhoneBook 0.1.1 ---\n')
    print('PhBook меню: \n'
          '1 - Найти контакт\n'
          '2 - Добавить новый контакт\n'
          '3 - Вывести все контакты\n'
          '4 - Выход\n')

    opt = int(input('Выберите опцию: '))
    while opt not in range(1, 5):
        opt = int(input('Выберите одну из доступных опций: '))

    if opt == 1:
        find = input('Поиск контакта. Укажите имя или фамилию для поиска:  ')
        fc.search(find)

    elif opt == 2:
        var = int(input('Добавить в ручную(1) или произвольно(2)? => '))
        while var not in range(1, 3):
            var = int(input('В ручную(1) или авто(2)?: '))

        if var == 1:
            ac.new_contact()
            view.last_add()
        else:
            ac.new_random()
            view.last_add()

    elif opt == 3:
        view.contacts()

    if opt == 4:
        sys.exit()


def start():
    while True:
        main_menu()
