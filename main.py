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


# this subclass give you the possibility to play against the computer and make your moves
class HumanPlayer(Player):
    def move(self):
        human_move = input('Make a move. Chosse between Rock, Paper or Scissors: ').lower()
        if human_move in moves:
            return human_move
        print('This move is invalid, try again!')


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is not None:
            return self.their_move
        else:
            return random.choices(moves)
        
    def learn(self, my_move, their_move):
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


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
            print('Player 1 wins!')
            self.player1_score += 1
            print(f'Player 1 score = {self.player1_score}')
            print(f'Player 2 score = {self.player2_score}')
        elif beats(move2, move1):
            print('Player 2 wins!')
            self.player2_score += 1
            print(f'Player 1 score = {self.player1_score}')
            print(f'Player 2 score = {self.player2_score}')
        else:
            print('Players done the same move. It is a Tie!')
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):  
            print(f"Round {round}:")
            self.play_round()
        print(f"Final scores:")
        print(f"Player 1: {game.player1_score}")
        print(f"Player 2: {game.player2_score}")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()