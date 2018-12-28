import os
import random
import time


class game_board_n_queen():

    #Initializing the board
    def __init__(self):
        self.board = []
        self.game_over = False

    def create_board(self, size):

        #Creating board of given size
        for i in range(size):
            board_row = []
            for j in range(size):
                board_row.append(0)

            self.board.append(board_row)



    def board_display(self):

        print(" "+'_______'*(len(self.board)+1))
        print("|  ", end="")
        counter = 1
        print("    |",end="")
        for i in range(len(self.board)):
            print(str(counter).rjust(4), end=" | ")
            counter += 1
        print()
        counter = 1
        for i in range(len(self.board)):
            print("| ", end= "")
            print(str(counter).rjust(4), end=" | ")
            counter += 1
            for j in range(len(self.board)):
                if self.board[i][j] != 0:
                    print(str('Q').rjust(4), end=" | ")
                else:
                    print("    ",end=" | ")
            print()
        print("|"+'_______'*(len(self.board)+1)+"|")



    def clear_screen(self):

        #for windows prompt
        if os.name == 'nt':
            _ = os.system('cls')

        #for mac and linux prompt(here os.name is 'posix')
        else:
            _ = os.system('clear')

        #for any IDLE remove include the below commented code
        #print("\n"*100)


    def check_game_over(self):

        queen_count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 1 :

                    queen_count += 1

                    #Checking upper left diagonal
                    x_check, y_check = i - 1, j - 1
                    while x_check >= 0 and y_check >= 0:
                        if self.board[x_check][y_check] == 1 :
                            return self.game_over
                        x_check, y_check = x_check - 1, y_check - 1

                    #Checking upper right diagonal
                    x_check, y_check = i - 1, j + 1
                    while x_check >= 0 and y_check < len(self.board):
                        if self.board[x_check][y_check] == 1 :
                            return self.game_over
                        x_check, y_check = x_check - 1, y_check + 1

                    #Checking the row
                    x_check, y_check = i, j - 1
                    while y_check >= 0:
                        if self.board[x_check][y_check] == 1 :
                            return self.game_over
                        y_check = y_check - 1
                    x_check, y_check = i, j + 1
                    while y_check < len(self.board):
                        if self.board[x_check][y_check] == 1 :
                            return self.game_over
                        y_check = y_check + 1

                    #Checking the column
                    x_check, y_check = i - 1, j
                    while x_check >= 0 :
                        if self.board[x_check][y_check] == 1 :
                            return self.game_over
                        x_check = x_check - 1
                    x_check, y_check = i + 1, j
                    while x_check < len(self.board) :
                        if self.board[x_check][y_check] == 1 :
                            return self.game_over
                        x_check = x_check + 1

        if queen_count == len(self.board) :
            self.game_over = True
        return self.game_over


    def is_possible_move(self, player_choice, remove = False):
        if remove :
            player_x_choice, player_y_choice = player_choice[0] - 1, player_choice[1] - 1

            return (self.board[player_x_choice][player_y_choice] == 1)
        else:
            player_x_choice, player_y_choice = player_choice[0] - 1, player_choice[1] - 1

            return (self.board[player_x_choice][player_y_choice] == 0)


    def place_remove_queen(self, player_choice, remove = False):
        if remove :
            player_x_choice, player_y_choice = player_choice[0] - 1, player_choice[1] - 1

            self.board[player_x_choice][player_y_choice] = 0
        else :
            player_x_choice, player_y_choice = player_choice[0] - 1, player_choice[1] - 1

            self.board[player_x_choice][player_y_choice] = 1


class MyError(Exception):

    # Constructor or Initializer
    def __init__(self, value = False):
        self.value = value

    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))




game = game_board_n_queen()

while True:

    try:
        print("Choose your game level between 4-10")

        level = int(input())

        if level in [4,5,6,7,8,9,10]:
            break
        else:
            raise(MyError())
    except:
        print("Invalid Game level! Choose your game level as follows!")

game.create_board(level)

win = False

while True:

    game.board_display()

    while True:

        correct_choice = False

        try:
            print("Enter your choice as follows")
            print("0: Place a QUEEN")
            print("1: Remove a QUEEN")
            print("2: Check game for result")

            choice = int(input())

            if choice in [0,1,2]:
                correct_choice = True

            if not correct_choice:
                raise(MyError())
            else:
                break

        except:
            print("Invalid Choise! Choose correct input as follows")

    if choice == 0:

        while True:

            correct_user_choice = False

            try:
                print("Enter your x and y positions to place the queen in a single line seperated by space")

                user_choice = list(map(int,input().strip().split()))

                correct_user_choice = game.is_possible_move(user_choice)
                while not correct_choice:

                    print("Invalid Choice!")
                    print("Enter your x and y positions to place the queen in a single line seperated by space")

                    user_choice = list(map(int,input().strip().split()))

                    correct_user_choice = game.is_possible_move(user_choice)

                game.place_remove_queen(user_choice)

                break

            except:
                print("Invalid input position given! Enter your position as follows")

    elif choice == 1:
        while True:

            correct_user_choice = False

            try:
                print("Enter your x and y positions to remove the queen in a single line seperated by space")

                user_choice = list(map(int,input().strip().split()))

                correct_user_choice = game.is_possible_move(user_choice)
                while not correct_choice:

                    print("Invalid Choice!")
                    print("Enter your x and y positions to remove the queen in a single line seperated by space")

                    user_choice = list(map(int,input().strip().split()))

                    correct_user_choice = game.is_possible_move(user_choice, True)

                game.place_remove_queen(user_choice, True)

                break

            except:
                print("Invalid input position given! Enter your position as follows")


    else:

        win = game.check_game_over()
        print(win)
        break



    game.clear_screen()

    time.sleep(1)

if win:
    print("Congrats! You won the game!!!")
else:
    print("Sorry, you lost. You placed the queens incorrectly")

game.board_display()

input()
