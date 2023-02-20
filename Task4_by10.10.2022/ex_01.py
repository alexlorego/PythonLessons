# Вычислить число c заданной точностью d
# Пример: при d = 0.001, π = 3.142,    10^(-1) ≤ d ≤10^(-10)

import math

def get_precision(inputData):
    data = str(inputData)
    if '.' not in data:
        return 0
    return len(data[data.index('.') + 1:])

pi = math.pi
d = input('Введите значение d: ')

print(round(pi, get_precision(d)))
print(f'{pi:.{get_precision(d)}f}')