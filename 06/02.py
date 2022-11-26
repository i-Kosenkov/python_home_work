# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности,
# список повторяемых и убрать дубликаты из заданной последовательности.

numbers = [1, 2, 3, 5, 1, 5, 3, 10]

print('Уникальные:', list(i for i in numbers if numbers.count(i) <= 1))
print('Пвторяющиеся:', list(set(i for i in numbers if numbers.count(i) > 1)))
print('Без дублей:', list(set(numbers)))
