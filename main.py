"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


# import statements
import random


# these are the possible moves
moves = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# this subclass returns a random choice between ['rock', 'paper, 'scissors']
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# this subclass give you the possibility to play against the computer
# and make your moves
class HumanPlayer(Player):
    def move(self):
        while True:
            human_move = input('Make a move.'
                               'Choose Rock, Paper or Scissors: ').lower()
            if human_move in moves:
                return human_move
            print('This move is invalid, try again!')


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
            index = moves.index(self.my_move)
            next_move_index = (index + 1) % len(moves)
            return moves[next_move_index]
        else:
            return random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move


# this function tells whether one move beats another one
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


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
        print(f'Player 1: {move1} Player 2: {move2}')
        if beats(move1, move2):
            print('Player 1 wins the round!')
            self.player1_score += 1
            print(f'Player 1 score = {self.player1_score}')
            print(f'Player 2 score = {self.player2_score}')
        elif beats(move2, move1):
            print('Player 2 wins the round!')
            self.player2_score += 1
            print(f'Player 1 score = {self.player1_score}')
            print(f'Player 2 score = {self.player2_score}')
        else:
            print('Players done the same move. It is a Tie!')
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("GAME START!")
        for round in range(3):
            print(f"ROUND {round}:")
            self.play_round()

        if self.player1_score > self.player2_score:
            print("Player 1 wins the game!")
        elif self.player2_score > self.player1_score:
            print("Player 2 wins the game!")
        else:
            print("It's a tie game!")

        print(f"FINAL SCORES:")
        print(f"PLAYER 1: {game.player1_score}")
        print(f"PLAYER 2: {game.player2_score}")
        print("GAME OVER!")


# this code allows to test and observe how differnt player strategies
# interact with a human player in the game.
if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()

    cycle_game = Game(HumanPlayer(), CyclePlayer())
    cycle_game.play_game()
