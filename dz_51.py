# Напишите программу, удаляющую из текста все слова, 
# содержащие ""абв"".

text = 'Enter the text Яабв люабвблю'.split()
smb = 'абв'
print(text)
print(' '.join(list(filter(lambda word: 'абв' not in word, text))))
