# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open("file1.txt", "r") as file1:
    polynom1 = ''.join(
        [el for el in file1.read().split() if el not in ('=', '0')])

with open("file2.txt", "r") as file2:
    polynom2 = ''.join(
        [el for el in file2.read().split() if el not in ('=', '0')])

result = f"({polynom1}) + ({polynom2}) = 0"

with open('result.txt', 'w') as file3:
    file3.write(result)

print(result)

# библиотека для работы с многочленами у меня не подгрузилась.
# Решение, показанное на семинаре, я понял, но полностью самостоятельно воспроизвести его наверное не смогу.
