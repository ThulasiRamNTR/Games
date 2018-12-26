import random
import os
import time


class game_board_tic_tac_toe():

    def __init__(self):
        self.board = [[0,0,0] for i in range(3)]
        self.game_over = False
        self.keypad_matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.inducerList = []

    def board_display(self):
        print(" "+'_______'*len(self.board))
        for row in self.board:
            print("| ",end="")
            for value in row:
                if value != 0:
                    print(str(value).rjust(4), end=" | ")
                else:
                    print("    ", end= " | ")
            print()
        print("|"+'_______'*len(self.board)+"|")

    def clear_screen(self):

        #for windows prompt
        if os.name == 'nt':
            _ = os.system('cls')

        #for mac and linux prompt(here os.name is 'posix')
        else:
            _ = os.system('clear')

        #for any IDLE remove include the below commented code
        #print("\n"*100)


    def fill_cell(self, player = 1, start = False):

        if player == 1:
        #Player starting the game
            if start == True:

                for i in range(len(self.board)):
                    for j in range(len(self.board)):
                        self.inducerList.append([i,j])

                x_choice, y_choice = random.choice(self.inducerList)

                self.board[x_choice][y_choice] = player



            else: #Subsequent player moves

                keypad_choice = random.choice(self.keypad_matrix)

                x_choice, y_choice = (keypad_choice - 1) // len(self.board), (keypad_choice - 1) % len(self.board)

                self.board[x_choice][y_choice] = player

        else:

            x_choice, y_choice = self.get_player_choice()

            self.board[x_choice][y_choice] = player

        del self.inducerList[self.inducerList.index([x_choice, y_choice])]

        keypad_value = (x_choice * len(self.board)) + (y_choice) + 1

        del self.keypad_matrix[self.keypad_matrix.index(keypad_value)]

    def get_player_choice(self):

        #print("Enter your choice of position as a number in 1-9 which is not filled")

        player_keypad_choice = int(input("Enter your choice of position as a number in 1-9 which is not filled\n\n"))

        while player_keypad_choice not in self.keypad_matrix:

            print("Invalid choice")

            player_keypad_choice = int(input("Enter your choice of position as a number in 1-9 which is not filled\n\n"))

        player_x_choice, player_y_choice = (player_keypad_choice - 1) // len(self.board), (player_keypad_choice - 1) % len(self.board)

        return [player_x_choice, player_y_choice]

    def check_game_over(self, player = 1):

        for x in range(len(self.board)):
            row_win = True
            col_win = True

            for y in range(len(self.board)):
                if self.board[x][y] != player:
                    row_win = False

                if self.board[y][x] != player:
                    col_win = False

            if row_win:
                return row_win

            if col_win:
                return col_win

            left_diag_win, right_diag_win = True, True

            for x in range(len(self.board)):
                if self.board[x][x] != player:
                    left_diag_win = False

                if self.board[len(self.board)-x-1][len(self.board)-x-1] != player:
                    right_diag_win = False

            if left_diag_win or right_diag_win:
                return True




game = game_board_tic_tac_toe()

game.board_display()

winner, counter = 0, 1

while True:

    for player in [1,2]:

        

        if counter == 1:

            game.fill_cell(player, True)


        else:

            game.fill_cell(player) 
            
        game.board_display()

        print("Board after " + str(counter) + " move")

        game.board_display()

        time.sleep(1)

        counter += 1

        if game.check_game_over(player):
            winner = player
            break

    if counter == 9:
        break
    if winner != 0:
        game.game_over = True

        game.clear_screen()
        game.board_display()
        print(str(winner) + " won the game!!!")

        break

if winner == 0:
    game.clear_screen()
    game.board_display()
    print("Its a DRAW!!!")
