import HangMan
import sys

test = HangMan.HangMan()


try:
    if __name__ == "__main__":
        get_word = test.wordList(sys.argv[1],sys.argv[2])
        test.main(get_word)
except IndexError:
    print("Please only enter two extra words")