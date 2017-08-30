import random
import string

class HangMan():
    def __init__(self):
        self.self = self

    def wordList(self,word1,word2):
        words = ["Jon", "Tyrion", "Sansa", "Arya"]
        words.extend([word1,word2])
        word = random.choice(words).upper()
        return word

    def wordCheck(self, word, guesses, guess):
        status = " "
        i = 0
        matches = 0
        for letter in word:
            if guesses[letter]:
                status += letter
            else:
                status += "*"
            if letter == guess:
                matches += 1

        if matches >= 1:
            print("Yes :) The word contains a match for: ", guess)
        else:
            print("Sorry :( The word does not contain a match for: ", guess)

        return status

    def main(self,word):
        test = HangMan()
        guesses = dict.fromkeys(string.ascii_uppercase, False)
        guessed = False
        print("The word contains", len(word), "letters.")
        while guessed == False:
            text = "Please enter a one letter guess or an entire word as a guess: "
            guess = input(text).upper()
            if guess in guesses.keys() and guesses[guess] == True:
                print('You already guessed "', guess, '"')
            elif len(guess) == len(word):
                guesses[guess] = True
                if guess == word:
                    guessed = True
                else:
                    print("Sorry, {} is the wrong word.".format(guess))
            elif len(guess) == 1:
                guesses[guess] = True
                result = test.wordCheck(word, guesses, guess)
                if result == word:
                    guessed = True
                else:
                    print(result)
            else:
                print("Invalid entry. Please try again.")

        print("Yes, the word is", word, "! You got it in ", sum(guesses.values()), "tries.")
        with open('word.txt', 'w') as file:
            file.write("The word was: " + word)