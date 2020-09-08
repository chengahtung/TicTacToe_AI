import random

class Player:
    def __init__(self):
        pass

    ## winning conditions for player
    def isWinner(self,board, player_num):
        win_state = [
                [board[0], board[1], board[2], board[3]],
                [board[4], board[5], board[6], board[7]],
                [board[8], board[9], board[10], board[11]],
                [board[12], board[13], board[14], board[15]],
                [board[0], board[4], board[8], board[12]],
                [board[1], board[5], board[9], board[13]],
                [board[2], board[6], board[10], board[14]],
                [board[3], board[7], board[11], board[15]],
                [board[0], board[5], board[10], board[15]],
                [board[3], board[6], board[9], board[12]],
        ]
        if [player_num,player_num,player_num,player_num] in win_state:
            return True
        else:
            return False

    # aims to maximize grid occupied in row/column
    def hasScore(self,board, possibleMoves,n):
    # first row
            return ( ( (board[0] == n and board[1] == n and (board[2] == n or board[3] == n) ))
                or ( (board[3] == n and board[2] == n and (board[1] == n or board[0] == n) ) )
                #second row
                or ( (board[4] == n and board[5] == n and (board[6] == n or board[7] == n) ) )
                or ( (board[7] == n and board[6] == n and (board[5] == n or board[4] == n) ) )
                #third row
                or ( (board[8] == n and board[9] == n and (board[10] == n or board[11] == n) ) )
                or ( (board[11] == n and board[10] == n and (board[9] == n or board[8] == n) ) )
                #fourth row
                or ( (board[12] == n and board[13] == n and (board[14] == n or board[15] == n) ) )
                or ( (board[15] == n and board[14] == n and (board[13] == n or board[12] == n) ) )
                #first column
                or ( (board[0] == n and board[4] == n and (board[8] == n or board[12] == n) ) )
                or ( (board[12] == n and board[8] == n and (board[4] == n or board[0] == n) ) )
                #second column
                or ( (board[1] == n and board[5] == n and (board[9] == n or board[13] == n) ) )
                or ( (board[13] == n and board[9] == n and (board[5] == n or board[1] == n) ) )
                #third column
                or ( (board[2] == n and board[6] == n and (board[10] == n or board[14] == n) ) )
                or ( (board[14] == n and board[10] == n and (board[6] == n or board[2] == n) ) )
                #fourth column
                or ( (board[3] == n and board[7] == n and (board[11] == n or board[15] == n) ) )
                or ( (board[15] == n and board[11] == n and (board[7] == n or board[3] == n) ) )
                #diagonal to down right
                or ( (board[0] == n and board[5] == n and (board[10] == n or board[15] == n) ) )
                or ( (board[15] == n and board[10] == n and (board[5] == n or board[0] == n) ) )
                #diagonal to down left
                or ( (board[3] == n and board[6] == n and (board[9] == n or board[12] == n) ) )
                or ( (board[12] == n and board[9] == n and (board[6] == n or board[3] == n) ) )	)

    # to priotise diagonals
    def getDiagonaldownright(self,board, i):
        # if position is diagonal and it is empty, return true
        return ((( i == 0 or i == 5 or i == 10 or i == 15 ) and board[i] == -1))


    # to priotise diagonals
    def getDiagonaldownleft(self,board, i):
        # if position is diagonal and it is empty, return true
        return ((( i == 3 or i == 6 or i == 9 or i == 12 ) and board[i] == -1))
    
    
    ## check any empty grids
    def empty_grid(self,board):
        grid =[]
        possibleMoves = [x for x, letter in enumerate(board) if letter == -1]
        for i in possibleMoves:
            grid.append(i)
        return grid

    def play(self, game_board_state, player_n):

        if (player_n == 1):
            opponent = 0
        if (player_n == 0):
            opponent = 1

        ##show the depth, based on number of available grids that ai still can occupy on
        depth = len(self.empty_grid(game_board_state))

        ## scores are calculated to pick the best move
        def automove(board):

            moves = []
            scoreList= []

            for let in [player_n, opponent]:
                for i in self.empty_grid(board):
                    ##create copy of game board
                    boardCopy = board[:]
                    boardCopy[i] = let

                    score = 0

                    # given the highest priority, occupies grid that provides AI winning state
                    if (self.isWinner(boardCopy,let) and let == player_n):
                        score += 15
                        scoreList.append(score)
                        moves.append(i)

                    # given 2nd highest priority, occupies grid that blocks opponent winning state
                    elif (self.isWinner(boardCopy,let) and let == opponent):
                        ##print(self.isWinner(boardCopy,let))
                        score += 10
                        scoreList.append(score)
                        moves.append(i)

                    # grids at side were given less priority
                    elif  (i == 1 or i==2 or i==4 or i==8 or i==7 or i==11 or i==13 or i==14):
                        score = 0
                        scoreList.append(score)
                        moves.append(i)

                    # given 3rd highest priority, occupies the most grids in a line
                    elif (self.hasScore(boardCopy,i,player_n) and let == player_n) :
                        score +=1
                        scoreList.append(score)
                        moves.append(i)

                    elif (i == 0 or i==5 or i==10 or i==15 or i==3 or i==6 or i==9 or i==12):
                        if self.getDiagonaldownright(board, i):
                            score =5
                            scoreList.append(score)
                            moves.append(i)

                        #check for diagonal empty spaces in current board
                        if self.getDiagonaldownleft(board, i):
                            score =5
                            scoreList.append(score)
                            moves.append(i)


            #for i in [0, 5, 10, 15, 3, 6, 9, 12]:
                #check for diagonal empty spaces in current board

            print(scoreList)
            print(moves)

            move = 0
            if scoreList and moves:
                    bestScore = 0
                    bestMove = 0
                    for i in range(0,len(moves)):
                            ##print("range",i)

                            if scoreList[i] > bestScore:
                                bestScore = scoreList[i]
                                bestMove = i

                            ##print("best score",bestScore)

                    move = moves[bestMove]
                    ##print("move: ",bestMove)

            return move

        ##always begin at corner for max advantage
        ##if ai moves first, it will be on depth 16 while if ai moves second after player it's depth 15.
        if depth == 16 and player_n == 0 or depth==15 and player_n == 1:
            ##randomly choose one of the four corners, ignore corners if occupied
            starting_point =[]
            for element in self.empty_grid(game_board_state):
                if element == 0 or element == 3 or element == 12 or element == 15:
                    starting_point.append(element)

            return random.choice(starting_point)
        else:
            ##print(automove(game_board_state))
            return automove(game_board_state)
