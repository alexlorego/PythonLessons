# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('введите число: '))
fibolist = [0]

for i in range(1, n + 1):
    fibolist.insert(0, (-1)**(i + 1) * fibonacci(i))
    fibolist.append(fibonacci(i))

print(fibolist)