#----------GLOBAL VARIABLES----------

def name():
  print("                          #TIC-TAC-TOE#")
board = ["_", "_", "_",
          "_", "_", "_",
          "_", "_", "_"
        ]    
    
#if game is Over
game_still_going = True

#who is the winner?
winner = None

#current player
current_player = "X"

def display_board():
  #displaying board
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])
    
#play TICTACTOE
def play_game():

  display_board()

  while game_still_going:
  # handle a single turn for an arbitriary player
    handle_turn(current_player)
  #check if gme is over someone won or tie
    check_if_game_over()
  #flipping between X and O
    flip_player()

  if winner ==  "X" or winner == "O":
    print(winner+" won.")
  elif winner == None:
    print("Tie.")  

def handle_turn(player):
  #handling turns for an arbitriary player
  print(player + "'s turn")
  
  position = input("Enter the position from 1 to 9 --> ")
  
  valid = False
  while not valid:

    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("Invalid Input. Choose a option between 1 to 9 --> ")

    position = int(position) - 1
    
    if board[position] == "_":
      valid = True
    else:
      print("You can't go there") 
  board[position] = player
  display_board()

def check_if_game_over():
  check_for_winner()
  check_if_tie()
  return

def check_for_winner():
  global winner
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  
  if column_winner:
    #there was a winner
    winner = column_winner
  elif row_winner:
    winner = row_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None    

  

  return


def  check_rows():
  global game_still_going

  row1 = board[0] == board[1] == board[2] != "_"
  row2 = board[3] == board[4] == board[5] != "_"
  row3 = board[6] == board[7] == board[8] != "_"

  if row1 or row2 or row3:
    game_still_going = False

  if row1:
    return board[0]
  if row2:
    return board[3]
  if row3:
    return board[6]      
  return


def  check_columns():
  global game_still_going
  col1 = board[0] == board[3] == board[6] != "_"
  col2 = board[1] == board[4] == board[7] != "_"
  col3 = board[2] == board[5] == board[8] != "_"

  if col1 or col2 or col3:
    game_still_going = False

  if col1:
    return board[0]
  if col2:
    return board[1]
  if col3:
    return board[2]      

  return


def  check_diagonals():
  global game_still_going
  dia1 = board[0] == board[4] == board[8] != "_"
  dia2 = board[2] == board[4] == board[6] != "_"

  if dia1 or dia2:
    game_still_going = False

  if dia1:
    return board[0]
  if dia2:
    return board[2]
  
  return



def check_if_tie():
  global game_still_going
  global winner

  if "_" not in board:
    game_still_going = False
    winner = None
  return

def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"

  elif current_player == "O" : 
    current_player = "X"
  return


play_game()  