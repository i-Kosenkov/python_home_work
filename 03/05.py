# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

import my_func

n = my_func.input_int_number('Input integer number: ')

# Fn = F(n + 1) + F(n + 2)
# Fn = F(n + 2) − F(n + 1)

f1 = f2 = 1
list = []
for i in range(-n - 1, n):
    if i < 0:
        f1, f2 = f2, f1 - f2
        list.insert(0, f2)
    elif i == 0 or i == 1:
        f2 = f1 = 1
        list.append(1)
    else:
        f1, f2 = f2, f1 + f2
        list.append(f2)

print(list)
