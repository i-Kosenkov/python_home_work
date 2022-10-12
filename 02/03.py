# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

s = 0
print(*(s := s + (1 + 1 / i) ** i for i in range(1, int(input('Number: ')) + 1)), sep='\r')

# n = int(input('Number: '))
# s = 0
# for i in range(1, n + 1):
#     s += (1 + 1 / i) ** i
# print(s)