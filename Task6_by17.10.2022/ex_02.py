# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности, список повторяемых и убрать дубликаты из заданной последовательности.

import random

data = []
for i in range(int(input('Размер списка: '))):
    data.append(random.randint(0,10))

non_reps = []
reps = []

for i in data:
    if data.count(i) == 1:
        non_reps.append(i)
    else:
        if i not in reps:
            reps.append(i)

print(data)
print(f'Уникальные элементы (без дубликатов) => {list(set(data))}')
print(f'Неповторяющиеся элементы => {non_reps}')
print(f'Повторяющиеся элементы => {reps}')