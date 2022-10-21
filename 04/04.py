# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0

import my_func
import itertools

k = my_func.input_int_number('Введите натуральную степень: ')
list_r = my_func.random_list(0, 101, k + 1)  # получаем список рандомных коэффициентов (функция в my_func)

template = ['x^'] * (k - 1) + ['x']
polynom = [[v, x, dg] for v, x, dg in itertools.zip_longest(list_r, template, range(k, 1, -1), fillvalue='') if x != 0]
for i in range(len(polynom) - 1):
    polynom[i].append(' + ')

polynom = list(itertools.chain(*polynom))
polynom.append(' = 0')

print("".join(map(str, polynom)))

with open('4.txt', 'w') as file:
     file.write("".join(map(str, polynom)))
