# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random

s = []
for i in range(int(input('Размер списка: '))):
    s.append(random.randint(-10,10))

result = s[1::2]
print(s)
print(f'Элементы на нечетных позициях - {result}, сумма этих элементов = {sum(result)}')
