# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import my_func

n = my_func.input_int_number('Input list lenght: ')
list = my_func.random_list(n, 10)
print(list)

multiplication = []
lenght = int(len(list) / 2) if len(list) % 2 == 0 else int(len(list) / 2 + 1)
for i in range(lenght):
    multiplication.append(list[i] * list[-i - 1])
print(multiplication)