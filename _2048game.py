import os
import time
import random

class game_board_2048():
    """docstring for game_board_2048."""
    def __init__(self):
        self.board = [[0,0,0,0] for _ in range(4)]
        self.game_over = False

    def board_display(self):
        print(" "+'____'*len(self.board))
        for row in self.board:
            print("| ",end="")
            #print(*row, sep=" | ", end="")
            for value in row:
                if value != 0:
                    print(value, end=" | ")
                else:
                    print(" ", end= " | ")
            print()
        print(" "+'____'*len(self.board))


    def move(self,tiles, direction): #tiles: row or column

        # 0:left, 1: right, 2: up, 3: down


        if direction == 0 or direction == 2:
            new_tiles = [0,0,0,0]
            j = 0
            previous = None

            for i in range(len(tiles)):
                if tiles[i] != 0: #Number different from zero
                    if previous == None:
                        previous = tiles[i]

                    else:
                        if previous == tiles[i]:
                                new_tiles[j] = 2 * tiles[i]
                                j += 1
                                previous = None
                                if new_tiles[j-1] == 2048:
                                    self.game_over = True

                        else:
                            new_tiles[j] = previous
                            j += 1
                            previous = tiles[i]

            if previous != None:
                new_tiles[j] = previous



        elif direction == 1 or direction == 3:
            new_tiles = [0,0,0,0]
            j = len(tiles) - 1
            previous = None

            for i in range(len(tiles) - 1, -1, -1):
                if tiles[i] != 0:
                    if previous == None:
                        previous = tiles[i]

                    else:
                        if previous == tiles[i]:
                            new_tiles[j] = 2 * previous
                            j -= 1
                            previous = None
                            if new_tiles[j-1] == 2048:
                                self.game_over = True


                        else:
                            new_tiles[j] = previous
                            j -= 1
                            previous = tiles[i]

            if previous != None:
                new_tiles[j] = previous


        return new_tiles


    def check_game_over(self, game = 0):
        if game == 0:
            if self.game_over == False:
                self.clear_screen()
                print("Game Over, You lost the game!!!")
                self.board_display()

            else:
                pass

        else:
            self.clear_screen()
            print("Congratulations, You won the GAME!!!")
            self.board_display()


    def clear_screen(self):

        #for windows prompt
        if os.name == 'nt':
            _ = os.system('cls')

        #for mac and linux prompt(here os.name is 'posix')
        else:
            _ = os.system('clear')

        #for any IDLE remove include the below commented code
        #print("\n"*100)

    def fill_cell(self,new_board, start = False):

        #start: first entry in the board

        if start == True:
            inducerList = [0,1,2,3]
            new_board[random.choice(inducerList)][random.choice(inducerList)] = 2
        else:
            inducerList = []

            for i in range(len(new_board)):
                for j in range(len(new_board)):
                    if new_board[i][j] == 0:
                        inducerList.append([i,j])

            row_choice, col_choice = random.choice(inducerList)

            new_board[row_choice][col_choice] = 2

        return new_board


    def game_turn(self, direction):
        new_board = []
        moved = False

        if direction == 0 or direction ==1:
            for i in range(len(self.board)):
                new_board.append(self.move(self.board[i], direction))
                #self.check_game_over()
        else:
            new_board_transpose = []
            board_transpose = [[self.board[j][i] for j in range(4)] for i in range(4)]
            for i in range(len(board_transpose)):
                new_board_transpose.append(self.move(board_transpose[i], direction))
            new_board = [[new_board_transpose[j][i] for j in range(4)] for i in range(4)]



        if all([new_board[i] == self.board[i] for i in range(len(self.board))]) and any([False if 0 in row else True for row in self.board]):
            #move is invalid and game is over
            self.game_over = False
            self.check_game_over()
        else:
            moved = True
            new_board = self.fill_cell(new_board)
            self.board = new_board

        if self.game_over == True:
            self.check_game_over(1)



game = game_board_2048()
#print(game.board)
game.fill_cell(game.board, True)
while True:

    print("  2048 Game  ")
    game.board_display()

    print("Enter your choice as follows:")
    print("0: Left")
    print("1: Right")
    print("2: Top")
    print("3: Bottom")

    direction = int(input())

    game.game_turn(direction)

    game.clear_screen()

    time.sleep(1)
