#!/usr/bin/env python
'''Final Project
Daniel Whitt
8/30/2017

These functions allow us to play the game Hangman
'''

import random
import string

class HangMan():
    def __init__(self):
        #this just initializes the class HangMan and does not take any arguments
        self.self = self

    def wordList(self,word1,word2):
        #this creates the possible words that have to be guessed
        #it takes in two arguments
        words = ["Jon", "Tyrion", "Sansa", "Arya"]
        words.extend([word1,word2])
        word = random.choice(words).upper()
        #a word is randomly picked and then returned as the output of this function
        return word

    def wordCheck(self, word, guesses, guess):
        #this function takes the word that was selected, the dictionary of guesses, and the user's guess
        #it will check the guess against the actual word and return the letters of the word that have been guessed
        word_status = ""
        matches = 0
        for letter in word:
            if guesses[letter]:
                word_status = word_status + letter
            else:
                word_status = word_status + "*"
            if letter == guess:
                matches = matches + 1

        if matches >= 1:
            print("Yes :) The word contains a match for: ", guess)
        else:
            print("Sorry :( The word does not contain a match for: ", guess)

        #It will print out if there was a match or not
        #It also returns the status of the unknown word after the guess
        #It will show letters that have been guessed and it will hide letters that have not been guessed
        return word_status

    def main(self,word):
        #This is the main function that actually runs HangMan
        #The input is the random word that was selected
        #It will ask the user for their guess and it will return how many matches there, if any
        #If there were matches, it will show the word with those letters revealed
        #Once the word is guessed correctly, it will display how many attempts it took along with writing
        #the word to a .txt file
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