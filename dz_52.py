# Создайте программу для игры с конфетами человек против
#  человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два 
# игрока делая ход друг после друга. Первый ход определяется
#  жеребьёвкой. За один ход можно забрать не более чем 28 
# конфет. Все конфеты оппонента достаются сделавшему последний
#  ход. Сколько конфет нужно взять первому игроку, чтобы забрать 
# все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint
# from unittest import result
draw = randint(0, 2)
if draw:
    print('First player turn')
else:
    print('Second player turn')
     
candies = 2021
first_player = int(input('Number of candies of the first player: '))
second_player = int(input('Number of candies of the second player: '))
max_candies = 28
result_first = 0
result_second = 0

while result_first <= candies and result_second <= candies:
    if first_player <= max_candies:
        result_first = first_player + result_second
    else:
        print('Взяли много конфет! ')
        first_player = int(input('Number of candies of the first player: '))    
    if result_first >= candies:
        break
    if second_player <= max_candies:
        result_second = second_player + result_first
    else:
        print('Взяли много конфет! ')
        second_player = int(input('Number of candies of the second player: '))
print(result_first)
print(result_second)

if result_first >= candies:
    print('Выиграл первый игрок! ')
else:
    print('Выиграл второй игрок! ')        
