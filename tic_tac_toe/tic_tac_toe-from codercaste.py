import random
import re
## Game state current
gsp = []
## Game state previous
gsc = []
## Last move made
losing_move = 'hi'
def win_conditions():
    ## These conditions will be unique to whatever game the AI
    ## is adapted for.  Since win conditions are of a small
    ## enough number for tic-tac-toe, I can simply enumerate
    ## them all.
    global gsc
    global xoro
    if (gsc[0] == xoro) & (gsc[1] == xoro) & (gsc[2] == xoro):
        return 1
    elif (gsc[3] == xoro) & (gsc[4] == xoro) & (gsc[5] == xoro):
        return 1
    elif (gsc[6] == xoro) & (gsc[7] == xoro) & (gsc[8] == xoro):
        return 1
    elif (gsc[0] == xoro) & (gsc[3] == xoro) & (gsc[6] == xoro):
        return 1
    elif (gsc[1] == xoro) & (gsc[4] == xoro) & (gsc[7] == xoro):
        return 1
    elif (gsc[2] == xoro) & (gsc[5] == xoro) & (gsc[8] == xoro):
        return 1
    elif (gsc[0] == xoro) & (gsc[4] == xoro) & (gsc[8] == xoro):
        return 1
    elif (gsc[2] == xoro) & (gsc[4] == xoro) & (gsc[6] == xoro):
        return 1
    else:
        return 0

## Output.  The display isn't much, but this isn't about
## graphics.
def print_board():
    global gsc
    print (gsc[0]+' '+gsc[1]+' '+gsc[2])
    print (gsc[3]+' '+gsc[4]+' '+gsc[5])
    print (gsc[6]+' '+gsc[7]+' '+gsc[8])

## Turns the game state into a string to be checked against the
## strings stored in the text file used as the AI's memory.
def makereadable(gsc,move):
    readable = ''
    for i in gsc:
        readable += i
    readable += str(move)
    return readable

def ai_turn():
    global gsp
    global gsc
    global losing_move
    global gameon
    global textbook

    ## Position is a value representing a move.
    ## For tic-tac-toe, it is an integer 0-8,
    ## with each number representing a box on the
    ## board.
    position = 0
    ## First try to make one of the nine valid
    ## moves in tic-tac-toe.
    while position < 9:
        ai_move = position
        ## Checksthis move against the record of bad moves
        if makereadable(gsc,ai_move) not in textbook:
            ## If the space is still open
            ## This condition will be unique for whatever
            ## game the AI is playing
            if gsc[ai_move] == '-':
                ## Set the game state previous as
                ## the game state current...
                gsp = []
                for i in gsc:
                    gsp.append(i)
                ## ...then modify the game state to
                ## reflect the move
                gsc[ai_move] = 'x'
                gsp[ai_move] = '-'
                ## Record the move
                losing_move = ai_move
                break
            ## If the move is not a valid move at the time...
            else:
                position += 1
        ## If the move has previously resulted in a loss...
        else:
            position += 1
    ## If there are no valid moves left, call the game off
    if position == 9:
        gameon = 0

## The artificially stupid computer,
## here to make quick moves against
## the AI so that the AI can learn
## quickly.
def as_turn():
    global gsc
    if '-' not in gsc:
        hold = 0
    else:
        hold = 1
    while hold == 1:
        as_move = random.randrange(0,9)
        if gsc[as_move] == '-':
            hold = 0
            gsc[as_move] = 'o'

## Opens or creates the file in which to store
## bad moves.
f = open('C:\\Users\\Joshua Bowe\\Python\\files\\tic_tac_toe\\bad_moves\\b.txt','a+')
f.seek(0)
textbook = f.read()

coursecredits = 0

while coursecredits < 100000:

    ## Sets the initial conditions of the game
    gsc = ['-','-','-','-','-','-','-','-','-']

    ## Sets it as x's turn
    xoro = 'x'
    gameon = 1
    
    ## Runs for one full game
    while gameon == 1:
        ## If it is x's turn
        if xoro == 'x':
            ai_turn()
            if gameon == 0:
                break
            ## If the game didn't end, check to see
            ## if this most recent move made
            ## x win
            elif win_conditions() == 1:
                gameon = 0
            ## If the game didn't end one way or
            ## another, give the turn over to o
            else:
                xoro = 'o'
        ## If it is o's turn
        else:
            as_turn()
            ## If o won - that is, if x, the AI,
            ## lost, write to the file the game state
            ## before x made its last move, and
            ## what that last move was
            if win_conditions() == 1:
                gameon = 0
                f.write(makereadable(gsp,losing_move))
                f.write('\n')
            else:
                xoro = 'x'

    coursecredits += 1
    if coursecredits % 5000 == 0:
        print ('HAL has earned',coursecredits,'credit hours towards his degree.')

f.close()
def human_turn():
    global gsc
    hold = 1
    while hold == 1:
        minihold = 1
        while minihold == 1:
            human_move = input('Your turn: ')
            try:
                human_move = int(human_move)
                minihold = 0
            except ValueError:
                print ('Invalid input.  Must be an integer from 0 to 8.')
        if (human_move != 0) & (human_move != 1) & (human_move != 2) & (human_move != 3) & (human_move != 4) & (human_move != 5) & (human_move != 6) & (human_move != 7) & (human_move != 8):
            print ('Invalid input.  Must be an integer from 0 to 8.')
        else:
            if gsc[human_move] != '-':
                print('Invalid choice.  That position has already been played.')
            else:
                gsc[human_move] = 'o'
                hold = 0
