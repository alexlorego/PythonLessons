# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

s = []
for i in range(int(input('Размер списка: '))):
    s.append(random.randint(-10,10))

res = []
for i in range(0, int(len(s)/2 + 0.5)):
    res.append(s[i] * s[-1 - i])

print(s)
print(f'=> {res}')