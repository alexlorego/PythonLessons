# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

data = list(
    map(int, input('Введите последовательность чисел через пробел: ').split()))

result = []

for i in range(len(data)):
    count = 0
    for j in range(len(data)):
        if data[i] == data[j]:
            count += 1
    if count == 1:
        result.append(data[i])

print(data)
print(f'Уникальные элементы => {list(set(data))}')
print(f'Неповторяющиеся элементы => {result}')
