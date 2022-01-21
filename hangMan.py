#including the random module for secret word selection
import random

#premade list of words
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


#ascii art for the hangman game
hangManPics = ['''
     +----+
     |    O
     |   /|\\
     |   / \\
     ===''','''
     +----+
     |    O
     |   /|\\
     |   /
     ===''','''
     +----+
     |    O
     |   /|\\
     |
     ===''','''
     +----+
     |    O
     |   /|
     |
     ===''','''
     +----+ 
     |    O 
     |    |
     |   
     ===''','''
     +----+
     |    O
     |
     |
     ===''','''
     +----+
     |
     |
     |
     ===''']

#this function returns a random word from a predetermined list of strings
def getRandomWord(wordlist):
    wordIndex = random.randint(0, len(wordlist) -1)
    return wordlist[wordIndex]

#intro text
print()
print("Let's play Hangman")

#The secret word players are attempting to guess
secretWord = getRandomWord(words)

#The incorrect letters guesses
lettersGuessed = ""

#the number of guesses a player has before loosing the game
failCount = 6

#loop until player has made too many incorrect guesses
#break loop if player succeeds in guessing word

while failCount > 0:

    #get guess from player but only store the first letter
    guess =  input("\nenter a letter: ")[0]

    if guess in secretWord:
        #player guess letter in the word correctly
        print(f"Correct there is one or more {guess} in the secret word")
    else:
        #player guess incorrect
        failCount -= 1
        print(f"Incorrect, {guess} was not a part of the secret word. You have {failCount} guesses remaining")

    #Gather a list of all pervious guesses from the user
    lettersGuessed = lettersGuessed + guess
    wrongLetterCount = 0

    #display the ascii art
    print(hangManPics[failCount])

    #small loop to display discovered letters
    for letter in secretWord:
        if letter in lettersGuessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrongLetterCount += 1

    if wrongLetterCount == 0:
        print(f"\nYou did it the secret word was {secretWord}. A winner is you!")
        break

else:
    print(f"\nSorry you are out of guesses. The word was {secretWord}. Try again!")