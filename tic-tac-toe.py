#This is my tic-tac-toe game refresher

#Positions of the grid of the game 
p1 = 1
p2 = 2
p3 = 3
p4 = 4
p5 = 5
p6 = 6
p7 = 7
p8 = 8
p9 = 9

#Players representation (X and O)
player_1 = 'x'
player_2 = 'o'


def main():
    #Defining the function to display the grid
    def display_grid():

        """
        This function creates a 3x3 grid with numbers
        """
        first_row = f"{p1}|{p2}|{p3}"
        second_row = f"{p4}|{p5}|{p6}"
        third_row = f"{p7}|{p8}|{p9}"
        
        print(first_row)
        print("-+-+-")
        print(second_row)
        print("-+-+-")
        print(third_row)

    #Defining the function to determine the winner
    def check_winner():
        """
        This function returns the value of the winner
        Which can be 'X' or 'O'
        """

        if p1 == p2 == p3:
            return p1
        
        elif p4 == p5 == p6:
            return p4

        elif p7 == p8 == p9:
            return p7

        elif p1 == p5 == p9:
            return p1

        elif p3 == p5 == p7:
            return p3

        return

    #Defining the function to put the player's choice in the board
    def put_movement(player, location):

        location = player

        return location

    #Now comes the game with the players choices
    def game():

        """
        This function will take the user input of where they want to put their 'X' or 'O',
        And replace the chosen place with their related letter representation.
        """

        choice_player1 = int(input(f"{player_1}'s turn to choose a square (p1-p9): "))

        movement = put_movement(player_1, choice_player1)

        P1 = movement

        display_grid()


    grid = display_grid()

    print(grid)


if __name__ == "__main__":
    main()