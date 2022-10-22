# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('04.txt', 'r') as file:
    text = file.readline()
    print(text)

count = 1
rle = []
for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1
    else:
        rle.append(text[i] + '¬' + str(count))
        count = 1
rle.append(text[i] + '¬' + str(count))

zip_rle = '¡'.join(rle)
print(zip_rle)

with open('04-zip.txt', 'w') as zip_file:
    zip_file.write(zip_rle)

# Расшифровка zip файла
with open('04-zip.txt', 'r') as new_file:
    interpretation = str()
    for item in new_file.readline().split('¡'):
        part_1, part_2 = item.split('¬')
        interpretation += (str(part_1) * int(part_2))
    print(interpretation)

