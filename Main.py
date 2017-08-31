#!/usr/bin/env python
'''Final Project
Daniel Whitt
8/30/2017

This runs the HangMan.py
'''

import HangMan
import sys

test = HangMan.HangMan()
#instantiates HangMan


try:
    if __name__ == "__main__":
        get_word = test.wordList(sys.argv[1],sys.argv[2])
        test.main(get_word)
        #this allows us to get input from the command line
except IndexError:
    print("Please only enter two extra words")
    #if we get an IndexError, we instead print the above statement