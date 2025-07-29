"""A number guessing game where the computer gives clues on whether the number
is higher or lower than the actual guess"""
import random
import os
from enum import Enum

def binary_search_strategy(max_value: int, correct_guess: int) -> int:
    """Implements a binary search for the values"""
    min_value = 1
    max_value = max_value + 1
    tries = 0
    while min_value <= max_value:
        assert tries < 1000, f"{min_value=}, {max_value=}, {correct_guess=}"
        tries +=1
        guess = (min_value + max_value) // 2
        if guess == correct_guess:
            return tries
        elif guess < correct_guess:
            min_value = guess
        else:
            max_value = guess
    return tries

def linear_search_strategy(max_value: int, correct_guess: int) -> int:
    tries = 0
    for guess in range(1, max_value + 1):
        tries += 1
        if guess == correct_guess:
            return tries

def random_search_strategy(max_value: int, correct_guess: int) -> int:
    tries = 0
    guesses = list(range(1, max_value +1))
    random.shuffle(guesses)
    for guess in guesses:
        tries += 1
        if guess == correct_guess:
            return tries


class PlayerType(Enum):
    AI = 0
    human = 1



class Game:
    def __init__(self,
                 max_guess=10,
                 player_type=PlayerType.human,
                 strategy = '',
                 save_file=None):
        """Initialises the game"""
        self.max_guess = max_guess
        self.correct_guess = random.randint(1, max_guess)
        self.tries = 0
        self.save_file = save_file
        self.player_type = player_type
        self.strategy = strategy
        if player_type == PlayerType.human:
            while True:
                self.play()
                print("Would you like to play again?")
                reply = input("(y/n̲) > ").lower()
                if reply != 'y':
                    break

    def ai_play(self, strategy):
        self.tries = strategy(self.max_guess, self.correct_guess)
        if self.save_file:
            self._save_results()

    def play(self):
        """play the game by asking the user for input"""
        while True:
            self.tries += 1
            print(f"Enter a guess between 1 and {self.max_guess}")
            try:
                guess = int(input(f"1-{self.max_guess}> "))
            except ValueError:
                print("You must use an integer!")
                continue
            if guess == self.correct_guess:
                print("You win!")
                print(f"It took you {self.tries} tries")
                break
            print((f"You guess is {'lower' if guess < self.correct_guess else 'higher'}"
                   " than the actual number"))
        if self.save_file:
            self._save_results()

    def _save_results(self):
        "saves the results to a csv file"
        with open(self.save_file, 'a') as f:
            if f.tell() == 0:
                f.write("max_number, tries, player type, strategy")
            f.write(f"\n{self.max_guess}, {self.tries}, {self.player_type.value}, {self.strategy}")





if __name__ == '__main__':
    max_values = [10, 100, 1000, 10_000]
    strategies = {'binary_search': binary_search_strategy,
                  'linear_search': linear_search_strategy,
                  'random_search': random_search_strategy}
    for desc, strategy in strategies.items():
        for max_val in max_values:
            for _ in range (100):
                Game(max_guess=max_val,
                     player_type=PlayerType.AI,
                     strategy=desc,
                     save_file='results.csv').ai_play(strategy)
