# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def InputNumbers(inputText):
    checked = False
    while not checked:
        try:
            number = int(input(f"{inputText}"))
            checked = True
        except ValueError:
            print("Ошибка ввода! Нужно вводить число")
    return number

def CheckDays(day):
    if 0 < day < 6:
       print('>>> это рабочий день')
    elif day == 6 or day == 7:
       print('>>> это выходной')
    elif day not in range(1, 8):
       print('указанная цифра не обозначает день недели')

CheckDays(InputNumbers('Введите номер дня недели: '))

