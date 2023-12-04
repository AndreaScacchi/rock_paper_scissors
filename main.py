"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


# import statements
import random


# these are the possible moves
moves = ['rock', 'paper', 'scissors', 'spock', 'lizard']


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# a subclass thay always plays rock
class AllRockPlayer(Player):
    pass


# this subclass returns a random choice between
# ['rock', 'paper, 'scissors', 'spock', 'lizard']
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# this subclass give you the possibility to play against the computer
# and make your moves
class HumanPlayer(Player):
    def move(self):
        # the 'while' creates an infinite loop, prompting the user to enter
        # a move repeatedly until a valid move is provided
        while True:
            # prompt the user to input a move, converting it to lowercase
            human_move = input('\033[1;32mMake a move. Rock, Paper '
                               'Scissors, Spock or Lizard? \033[0m').lower()
            # check if the entered move is one of the valid moves
            if human_move in moves:
                return human_move
            print('\033[1;31mThis move is invalid, try again!\033[0m')


# this subclass remembers the previous move the opponent played last round and
# plays that move in the next round
class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.their_move = None

    def move(self):
        if self.their_move is not None:
            return self.their_move
        else:
            return random.choice(moves)

    def learn(self, my_move, their_move):
        self.their_move = their_move


# this sublcass remembers what move it played last round and cycles through
# the three moves
class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.my_move = None

    def move(self):
        if self.my_move is not None:
            # find the index of the player's previous move in the moves list
            index = moves.index(self.my_move)
            # calculate the index of the next move i a cyclic manner.
            # if the player's previous move was the last one in the list,
            # it wraps around to the first move
            next_move_index = (index + 1) % len(moves)
            return moves[next_move_index]
        else:
            return random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move


# this function tells whether one move beats another one
# it employs a dictionary to map each choice to a list of options it can defeat
# the get method retieves the list corresponding to the first argument(one)
# from the dictionary, and if one is not a key in the dictionary,
# it returns an empty list. The function then checks if the second
# argument(two) exists in this list and returns a Boolean result accordingly
def beats(one, two):
    return two in {
        'rock': ['scissors', 'lizard'],
        'scissors': ['paper', 'lizard'],
        'paper': ['rock', 'spock'],
        'spock': ['scissors', 'rock'],
        'lizard': ['spock', 'paper']
    }.get(one, [])


# this class starts the game. The play_round method simulates a single round
# of the game. The play_game method executes the entire game.
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.player1_score = 0  # initialize player 1's score to zero
        self.player2_score = 0  # initialize player 2's score to zero

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f'\033[1;34mPlayer 1: {move1} - Player 2: {move2}\033[0m')
        if move1 == move2:
            print('\033[1;35mPlayers made the same move. It is a Tie!\033[0m')
        elif beats(move1, move2):
            print('\033[1;36mPlayer 1 wins the round!\033[0m')
            self.player1_score += 1
            print(f'\033[1;36mPlayer 1 score = {self.player1_score}\033[0m')
            print(f'\033[1;33mPlayer 2 score = {self.player2_score}\033[0m')
        else:
            print('\033[1;33mPlayer 2 wins the round!\033[0m')
            self.player2_score += 1
            print(f'\033[1;36mPlayer 1 score = {self.player1_score}\033[0m')
            print(f'\033[1;33mPlayer 2 score = {self.player2_score}\033[0m')
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print('\033[1;37mGAME START!\033[0m')
        for round in range(3):
            print(f'\033[1;30mROUND {round}:\033[0m')
            self.play_round()

        # check if the score of player 1 is greater to the score of player 2
        if self.player1_score > self.player2_score:
            print('\033[1;36mPlayer 1 wins the game!\033[0m')
        # check if the score of player 2 is greater to the score of player 1
        elif self.player2_score > self.player1_score:
            print('\033[1;33mPlayer 2 wins the game!\033[0m')
        else:
            print('\033[1;35mIt is a tie game!\033[0m')

        print(f'\033[1;32mFINAL SCORES:\033[0m')
        print(f'\033[1;36mPLAYER 1: {game.player1_score}\033[0m')
        print(f'\033[1;33mPLAYER 2: {game.player2_score}\033[0m')
        print('\033[1;37mGAME OVER!\033[0m')


# this code allows to test and observe how differnt player strategies
# interact with a human player in the game.
if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()

    cycle_game = Game(HumanPlayer(), CyclePlayer())
    cycle_game.play_game()
