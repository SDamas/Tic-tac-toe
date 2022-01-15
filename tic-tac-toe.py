#This program runs a tic-tac-toe game

#Defining the game board
board = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

#Creating the players' mark
player_1 = "x"
player_2 = "o"
draw = "Draw!"

#Setting the players turn.
#None selected because it'll be according to the user's choice.
turn = None

#Main function to run the game
def main():

    global turn

    #Variable that checks for winner or tie
    winner = False

    print("Welcome to the tick-tac-toe game!")

    player_1 = input("Player 1 choose your mark 'x'/'o': ")
        
    if player_1.lower() == 'x':
        print("Player 2 is going with the 'o'.")
        turn = player_1
    else: 
        print("Player 2 is going with the 'x'.")
        turn = player_2

    #First display of the game board to start the game
    display_board(board)

    #Game loop while there is no winner nor it's a tie
    while not winner:
        winner = game()

        if winner == "Tie!":
            print(winner)
            print("Good game. Thanks for playing!")

#Function to run the game
def game():

    """
    This function runs the game.
    """

    winner = None

    #Display player turn and let him choose
    # a spot on the board
    choice = display_turn()

    #Set his mark on the board spot he chose
    set_mark(choice)

    #Display the updated board
    display_board(board)

    #Check if there is a winner already
    winner = check_winner()

    #Check if it is a tie already
    draw = check_tie()

    #If there is not a winner nor it is a tie,
    #Switch players' turn
    switch_turn()

    if winner:
        return winner
    elif draw:
        return draw

#Setting the function to display the game board
def display_board(board):

    """
    This function displays the game board
    """

    #First line of the board
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")

    #Second line of the board
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")

    #Third line of the board
    print(f"{board[6]}|{board[7]}|{board[8]}")

#Creating the function to display players' turn
def display_turn():

    """
    This function displays which player's it's the turn
    Let him choose on which spot he wants to set his mark,
    and return the choice.

    Turn = Current player

    return: player's choice of the spot to put his mark
    """

    global turn

    if turn == player_1:
        choice = int(input(f"{player_1}'s turn to choose a square (1-9): "))

    
    elif turn == player_2:
        choice = int(input(f"{player_2}'s turn to choose a square (1-9): "))


    return choice

#Creating the function that will update the game board
#with the players' location choice
def set_mark(choice):

    """
    This function set the mark of the player
    in the location he chose on the game board

    Return: Nothing. This function's function is to update the
    game board with the player's choice.
    """
    
    global turn
    global board

    #Check each spot on the board, if the spot equals the player choice,
    #update with his mark
    for i in board:
        if i == choice and turn == player_1:   
            board[i-1] = turn

        elif i == choice and turn == player_2:   
            board[i-1] = turn

#Creating the function to switch turns between players
def switch_turn():

    """
    This function switches the turn
    between players

    return which player it will be the turn
    """

    global turn

    #Takes the turn variable and replaces it with the next player
    if turn == player_1:
        turn = player_2

    elif turn == player_2:
        turn = player_1

    return turn

#Creating a function to check the winner
def check_winner():
    
    """
    This function checks for the winner

    Return true if there is a winner
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

#Creating a function to check if it is tie
def check_tie():

    """
    This function checks if it is a tie

    return: "Tie!"
    """

    global board

    empty_spaces = 0
    tie = "Tie!"

    #Check if there is still numbers in the board, which means it is an empty space. 
    for i in board:
        if i in range(1, len(board)):
            empty_spaces += 1
    
    if empty_spaces == 0:
        return tie


if __name__ == "__main__":
    main()


