#  Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
#  Позиции хранятся в файле file.txt в одной строке одно число.

import random

s = []
N = int(input('Размер списка: '))
for i in range(N):
    s.append(random.randint(-N,N))

pos = []
f = open('file.txt')
for line in f:
    pos.append(int(line))

result = 1
for res in range (len(pos)):
    result *= s[pos[res]]

print(s)
print(f'индексы элементов: {pos}')
print(f'Произведение элементов = {result}')