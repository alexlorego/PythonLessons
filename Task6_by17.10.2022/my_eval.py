# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

import re

expr = '10+(5-4/4)*2+4+(1*2+12)/(3-1)'
s = re.findall(r"\d+|[()+\-*\/]", expr)

print(f"\n{expr} = ?")

def my_calc(s):
    calc = {'*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y}

    for i in range(s.count('*') + s.count('/')):
        for el in s:
            if str(el) in '*/':
                idx = s.index(el)
                res = calc[el](float(s[idx - 1]), float(s[idx + 1]))
                s[idx - 1:idx + 2] = [res]
                break

    for i in range(s.count('-') + s.count('+')):
        for el in s:
            if str(el) in '-+':
                idx = s.index(el)
                res = calc[el](float(s[idx - 1]), float(s[idx + 1]))
                s[idx - 1:idx + 2] = [res]
                break
    return s

for n in range(s.count('(')):
    if '(' and ')' in s:
        op = s.index('(')
        cl = s.index(')') + 1
        res = s[op+1:cl-1]
        my_calc(res)
        s[op:cl] = res
        
my_calc(s)

print(f'Считаем без библиотек => {s[0]}')
print(f'Считаем встроенной функцией => {eval(expr)}\n')