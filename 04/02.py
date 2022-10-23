# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

import my_func

n = my_func.input_int_number('Введите натуральное число: ')
i = 2
list = []
while True:
    if n % i == 0:
        list.append(i)
        n /= i
        i = 2
    elif n == 1:
        break
    else:
        i += 1

print('Число простое' if len(list) == 1 else f'Простые множители числа: {list}')
