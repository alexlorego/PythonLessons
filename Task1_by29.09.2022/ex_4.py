# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def FindXYinQuarter(quater):
    if quater == 1:
        print('x > 0 and y > 0')
    elif quater == 2:
        print('x < 0 and y > 0')  
    elif quater == 3:
        print('x < 0 and y < 0')
    elif quater == 4:
        print('x > 0 and y < 0')

quater = int(input("Введите номер четверти (1, 2, 3 или 4): "))
while quater not in range(1,5):
     print('Ошибка! Четверти всего 4, других нет')
     quater = int(input("Введите номер четверти (1, 2, 3 или 4): "))
FindXYinQuarter(quater)