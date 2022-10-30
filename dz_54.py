# Реализуйте RLE алгоритм: реализуйте модуль сжатия и
#  восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
 
module = input('Enter the data: ')
res = str( )
i = 0

while i < len(module):
    count = 1
    while i + 1 < len(module) and module[i] == module[i + 1]:
        count = count + 1
        i += 1
    res += str(count) + module[i]
    i += 1

with open('text_word.txt', 'w', encoding='UTF-8')as input:
    print(f'input data: {module}', file=input)

with open('text_outword.txt', 'w') as output:
    print(f'output data: {res}', file=output)

