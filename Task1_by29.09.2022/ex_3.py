# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def inputCoordinates():
    xy = ['X', 'Y']
    coordinates = []
    for i in range(2):
        number = float(input(f"Введите {xy[i]} координату: "))
        while number==0:
            print(f'Ошибка! {xy[i]} не должен быть равен 0')
            number = float(input(f"Введите {xy[i]} координату: "))
        coordinates.append(number)
    return coordinates   

def checkCoordinates(xy):
    quarter = 4
    if xy[0] > 0 and xy[1] > 0:
        quarter = 1
    elif xy[0] < 0 and xy[1] > 0:
        quarter = 2
    elif xy[0] < 0 and xy[1] < 0:
        quarter = 3
    print(f"Точка находится в {quarter} четверти плоскости")

checkCoordinates(inputCoordinates())