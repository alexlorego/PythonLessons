# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def factorial(input):
    f = 1
    for i in range(2, input + 1):
      f *= i
    return f

print([
    factorial(i) for i in range(1, int(input('N:')) + 1)
])
