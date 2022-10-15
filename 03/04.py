# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

import my_func

n = my_func.input_int_number('Input integer number: ')
double = str()
while n > 0:
    double = double + str(n % 2)
    n = n // 2
print('Binary number = ', double[::-1])
