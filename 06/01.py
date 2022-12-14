# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

# через встроенную функцию
# print(eval(input('--> ')))

import re

res = []
example = re.split('(\W)', input('-> '))  # получаем список элементов вместо строки

i = 0
while i < len(example):  # убираем - и + из элементов списка
    if example[i] == '-':
        res.append(0 - float(example[i + 1]))  # в новый список --> число с минусом
        i += 2
    elif example[i] == '+':
        res.append(float(example[i + 1]))  # в новый список --> число без плюса
        i += 2
    else:
        res.append(example[i])  # в новый список --> / * число
        i += 1

for k in range(len(res)):  # выполняем деление
    if res[k] == '/':
        res[k + 1] = (float(res[k - 1]) / float(res[k + 1]))  # во второе значение записываем результат деления
        res[k - 1] = res[k] = 0  # вместо первого значений и знака записываем нули

res = [x for x in res if x != 0]  # удаляем нули из списка

for j in range(len(res)):  # выполняем умножение
    if res[j] == '*':
        res[j + 1] = (float(res[j - 1]) * float(res[j + 1]))
        res[j - 1] = res[j] = 0

res = [x for x in res if x != ''] # удаляем пустые элементы (появляются если первое значение с минусом)

print(sum(map(float, res)))  # печатаем сумму элементов списка переведя все во float
