# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import my_func

n = my_func.input_int_number('Input list lenght: ')
list = my_func.random_list_float_numbers(n, 0, 10, 2)
print(list)

print('Max = ', round(max(i - int(i) for i in list), 2))  # print maximum fractional part
print('Min = ', round(min(i - int(i) for i in list), 2))  # print minimum fractional part

print('Max - Min = ', round(max(i - int(i) for i in list) - min(i - int(i) for i in list), 2))
