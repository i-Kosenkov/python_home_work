# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

n = int(input('Количество элементов: '))
lst_rnd = random.sample(range(-n, n), n)

file = open('file.txt')
file = file.readlines()

summa = 0
for i in range(len(file)):
    if int(file[i]) < len(lst_rnd):
        summa += lst_rnd[int(file[i])]
        n = 'ok'  # триггер указывает, что есть найденные значения (использую в if)
        lst_rnd[int(file[i])] = str(lst_rnd[int(file[i])])  # выделяю в списке '' найденные значения
                                                            # (исключительно для визуального удобства)
print(lst_rnd, '=', summa if n == 'ok' else 'Значения не найдены')
