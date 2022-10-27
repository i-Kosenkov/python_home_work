# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('04.txt', 'r') as file:
    text = file.readline()
    print(text)

rle = str()
count = 1

for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1
        if count == 9:
            rle += str(count) + text[i]
            count = 0
    else:
        rle += str(count) + text[i]
        count = 1
rle += str(count) + text[i]

print(rle)

with open('04-zip.txt', 'w') as zip_file:
    zip_file.write(rle)

# Расшифровка zip файла
with open('04-zip.txt', 'r') as new_file:
    interpretation = str()
    rle_item = new_file.readline()
    for i in range(0, len(rle_item) - 1, 2):
        interpretation += (str(rle_item[i + 1]) * int(rle_item[i]))
print(interpretation)
