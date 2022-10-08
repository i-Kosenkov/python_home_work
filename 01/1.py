# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

n = int(input('Input day number: '))
print('Wrong day number' if 7 < n or n < 1 else 'Yes' if n == 6 or n == 7 else 'No')