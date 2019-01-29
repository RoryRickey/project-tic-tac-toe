import random

def draw_board(board):
    # This function prints out the board that it was passed and should not return anything
    #HINT: pass a list to this function that holds the position of 'X's and 'O's
    print(board[6] + "  | " + board[7] + " | " + board[8])
    print("___|___|___")
    print(board[3] + "  | " + board[4] + " | " + board[5])
    print("___|___|___")
    print(board[0] + "  | " + board[1] + " | " + board[2])
    print("   |   |   ")
    return

def input_player_letter():
  print ("Please Select X or O")
  player_letter = input()
  player_letter = player_letter.upper()
  while (player_letter!= ('X') and  player_letter!= ('O')):
    print ("Please Select X or O")
    player_letter = input()
    player_letter = player_letter.upper()
    #Ask the player if they want to be 'X' or 'O'
    #Return the chosen letter
    #Hint: Use a loop to keep prompting the player for a letter if the input is not valid
  return player_letter

def who_goes_first():
    #Randomly choose who goes first
    #Return the string 'computer' or 'player'
    #HINT: look up the documentation for the 'random' library

    return

def main():

    print ('Welcome to Tic Tac Toe')
    starter = who_goes_first()

    player_letter = input_player_letter()
    #Here assign computer_letter to be 'O' if player_letter is 'X' or vice versa



    #initialize your board list here to pass to draw the board
    board = [' ']*9
    draw_board(board)

main()