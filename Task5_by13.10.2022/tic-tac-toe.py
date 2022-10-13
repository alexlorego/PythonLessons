# Создайте программу для игры в "Крестики-нолики"

import random

def print_board():
    print(board[0],'|', board[1],'|', board[2])
    print('-'*9)
    print(board[3],'|', board[4],'|', board[5])
    print('-'*9)
    print(board[6],'|', board[7],'|', board[8])
    
def who_win(first, second):
    winner = ""
    for i in v:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            winner = f"{first}"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            winner = f"{second}"
    return winner

def make_move(put, ch):
    i = board.index(put)
    board[i] = ch

v = [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8],
     [0, 3, 6],
     [1, 4, 7],
     [2, 5, 8],
     [0, 4, 8],
     [2, 4, 6]]

board = list(range(1, 10))

print('\n======== крестики-нолики ===========')
player_1 = input('Введите имя первого игрока: ')
player_2 = input('Введите имя второго игрока: ')

lots = random.randint(1, 2)
if lots == 1:
    first = player_1
    second = player_2
else:
    first = player_2
    second = player_1
print(f'\nПервым ходит {first}, он играет крестиками')
move = first
turn = 1
winner = ''

while winner == '' and turn <= 9:
    print_board()
    if move == first:
        ch = 'X'
        put = int(input(f"{first}, твой ход! Куда поставим {ch}? => "))
        while put not in board:
            put = int(input(f"Не туда нажал? Попробуй еще раз: ")) 
        move = second
    else:
        ch = 'O'
        put = int(input(f"{second}, твой ход! Куда поставим {ch}? => "))
        while put not in board:
            put = int(input(f"Не туда нажал? Попробуй еще раз: ")) 
        move = first

    make_move(put, ch)
    winner = who_win(first, second)
    turn += 1
    
print_board()
if winner == '': print('Кажется у нас НИЧЬЯ!')
else: print(f"Победил {winner}! Поздавляем!")
