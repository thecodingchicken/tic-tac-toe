import time
class AI(object):
    def __init__(self,player='Y',empty=' '):
        self.player=player
        self.marker=player#marker = player
        self.default=[[1,1],[0,0],[0,2],
                      [2,0],[2,2],[0,1],
                      [1,0],[1,2],[2,0]]
        self.__xpos__=[1,0,0,2,2,0,1,1,2]
        self.__ypos__=[1,0,2,0,2,1,0,2,1]
        self.__test__=[[1,5,2],[6,0,7],[3,8,4]]
        self.empty = empty
    def fancy_welcome(self):
        print("Ladies and Gentlemen... ",end='')
        time.sleep(1);
        print("welcome the powerful AI into the scene!")
        time.sleep(1);
        print("I will beat most of you.",end='')
        for i in range(5):print(".",end='');time.sleep(0.25)
    def fancy_print(self,text,end=1,delay=0):
        print("%s"%text,end='')
        time.sleep(delay)
        if end==1:print()
    def call(board):
        """A function to determine where to play."""
        foo = self.__check_self_win__(board)
        if foo[0]==1:
##            self.change_board(
            pass
    def __pick_spot_2__(self,board):
        for i in range(9):
            if board[self.__xpos__[i]][self.__ypos__[i]]==self.empty:
                     board[self.__xpos__[i]][self.__ypos__[i]]=self.player
                     break
        print(3)#Testing
        return board
    def __check_hor_win__(self,board,marker):
        moved=0
        for i in range(3):
            b=board[i][:]
            if b[0]==marker and b[1]==marker and b[2]==self.empty:
                moved=1
                print(
                if marker==self.marker:
                    board[i][2]=self.marker
                else:
                    board[i][2]=self.marker
            elif b[1]==marker and b[2]==marker and b[0]==self.empty:
                moved=1
                if marker==self.marker:
                    board[i][0]=self.marker
                else:
                    board[i][0]=self.marker
            elif b[0]==marker and b[2]==marker and b[1]==self.empty:
                moved=1
                if marker==self.marker:
                    board[i][1]=self.marker
                else:
                    board[i][1]=self.marker
        return board,moved
    def __check_2_3__(self,s1,s2,s3,marker):
        if s1==marker and s2==marker and s3==self.empty:return True
        if s2==marker and s3==marker and s1==self.empty:return True
        if s1==marker and s3==marker and s2==self.empty:return True
        return False
    def __find_clear__(self,s1,s2,s3,ret=1):
        b=None
        if s1==self.empty:b= 0
        if s2==self.empty:b= 1
        if s3==self.empty:b= 2
        return b
    def __check_win_self__(self,board):
        print(1)#Testing
        board,moved = self.__check_ver_win__(board,self.marker)
        if moved==1:
            print("I won!");return board;
        board,moved = self.__check_hor_win__(board,self.marker)
        if moved==1:
            print("I won!");return board;
        board,moved = self.__check_dia_win__(board,self.marker)
        if moved==1:
            print("I won!");return board;
        return board,moved
    def __check_win_other__(self,board,other='X'):
        print(2)#Testing
        board,moved=self.__check_ver_win__(board,other)
        if moved==1:
            print("HAHA!!!  Took your spot!");return board;
        board,moved=self.__check_hor_win__(board,other)
        if moved==1:
            print("HAHA!!!  Took your spot!");return board;
        board,moved = self.__check_dia_win__(board,self.marker)
        if moved==1:
            print("HAHA!!!  Took your spot!");return board;
        return board,moved
    def __check_ver_win__(self,board,marker):
        moved=0
        for i in range(3):
            if self.__check_2_3__(board[0][i],board[1][i],board[2][i],marker)==True:
                open_space = self.__find_clear__(board[0][i],
                                                 board[1][i],
                                                 board[2][i])
##                print(open_space,i,self.marker)##Testing
                board[open_space][i]=self.marker;
##                print("Done on round %d\nOpen space %d"%(i,open_space))
                #Previous line for testing
                break
        return board,moved
            
        for i in range(3):
            b=[board[0][i],board[1][i],board[2][i]]
            print(b)
            if b[0]==marker and b[1]==marker and b[2]==self.empty:
                pass
            elif b[1]==marker and b[2]==marker and b[0]==self.empty:pass
            elif b[0]==marker and b[2]==marker and b[1]==self.empty:pass
    def __check_dia_win__(self,board,marker):
        moved=0
        if self.__check_2_3__(board[0][0],board[1][1],
                              board[2][2],marker) == True:
            open_space = self.__find_clear__(board[0][0],
                                                 board[1][1],
                                                 board[2][2],1)
            moved=1
            board[open_space][open_space]=marker
        elif self.__check_2_3__(board[0][2],board[1][1],
                              board[2][0],marker) == True:
            open_space = self.__find_clear__(board[0][2],
                                                 board[1][1],
                                                 board[2][0],2)
            moved=1
            if open_space==0:
                board[0][2]=marker
            elif open_space==1:
                board[1][1]=marker
            elif open_space==2:
                board[2][0]=marker
        return board ,moved           
##    def check_win(self, board):
##        _board=self.__check_win_self__(board[:])
##        __board=self.__check_win_other__(board[:])
##        if board!=_board or board!= __board:
##            if board != _board:print(1);return _board
##            else:print(2);return _board
##        else:
##            board=self.__pick_spot_2__(board)
##            print(3)
##            return board
    def check_win2(self,board):
        board1, moved1 = self.__check_win_self__(board[:])
        board2, moved2 = self.__check_win_other__(board[:])
        print ("%s %s %d %d"%(board1==board,board2==board,moved1,moved2))
        if ((board1 != board) and (moved1==1)):#and (board2==board):
            print(4)#Testing
            return board1
        elif (board2 != board) and (board1==board) and m:
            print(5)#Testing
            return board2
        elif ( board1 == board) and (board2 == board ):
            print(6)#Testing
            return self.__pick_spot_2__(board)
    def say_turn(self):
        print("*****AI's TURN******\n")
        print("Be prepared...")
    def turn(self,board):
        self.say_turn()
        board=self.check_win2(board)
        return board
    def ai_won(self):
        print("HAHA!!!!")
        print("I always knew I could beat you!")
        self.fancy_print("Why try to beat me?",0,3)
        self.fancy_print("I will survive.")
        print("Score:\n\tComputer\t 1\n\tPerson\t\t 0")
    def ai_lost(self):
        self.fancy_print("What???",delay=3)
        self.fancy_print('How dare you!!!',1,2)
        
__all__=[AI]
