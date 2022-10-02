# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

import random

s = []
for i in range(int(input('Размер списка: '))):
    s.append(round(random.uniform(0, 10),2))
print(s)

for i in range(len(s)):
    s[i] = s[i] - int(s[i])

print(f'=> {round(max(s) - min(s), 2)}')