# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

f_1 = open('4_1.txt', 'r')
f_2 = open('4_2.txt', 'r')

pol_1 = f_1.read().split()
pol_2 = f_2.read().split()

pol_3 = []

for i in range(0, len(pol_1) - 3, 2):
    pol_3.append(str(int(pol_1[i][:pol_1[i].find('x')]) + int(pol_2[i][:pol_2[i].find('x')])) + pol_1[i][pol_1[i].find(
        'x'):] + ' +')
pol_3.append(str(int(pol_1[-3]) + int(pol_2[-3])) + ' = 0')

print(' '.join(pol_3))

with open('5.txt', 'w') as f_3:
    f_3.write(' '.join(pol_3))

f_1.close()
f_2.close()
