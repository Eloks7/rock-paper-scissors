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

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.p1_score += 1
            print("Player One wins this Round")
        elif move1 == move2:
            print("Couldn't agree on a winner")
        else:
            self.p2_score += 1
            print("Player Two wins this Round")
        print("Player one -- " + str(self.p1_score) + " & "
              "Player Two -- " + str(self.p2_score))
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
    
    def play_game(self):
        print(Fore.RED + "Game start!\n")
        print(Style.RESET_ALL)
        print("This is a 3 Round game\n")
        print("Type 'quit' when you want to quit\n")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
            if self.p1_score - self.p2_score == "2":
                return print(Fore.RED + "FATALITY!!! Player 1 has won already")
            elif self.p2_score - self.p1_score == "2":
                return print(Fore.RED + "FATALITY!!! Player 2 has already won")
        print(Style.RESET_ALL)
        # Checking for winner
        if self.p1_score > self.p2_score:
            print("Player 1 (" + str(self.p1_score) + ") : ("
                  + str(self.p2_score) + ") Player 2\n")
            print(Fore.GREEN + "Player 1 Champion")
            print(Style.RESET_ALL)
        elif self.p2_score > self.p1_score:
            print("Player 1 (" + str(self.p1_score) + ") : ("
                  + str(self.p2_score) + ") Player 2\n")
            print(Fore.GREEN + "Player 2 Champion")
            print(Style.RESET_ALL)
        else:
            print("Player 1 (" + str(self.p1_score) + ") : ("
                  + str(self.p2_score) + ") Player 2\n")
            print(Fore.YELLOW + "No Victor, No Vanquished")
            print(Style.RESET_ALL)

        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
