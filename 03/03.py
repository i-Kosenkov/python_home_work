# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import my_func

n = my_func.input_int_number('Input list lenght: ')
list = my_func.random_list_float_numbers(n, 0, 10, 2)
print(list)

maximum = round(max(i - int(i) for i in list), 2)
minimum = round(min(i - int(i) for i in list), 2)

print(f'Max({maximum}) - Min({minimum}) = {round(maximum - minimum, 2)}')
