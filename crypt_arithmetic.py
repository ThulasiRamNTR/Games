import os
import random
import time


class game_board_crypt_arithmetic():

    #Initializing the game board
    def __init__(self):
        self.board = []
        self.user_value_board = ['*' for i in range(10)]
        self.game_over = False

    def board_display(self, user_value = False):

        max_word_len = 0

        for word in self.board:
            if len(word) > max_word_len:
                max_word_len = len(word)

        max_word_len += 1 #Increased by one for storing the operator

        if not user_value:
            print(" "+'_______'*(max_word_len))

            for word_index in range(len(self.board)):
                print("| ",end="")
                if word_index < len(self.board) - 2:
                    for char in self.board[word_index].rjust(max_word_len):
                        print(char.rjust(4), end=" | ")
                    print()
                elif word_index == len(self.board) - 2:
                    curr_word = self.board[word_index].rjust(max_word_len)
                    curr_word_with_operator = '+'+curr_word[1::]
                    for char in curr_word_with_operator:
                        print(char.rjust(4), end=" | ")
                    print("\n|"+'_______'*(max_word_len)+"|")
                else:
                    for char in self.board[word_index].rjust(max_word_len):
                        print(char.rjust(4), end=" | ")
                    print()
            print("|"+'_______'*(max_word_len)+"|")

        else:
            print(" "+'_______'*(10))
            print("| ",end="")
            for index in range(10):
                print(str(index).rjust(4), end=" | ")
            print()
            print("|"+'_______'*(10)+"|")
            print("| ", end="")
            for char in self.user_value_board:
                if char != '*' :
                    print(str(char).rjust(4), end=" | ")
                else:
                    print("    ", end=" | ")
            print("\n|"+'_______'*(10)+"|")


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

        char_set = ""

        for word in self.board:
            char_set += word

        char_set = set(char_set)

        for char in char_set:
            if char not in self.user_value_board:
                return -1

        carry = 0

        max_word_len = 0

        for word in self.board:
            if len(word) > max_word_len:
                max_word_len = len(word)

        word_list = []

        for word in self.board:
            word_list.append(word.rjust(max_word_len))

        for y_index in range(max_word_len-1, -1, -1):
            char_sum = 0
            for x_index in range(len(word_list)-1):
                if word_list[x_index][y_index] != " ":
                    char_sum += self.user_value_board.index(word_list[x_index][y_index])
            char_sum += carry

            char_sum, carry = (char_sum % 10), (char_sum // 10)

            if char_sum != self.user_value_board.index(word_list[len(word_list)-1][y_index]):
                return 1

        return 2


    def set_board(self):

        #Getting input from the document and storing into the game board

        crypt_questions = ["SEND + MORE = MONEY","WIRE + MORE = MONEY","WRONG + WRONG = RIGHT","LETTERS + ALPHABET = SCRABBLE","BASE + BALL = GAMES","GERALD + DONALD = ROBERT","ATTRACTIONS + INTENTIONS = REGENERATION","LIONNE + TIGRE = TIGRON","WEIN + WEIB = LIEBE"]

        crypt_question_choice = random.choice(crypt_questions)

        question_word, answer_word = crypt_question_choice.split(" = ")

        questions_word_list = question_word.split(" + ")

        for word in questions_word_list:
            self.board.append(word)

        self.board.append(answer_word)


    def set_input(self, remove = False):

        char_set = ""

        for word in self.board:
            char_set += word

        char_set = set(char_set)

        if not remove:
            while True:
                try:
                    print("Enter the character to set your value in 'CAPS'")

                    char = input().strip()

                    if char not in char_set:
                        raise(MyError())

                    print("Enter your value for " + char + " between 0-9")

                    user_value = int(input())

                    if user_value not in [counter for counter in range(0,10,1)]:
                        raise(MyError())

                    self.user_value_board[user_value] = char

                    break
                except:
                    print("Invlalid character/value! Enter a correct value as follows:")

        else:
            while True:
                try:
                    print("Enter the character to remove your current value in 'CAPS'")

                    char = input().strip()

                    if char not in char_set:
                        raise(MyError())

                    print("Enter your new_value for " + char + " between 0-9")

                    user_value = int(input())

                    if user_value not in [counter for counter in range(0,10,1)]:
                        raise(MyError())

                    self.user_value_board[self.user_value_board.index(char)] = '*'

                    self.user_value_board[user_value] = char

                    break
                except:
                    print("Invlalid character/value! Enter a correct value as follows:")


class MyError(Exception):

    # Constructor or Initializer
    def __init__(self, value = False):
        self.value = value

    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))



game = game_board_crypt_arithmetic()

game.set_board()

win = 0

while True:

    game.board_display()

    game.board_display(True)

    print("Enter your input as follows")
    print("0: Enter a value for a character")
    print("1: Replace a value for an existing character")
    print("2: Check the input values for characters")

    while True:

        choice = int(input())

        try:
            if choice not in [0,1,2]:
                raise(MyError())
            else:
                if choice == 0:
                    game.set_input()
                elif choice == 1:
                    game.set_input(True)
                else:
                    win = game.check_game_over()

                break
        except:
            print("Invalid choice! Enter your choice as follows")


    game.clear_screen()

    time.sleep(1)

    if win != 0:
        if win == -1:
            print("Sorry! You haven't given enough inputs for the required character!")
        elif win == 1:
            print("Sorry! You lost! You haven't given the values correctly!")
        else:
            print("Congrats! You solved the crypt_arithmetic problem correctly!")
        break

input()
