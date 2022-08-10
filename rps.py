from colorama import Fore, Style
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

# moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    # Making the moves variable a class-level variable
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        # Giving an initial value to their move when the game starts
        self.their_move = random.choice(self.moves)
        # For the CyclePlayer class to get an initial start value
        self.my_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)


class ReflectPlayer(Player):
    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == self.moves[0]:
            return self.moves[1]
        elif self.my_move == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]


class HumanPlayer(Player):
    def move(self):
        # while loop to prevent crashing from invalid input
        while True:
            human_move = input("Play either rock, paper or scissors :-"
                               ).lower()
            if human_move in self.moves:
                return human_move
            elif human_move == "quit":
                return quit()
