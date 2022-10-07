# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Введите натуральное число N: '))
factors = []
factor = 2
while N > 1:
    if N % factor == 0:
        factors.append(factor)
        N = N / factor
    else:
        factor+= 1

print(f'Список простых множителей числа => {factors}')