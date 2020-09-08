import random
class Player:
  def __init__(self):
    pass

  def play(self, game_board_state, player_n):
      
      if (player_n == 1):
          opponent = 0
      if (player_n == 0):
          opponent = 1
          
      def isWinner(board, let):
          #priority PLAYER win 
          if (player_n == let):
              return ((board[0] == let and board[1] == let and board[2] == let and board[3] == let) or (board[4] == let and board[5] == let and board[6] == let and board[7] == let) or (board[8] == let and board[9] == let and board[10] == let and board[11] == let) or (board[12] == let and board[13] == let and board[14] == let and board[15] == let) or (board[0] == let and board[4] == let and board[8] == let and board[12] == let) or (board[1] == let and board[5] == let and board[9] == let and board[13] == let) or (board[2] == let and board[6] == let and board[10] == let and board[14] == let) or (board[3] == let and board[7] == let and board[11] == let and board[15] == let) or (board[0] == let and board[5] == let and board[10] == let and board[15] == let) or (board[3] == let and board[6] == let and board[9] == let and board[12] == let))     
          if (opponent == let):
              return ((board[0] == let and board[1] == let and board[2] == let and board[3] == let) or (board[4] == let and board[5] == let and board[6] == let and board[7] == let) or (board[8] == let and board[9] == let and board[10] == let and board[11] == let) or (board[12] == let and board[13] == let and board[14] == let and board[15] == let) or (board[0] == let and board[4] == let and board[8] == let and board[12] == let) or (board[1] == let and board[5] == let and board[9] == let and board[13] == let) or (board[2] == let and board[6] == let and board[10] == let and board[14] == let) or (board[3] == let and board[7] == let and board[11] == let and board[15] == let) or (board[0] == let and board[5] == let and board[10] == let and board[15] == let) or (board[3] == let and board[6] == let and board[9] == let and board[12] == let))
     
      def hasScore(board, possibleMoves):
          n = player_n
                  #first row
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

      
      def getDiagonaldownright(board, i):
          # if position is diagonal and it is empty, return true
          return ((( i == 0 or i == 5 or i == 10 or i == 15 ) and board[i] == -1))        

      def getDiagonaldownleft(board, i):
          # if position is diagonal and it is empty, return true          
          return ((( i == 3 or i == 6 or i == 9 or i == 12 ) and board[i] == -1))        
   
      def automove():
          move = random.choice([i for i in range(len(game_board_state)) if game_board_state[i] < 0])
          #insert available moves into a array from game_board_state
          possibleMoves = [x for x, letter in enumerate(game_board_state) if letter == -1]

          for let in [player_n, opponent]:
              for i in possibleMoves:
                  #make virtual copy of the board
                  boardCopy = game_board_state[:]
                  #insert player_n into the  virtual board
                  boardCopy[i] = let
                  
                  #check is there any winner using the inserted virtual board
                  if isWinner(boardCopy, let):
                      move = i
                      return move
                  
                   #diagonal positions (priority)
          for i in [0, 5, 10, 15, 3, 6, 9, 12]:
              #make virtual copy of the board
              boardCopy2 = game_board_state[:]
              #insert player_n into the  virtual board
              boardCopy2[i] = let

              #check for diagonal empty spaces in current board
              if getDiagonaldownright(game_board_state, i):
                 move = i 
                 break
              #check for diagonal empty spaces in current board
              if getDiagonaldownleft(game_board_state, i):
                 move = i
                 break
            
              for o in possibleMoves:
                  #using the virtual board with the moves inserted, check to see if hasScore
                  if hasScore(boardCopy, o):
                      move = o
                      break
                                    
                 
          return move         
#          return random.choice([i for i in range(len(game_board_state)) if game_board_state[i] < 0])
#          return game_board_state.index(-1)
      return automove()
      

   
    

  