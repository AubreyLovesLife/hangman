# Hangman Game
# User selects level of play: easy medium or hard (this determines the length of the word)
# Print out blank spaces for number of letters in a random word (using SOWPODS dictionary of words)
# Prompt user to guess a letter
# This program returns list of blank spaces and the correctly guessed letters, as well as a list of all the letters guessed
# Game ends when word is completely guessed, or after 9 tries

print(" ___ ") # intial hangman printout
print(" |  | ")
print(" |    ")
print(" |   ")
print(" |   ")
print(" |   ")
print("_|______")  


# a function that makes the list of letters pretty by removing [] and commas
def prettifyList(guessList):
    wordGuessOut = " ".join(guessList) # this one has spaces, to make it look nice when printing out hangman word for the game
    return (wordGuessOut) 
def collapseList(guessList):
    wordGuessOut = "".join(guessList) # this one has no spaces, to make it easy to compare wordGuess to the wordToGuess variables in the guessLetter function
    return (wordGuessOut)


# function that has a user guess a letter, then if the letter is in the word, put letter in the wordGuess list, also checks to see if full word has been guessed
def guessLetter(wordGuess,wordToGuess):

    print()
    print ("______________")
    print()
    userGuess = input("Guess a letter: ").upper()
    print ("______________") 

    letters = wordDict.values() # create list of letters from wordDict (the values)
    if userGuess in letters: # if guess is in the word, find the place it goes, and change the value
        for i in list(range(length)):
            if userGuess == wordToGuess[i]: # the keys in wordDict are ordered numerically
                wordGuess[i] = userGuess
        print()
    else:
        print()
        print ("Ooooops! This letter isn't in the word.")
        print()
        print (prettifyList(wordGuess))
        return [userGuess,"wrongGuess"]  # return a list with "wrongGuess" in the list, so in the while-loop of the play we know when to add a body part to the hangman

    print (prettifyList(wordGuess))

    if wordToGuess == str(collapseList(wordGuess)):  # checks to see if the word has been completely guessed
        print ("______________")
        print()
        print ( "Yay, you win!")
        print()
        return "endGame"

    return userGuess


# A function that picks a random word from a list of words from the SOWPODS dictionary
# the hardness parameter can be either "easy", "medium", or "hard" and determines the length of the random word
def randWord(hardness):
    
    import requests
    import random

    dictionary = requests.get('http://norvig.com/ngrams/sowpods.txt').text 

    listOfWords = dictionary.split() # create a list of words from dictionary

    level = "none"

    while hardness != level: # keep picking a random word from listOfWords until the length of the word matches the hardness level parameters

        choice = random.choice(listOfWords) # chose a random word from the list of words

        wordLength = len(choice)

        if wordLength > 9: # word size greater than 9
            level = "hard"
        elif wordLength > 5: # wordsize should be 6, 7, 8 or 9 letters long
            level = "medium"
        else: 
            level = "easy" # wordsize <= 4

    return choice

#----------------- Start of game play ------------------#

level = input("Would you like an easy, medium, or hard word?: ") # promts user for what level of hardness they would like  

hangmanWord = randWord(level) # set the word to be guessed by running the randWord function with the level input selected by user

length = len(hangmanWord)
guesses = [] # will add letter guesses to this list

guessNum = 9 # set limit to number of guesses

# convert the word to a dictionary, where the keys are numbers 0 to length and the values are the 
# letters that correspond to that number
# eg. word = "cats"  ---> wordDict = {0:'c', 1:'a', 2:'t', 3:'s'}
wordDict = {letter: hangmanWord[letter] for letter in list(range(length))}


# create list of empty spaces the length of the word to be guessed, 
# this will be the argument that goes into the guessLetter() function
wordGuessBlank = []
for i in list(range(length)): 
    wordGuessBlank.append('_')

print()
print(prettifyList(wordGuessBlank))
wrongGuess = 0   # set num of wrong guesses to 0

while wrongGuess < 9: # start of loop ------------------------------------------------------------------------------------------------------------------------------------------------------------


    guess = guessLetter(wordGuessBlank,hangmanWord) # run guessLetter function with the input of num of blanks and the hangmanWord, word to be guessed

    if "wrongGuess" in guess: # then the letter guessed isn't in the word, and the second value of the guess list is "wrongGuess"
        wrongGuess = wrongGuess + 1 # add 1 to the wrongGuess value to print out the correct hangman image

    elif guess == "endGame": # guessLetter function will return "endGame" if the wordGuess is equal to the hangmanWord, then break the loop
        break

    guesses.append(guess[0]) # add letter guessed to the list of letters guessed (must take the 0 item, because if the guess is wrong, the function returns a list with the letter guessed as the 0 value)

    print ("Your guesses so far: " + str(", ".join(guesses))) # print out the list of letters guessed


    print (" ___ ")  ######### Print out hangman image based on how many wrong guesses have been made #######
    print (" |  | ")

    if wrongGuess == 0:
        print(" |    ")
        print(" |   ")
        print(" |   ")
        print(" |   ")
        print("_|______")  
    elif wrongGuess == 1:
        print(" |   O")
        print(" |    ")
        print(" |    ")
        print(" |   ")
        print("_|______") 
    elif wrongGuess == 2:
        print(" |   O")
        print(" |   | ")
        print(" |    ")
        print(" |   ")
        print("_|______") 
    elif wrongGuess == 3:
        print(" |   O")
        print(" |   |\\ ")
        print(" |    ")
        print(" |   ")
        print("_|______")
    elif wrongGuess == 4:
        print(" |   O")
        print(" |  /|\\ ")
        print(" |     ")
        print(" |     ")
        print("_|______")  
    elif wrongGuess == 5:
        print(" |   O")  
        print(" |  /|\\ ")
        print(" |   | ")
        print(" |     ")
        print("_|______")
    elif wrongGuess == 6:
        print(" |   O")
        print(" |  /|\\ ")
        print(" |   | ")
        print(" |    \\ ")
        print("_|______") 
    elif wrongGuess >= 7:
        print(" |   O")
        print(" |  /|\\ ")
        print(" |   | ")
        print(" |  / \\ ")
        print("_|______") 
        print("Better hurry, he aint got long.")  

    # end of while loop -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 


print()
if guess != "endGame":  
    print ("Good try! The word was ", hangmanWord)  # if the word wasn't guessed before running out of guesses, print out the entire word 
else:
    print ("Good job!")

review = input("How'd you like the game? ")
print("Thanks for the input!")

  
