# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import my_func

n = my_func.input_int_number('Input list lenght: ')
list = my_func.random_list(n, 100)
print(list)

sum = 0
print(*(sum := sum + (list[i]) for i in range(1, len(list), 2)), sep='\r')
