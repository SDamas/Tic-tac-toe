#This program runs a tic-tac-toe game

#Defining the game board
board = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

#Creating the players' mark
player_1 = "x"
player_2 = "o"
draw = "Draw!"

#Setting the default first player turn.
#None selected because it'll be according to the user's choice.
turn = None

#Main function to run the game
def main():

    global turn
    
    game_run = True

    winner = False

    draw = False

    print("Welcome to the tick-tac-toe game!")

    player_1 = input("Player 1 choose your mark 'x'/'o': ")
        
    if player_1.lower() == 'x':
        print("Player 2 is going with the 'o'.")
        turn = player_1
    else: 
        print("Player 2 is going with the 'x'.")
        turn = player_2

    display_board(board)

    while not winner:
        winner = game()

        if winner.lower() == "draw!":
            print("Good game. Thanks for playing!")


#Function to run the game
def game():

    """
    This function runs the game.
    """

    winner = None

    choice = display_turn()
    set_mark(choice)
    display_board(board)
    winner = check_winner()
    draw = check_draw()
    switch_turn()

    if winner:
        return winner
    else:
        return draw

#Setting the function to display the game board
def display_board(board):

    """
    This function displays the game board
    """

    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")


#Creating the function to display players' turn
def display_turn():

    """
    This function displays which player's it's the turn
    Let him choose on which spot he wants to set his mark,
    and return the choice.

    Turn = Current player
    """

    global turn

    if turn == player_1:
        choice = int(input(f"{player_1}'s turn to choose a square (1-9): "))

    
    elif turn == player_2:
        choice = int(input(f"{player_2}'s turn to choose a square (1-9): "))


    return choice


#Creating the function that will update the game board
#with the players location choice
def set_mark(choice):

    """
    This function set the mark of the player
    in the location he chose on the game board
    """
    
    global turn
    global board

    for i in board:
        if i == choice and turn == player_1:   
            board[i-1] = turn
            
            playing = True

        elif i == choice and turn == player_2:   
            board[i-1] = turn


#Creating the function to switch turns between players
def switch_turn():

    """
    This function switches the turn
    between players
    """

    global turn

    if turn == player_1:
        turn = player_2

    elif turn == player_2:
        turn = player_1

    return turn


#Creating a function to check the winner
def check_winner():
    
    """
    This function checks for the winner
    """

    global board
    
    #Check if the columns match.
    if board[0] == board[1] == board[2]:
        print("Good game. Thanks for playing!")
        return True
    elif board[3] == board[4] == board[5]:
        print("Good game. Thanks for playing!")
        return True
    elif board[6] == board[7] == board[8]:
        print("Good game. Thanks for playing!")
        return True

    #Check if the rows match.
    if board[0] == board[3] == board[6]:
        print("Good game. Thanks for playing!")
        return True
    elif board[1] == board[4] == board[7]:
        print("Good game. Thanks for playing!")
        return True
    elif board[2] == board[5] == board[8]:
        print("Good game. Thanks for playing!")
        return True

    #Check if diagonal match:
    if board[0] == board[4] == board[8]:
        print("Good game. Thanks for playing!")
        return True
    elif board[2] == board[4] == board[6]:
        print("Good game. Thanks for playing!")
        return True

#Creating a function to check if it is a draw
def check_draw():

    """
    This function checks if the game is draw
    """

    for i in board:
        if i != range(1, 9):
            draw 
            return "Draw!"

if __name__ == "__main__":
    main()


