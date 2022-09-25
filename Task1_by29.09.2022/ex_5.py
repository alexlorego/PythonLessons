# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def inputPointCoordinates(text):
    print(text)
    xy = ['X', 'Y']
    point = []
    for i in range(2):
        checked = False
        while not checked:
            try:
                number = int(input(f'Введите координату по {xy[i]}: '))
                point.append(number)
                checked = True
            except ValueError:
                print('Ошибка! Введите целое число')
    return point

def FindDistance(pointA, pointB):
    distance = ((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2) ** (0.5)
    return distance

pointA = inputPointCoordinates('Задайте координаты точки А')
pointB = inputPointCoordinates('Задайте координаты точки B')

print(f"Расстояние между точками А и В -> {FindDistance(pointA, pointB):.{2}f}")