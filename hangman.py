# A program for playing hangman
# Import the images of the gallows that will be displayed to screen
from images import images

class HangMan():
    from images import images

    def __init__(self, word):
        self.word = word
        self.correct_guesses = []
        self.incorrect_guesses = []

    def __str__(self):
        list = [x if x in self.correct_guesses else "_" for x in self.word]
        return "".join(list)

    def make_guess(self, guess):
        if guess in self.correct_guesses or guess in self.incorrect_guesses:
            # Already guessed!
            print("You already guessed that...")
        elif guess in self.word:
            # Correct guess
            print("You guessed correctly!")
            self.correct_guesses.append(guess)
        else:
            # Incorrect guess
            print("You guessed incorrectly :(")
            self.incorrect_guesses.append(guess)

    def print_state(self):
        num_wrong_guesses = len(self.incorrect_guesses)
        border = "\n\n------------------------------\n\n"
        print(border)
        print(images[num_wrong_guesses])
        print(f"Incorrect guesses: {' - '.join(self.incorrect_guesses)}")
        print(f"Word: {self}")
        print(border)

    def play(self):
        print("Let's play hangman!")
        print("Word:", self, "\n")

        won = lost = False
        while not (won or lost):

            self.make_guess(input("What is your guess?: "))
            self.print_state()

            won = (str(self) == self.word)
            lost = (len(self.incorrect_guesses) == len(images))

        if won:
            print("\n\n\n\nWell done!")
            print(f"You correctly guessed the word was {self.word}\n\n")
        else:
            print(f"\n\n\n\nUnlucky bud, you lost.\nThe word was {self.word}")

        print("Game Finished")


def main():
    from random import choice

    DICTIONARY_FILE_NAME = "words.txt"

    # Open file, ignore commented lines, and remove trailing '\n'
    with open(DICTIONARY_FILE_NAME, "r") as filein:
        word_list = [word.rstrip("\n") for word in filein.readlines()
                     if not word.startswith('#')]

    # choose a word at random using random module, and play the game.
    word = choice(word_list)
    HangMan(word).play()

if __name__ == "__main__":
    main()
