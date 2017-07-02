#/bin/bash python3
"""tic_tac_toe.py
A python version of tic-tac-toe.
It will have options:
    1. Player 1 vs. Player 2
    2. Player vs AI"""
import time
import os
import sys
import AI
##import boardManip
from getPos import __get_row__,__get_col__
class ListNot2D(Exception):pass
class NeededAList(Exception):pass
class WonError(Exception):pass
def print_board(board):
    amt_p=13
    if(type(board))!=list:
        raise NeededAList()
    else:
        if type(board[0])!=list:
            raise ListNot2D()
    for i in range(3):
        for j in range(3):
            board[i][j]=board[i][j].upper()
##    print("    1   2   3   \n  ",end='')
    print("    1   2   3   \n ","-"*amt_p)
    for i in range(3):
        print("%s | %s | %s | %s |"%(i+1,board[i][0],board[i][1],board[i][2]))
        print(' ',"-"*amt_p)

def get_move(board,player):
    if(type(board))!=list:
        raise NeededAList()
    else:
        if type(board[0])!=list:
            raise ListNot2D()
    while True:
        row=__get_row__(player)
        col=__get_col__(player)
        if board[row][col]==' ':
            board[row][col]=player.upper()
            return board
        elif board[row][col]== player.upper():
            print("You have chosen this spot already.")
        else:print("The other player has chosen this spot.")
##    return board
def __check_row__(s1,s2,s3,player):
    if s1!=player:return False
    if s2!=player:return False
    if s3!=player:return False
    return True
def check_win(board,player,verbal=1):
    if(type(board))!=list:
        raise NeededAList()
    else:
        if type(board[0])!=list:
            raise ListNot2D()
    if __check_row__(board[0][0],board[0][1],board[0][2],player):
        if verbal:print("!!!!!WIN!!!!!")
        return True;
    elif __check_row__(board[1][0],board[1][1],board[1][2],player):
        if verbal:print("!!!!!WIN!!!!!")
        return True;
    elif __check_row__(board[2][0],board[2][1],board[2][2],player):
        if verbal:print("!!!!!WIN!!!!!")
        return True;
    elif __check_row__(board[0][0],board[1][0],board[2][0],player):
        if verbal:print("!!!!!WIN!!!!!")
        return True;
    elif __check_row__(board[0][1],board[1][1],board[2][1],player):
        if verbal:print("!!!!!WIN!!!!!")
        return True;
    elif __check_row__(board[0][2],board[1][2],board[2][2],player):
        if verbal:print("!!!!!WIN!!!!!")
        return True;
    elif __check_row__(board[0][0],board[1][1],board[2][2],player):
        if verbal:print("!!!!!WIN!!!!!")
        return True;
    elif __check_row__(board[0][2],board[1][1],board[2][2],player):
        if verbal:print("!!!!!WIN!!!!!")
        return True;
def spots_left(board):
    cnt=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':cnt+=1
    return cnt
def cats_game(board):
    left=spots_left(board)##See how many spots are free
    if left == 0:
        b = check_win(board,'X',0) or check_win(board,'Y',0)
        if not b:
            print_board(board);
            print("\n\n\nBummer.")
            time.sleep(2)
            for i in range(3):print(".",end='');time.sleep(0.5);
            print("\nCat's game...")
            print(board)
            sys.exit()
def gameboard(rows,cols,filler=None):
    l=[]
    for i in range(rows):
        l.append([])
        for j in range(cols):
            l[i].append(filler)
    return l
def game():
    won=False
    board=gameboard(3,3,' ')
    player='X'
    while not won:
        print("*****PLAYER X's turn*****\n")
        player='X'
        print_board(board);print();
        get_move(board,'X')
        cats_game(board)
        won=check_win(board,'X')
        if won:who='X';break
        print("*****PLAYER Y's turn*****\n")
        player='Y'
        print_board(board);print();
        get_move(board,'Y')
        cats_game(board)
        won=check_win(board,'Y')
        if won:b='Y';break;
    print("\n\nPlayer %s won!!!\nGood for you."%player);time.sleep(5);
    print("Now for the other one of you",end='')
    for i in range(3):print('.',end='');time.sleep(1);
    print("\nTry harder!")
    print(board)
def gameAI():
    board=gameboard(3,3,' ')
    print("Welcome to tic-tac-toe")
    print("You will play against a computer!!!")
    ai=AI.AI('Y')
    ai.fancy_welcome()
##    ai.fancy_print("I guess you will want to go first?")
##    ai.fancy_print("Well, ...\n",1,3)
##    ai.fancy_print("you can't!  Haha! ",1,3)
##    print("BOSS: They can go first...\nLet the pitiful human try and die.".upper())
##    ai.fancy_print("Ok...",delay=0.5)
    game_in_play = True
    while game_in_play:
        print("\n*****PLAYER X's turn*****\n")
        player='X'
        print_board(board);print();
        get_move(board,'X')
        cats_game(board)
        won=check_win(board,'X')
        if won:who='X';break
        board = ai.turn(board[:])
##        try:board = ai.turn(board[:])
##        except ValueError as e:print("%s\n\n%s"%(board,e));sys.exit()
        cats_game(board)
        won=check_win(board,'Y')
        if won:who='Y';break
    print_board(board)
    if who =='X':
        print("Congrats!");
        print("Now a message from your enemy:")
        ai.ai_lost()
    elif who=='Y':
        print(":-((")
        ai.ai_won()
##game()
b=AI.AI('Y')
board=gameboard(3,3,' ')
####gameAI()
##board=[['X', ' ', ' '], [' ', 'Y', ' '], ['Y', 'Y', ' ']]
####b.__check_ver_win__(board,'Y')
####print_board(board)
######print(b.__check_hor_win__(board,'X'))
####board=gameboard(3,3,' ');print("Reset board.")
##board=[['X', 'X', 'X'], [' ', 'Y', ' '], ['Y', 'Y', ' ']]
##board=[['Y', ' ', 'X'], [' ', 'Y', ' '], [' ', 'Y', ' ']]
##b.check_win(board)
##print_board(board)
##b=check_win(board,'Y');
##if b:print("Y won");
##c=check_win(board,'X');
##if c:print("X won");
gameAI()
