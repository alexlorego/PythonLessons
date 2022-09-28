# Реализуйте алгоритм перемешивания списка.

import random

s = []
for i in range(int(input('Размер списка: '))):
    s.append(random.randint(0,10))

print(f'Изначальный список:{s}')
random.shuffle(s)
print(f'Перемешанный список:{s}')