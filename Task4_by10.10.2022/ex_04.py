# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:  - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k_list = []
for i in range(int(input('Введите натуральную степень k: ')) + 1):
   k_list.append(random.randint(0,100))
print(k_list)

poly = []
power = len(k_list) - 1
for el in k_list:
    if el != 0:
        if power > 1:
            item = f'{el}x^{power}'
            poly.append(item)
            power-= 1
        elif power == 1:
           item = f'{el}x'
           poly.append(item)
           power-= 1
        elif power == 0:
           item = f'{el}'
           poly.append(item) 
    else:
        power-= 1

polynom = ' + '.join(poly) + ' = 0'
print(polynom)

with open('ex4.txt', 'w') as file:
    file.write(polynom)
    


