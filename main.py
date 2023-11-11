"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


# these are the possible moves
moves = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""

class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass