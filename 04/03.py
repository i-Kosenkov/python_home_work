# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import my_func

list = my_func.random_list(0, 10, 10)
print(list)
newlist = []
for i in range(len(list)):  # находим повторяющиеся элементы списка
    for j in range(i + 1, len(list)):
        if list[i] == list[j]:
            newlist.append(list[i])  # записываем их в новый список
            break

newlist = [x for x in list if x not in newlist]
print(newlist)
