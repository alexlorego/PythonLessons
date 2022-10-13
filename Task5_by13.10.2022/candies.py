# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход

import random

def vs_player(candies):
    candies_left = candies
    player_1 = input('Введите имя первого игрока: ')
    player_2 = input('Введите имя второго игрока: ')
    print(f'\nВысыпаем конфеты...на кону аж {candies_left}!')

    lots = random.randint(1, 2)
    if lots == 1:
        first = player_1
        second = player_2
    else:
        first = player_2
        second = player_1
    move = first

    while candies_left > 0:
        if move == first:
            take = int(input(f'{first}, твой ход! Сколько конфет берешь? => '))
            while take not in range(1, 29) or take > candies_left:
                take = int(
                    input('Столько взять не получится! Попробуй еще раз: '))
            candies_left -= take
            if candies_left != 0:
                print(f'Конфет осталось: {candies_left}')
                move = second
            else:
                print(f'Поздравляем, {first}! Ты ПОБЕДИЛ!')

        if move == second:
            take = int(
                input(f'{second}, твой ход! Сколько конфет берешь? => '))
            while take not in range(1, 29) or take > candies_left:
                take = int(
                    input('Столько взять не получится! Попробуй еще раз: '))
            candies_left -= take
            if candies_left != 0:
                print(f'Конфет осталось: {candies_left}')
                move = first
            else:
                print(
                    f'\nКонфеты закончились! Поздравляем, {second}! Ты ПОБЕДИЛ!')


def vs_AI(candies):
    candies_left = candies
    player = input('Игрок, как тебя зовут? => ')
    bot = "Бот_Валера"
    print(
        f'\nВысыпаем конфеты...на кону аж {candies_left}!')

    lots = random.randint(1, 2)
    if lots == 1:
        move = 1
        print(f'Первым ходит {player}')
    else:
        move = 0
        bot = "Бот_С_Мозгами"        
        print(f'Первым ходит {bot}')

    while candies_left > 0:
        if move == 1:
            take = int(
                input(f'{player}, твой ход! Сколько конфет берешь? => '))
            while take not in range(1, 29) or take > candies_left:
                take = int(
                    input('Столько взять не получится! Попробуй еще раз: '))
            candies_left -= take
            if candies_left != 0:
                print(f'Конфет осталось: {candies_left}')
                move -= 1
            else:
                print(f'Поздравляем, {player}! Ты ПОБЕДИЛ!')

        if move == 0 and bot == "Бот_Валера":
            if candies_left > 28:
                take = random.randint(1, 28)
                print(f'{bot} подумал и взял => {take}')
            else:
                take = candies_left
                print(f'{bot} забрал все')
            candies_left -= take
            if candies_left != 0:
                print(f'Конфет осталось: {candies_left}')
                move += 1
            else:
                print(f'\nУпс! Кажется {bot} победил. Игрок, не отчаивайся!')

        if move == 0 and bot == "Бот_С_Мозгами":
            winnumber = 29
            if winnumber < candies_left:
                take = candies_left % winnumber
                print(f'{bot} подумал и взял => {take}')
                candies_left -= take
            else:
                take = candies_left
                candies_left -= take
                print(f'{bot} забрал все')
            if candies_left != 0:
                print(f'Конфет осталось: {candies_left}')
                move += 1
            else:
                print(f'\nОчевидно {bot} победил. Игрок, у тебя не было шансов.')


welcome = ('\n***Игра с конфетами*** \n'
           "Правила: На столе лежит 2021 конфета, за один ход можно забрать не более чем 28 конфет.\n"
           "Все конфеты оппонента достаются сделавшему последний ход. \nНачнем! =================>")
print(welcome)

mod = int(input(
    '\nВыберите режим игры: \n1 - против другого игрока\n2 - против ИИ\nЧто решил?: '))
while mod not in range(1, 3):
    mod = int(input('Выбери один из двух вариантов: '))

if mod == 1:
    print('\nИгроки, приготовиться! Мы начинаем!')
    vs_player(2021)
else:
    print('\nИграем с ИИ! Поехали!')
    vs_AI(2021)
