import view as v


def search(key_word):
    find = False
    with open('Phonebook.csv', 'r') as database:
        for line in database:
            if key_word in line:
                v.show_contact(line)
                find = True
        if not find:
            print('Совпадений не найдено\n')
