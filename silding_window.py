import random
import os
import time


class game_board_sliding_window():

    def __init__(self):

        #Initializing the game

        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.keypad_matrix = [1,2,3,4,5,6,7,8]
        self.inducer_positions = []

        for i in range(len(self.board)):
            for j in range(len(self.board)):
                self.inducer_positions.append([i,j])


    def create_board(self):

        #Initializing the game board

        for i in range(8):

            x_choice, y_choice = random.choice(self.inducer_positions)

            value_choice = random.choice(self.keypad_matrix)

            self.board[x_choice][y_choice] = value_choice

            del self.inducer_positions[self.inducer_positions.index([x_choice, y_choice])]

            del self.keypad_matrix[self.keypad_matrix.index(value_choice)]

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


    def check_game_over(self):

        return self.board == [[1,2,3], [4,5,6], [7,8,0]]

    def move(self, direction):

        moved = False

        if direction == 0:

            for i in range(len(self.board)):
                for j in range(len(self.board)):
                    if self.board[i][j] == 0:
                        self.board[i][j], self.board[i][j-1] = self.board[i][j-1], self.board[i][j]
                        moved = True
                        break
                if moved:
                    break

        elif direction == 1:

            for i in range(len(self.board)):
                for j in range(len(self.board)):
                    if self.board[i][j] == 0:
                        self.board[i][j], self.board[i][j+1] = self.board[i][j+1], self.board[i][j]
                        moved = True
                        break
                if moved:
                    break

        elif direction == 2:

            for i in range(len(self.board)):
                for j in range(len(self.board)):
                    if self.board[i][j] == 0:
                        self.board[i][j], self.board[i-1][j] = self.board[i-1][j], self.board[i][j]
                        moved = True
                        break
                if moved:
                    break

        else:

            for i in range(len(self.board)):
                for j in range(len(self.board)):
                    if self.board[i][j] == 0:
                        self.board[i][j], self.board[i+1][j] = self.board[i+1][j], self.board[i][j]
                        moved = True
                        break
                if moved:
                    break

    def get_possible_moves(self):

        #getting the liable or possible moves of the empty box

        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    empty_box_x_position, empty_box_y_position = i, j
                    break

        possible_moves = [0, 1, 2, 3]

        if empty_box_y_position == 0: del possible_moves[possible_moves.index(0)]
        if empty_box_y_position == len(self.board) - 1 : del possible_moves[possible_moves.index(1)]
        if empty_box_x_position == 0: del possible_moves[possible_moves.index(2)]
        if empty_box_x_position == len(self.board) - 1 : del possible_moves[possible_moves.index(3)]

        return possible_moves




game = game_board_sliding_window()

game.create_board()

game.board_display()

counter = 0

win = False

while True:

    liable_moves = game.get_possible_moves()

    print("Enter your move as follows to move the empty box")

    while True:

        for i in liable_moves:

            if i == 0: print("0: Left")
            elif i == 1: print("1: Right")
            elif i == 2: print("2: Top")
            else : print("3: Bottom")

        player_move = int(input())

        if player_move in liable_moves:
            break
        else:
            print("Invalid choice! Enter a correct choice as follows")

    game.move(player_move)

    counter += 1

    win = game.check_game_over()

    game.clear_screen()

    time.sleep(1)

    game.board_display()

    if win == True:
        break

print("You won the game in "+ str(counter) + " moves.")

game.board_display()

close = input()
