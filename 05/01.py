# Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы "абв".

text = "Автобус ехал по маршруту и случайно обВалился на обочину! крокодил, бульвар, самолет"
text = text.split()
for word in text:
    if 'а' in word.lower() and 'б' in word.lower() and 'в' in word.lower():
        text.remove(word)
print(' '.join(text))
