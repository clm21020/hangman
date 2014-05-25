import random

words_list = ["HELLO", "LULZ", "ROFLER", "TABLE", "CHAIR", "TREAT", "GOLDFISH", "COOKIE", "APPLE", "ORANGE"]

def new_game_setup ():
    return choose_word(words_list), "", 5

def prompt_user():
    user_guess = raw_input("Please guess a single letter: ")  
    return user_guess

def choose_word(words_list):
    the_word = words_list[random.randint(0,9)]
    return the_word

def hide_the_word(the_word, letters_guessed): 
    hidden_word = ""
    for i in xrange(0,len(the_word)):
        if the_word[i] in letters_guessed:
            hidden_word = hidden_word + the_word[i]
        else:
            hidden_word = hidden_word + "_"
    return hidden_word

def valid_guess(guess, letters_guessed):
    return len(guess) == 1 and guess.isalpha() and guess not in letters_guessed

def wrong_guess(misses_remaining):
    if misses_remaining <= 4: print("   O   ".center(15))
    if misses_remaining <= 3: print(" \_|_/ ".center(15)) 
    if misses_remaining <= 2: print("   |   ".center(15))
    if misses_remaining <= 1: print("  / \  ".center(15))
    if misses_remaining == 0: print(" d   b ".center(15))
    print("Misses Remaining: " + str(misses_remaining))
    
def hanged(the_word):
    print("You're hanged!")
    print("The word was " + the_word)

def winner(the_word):
    print("You won!")
    print("The word was " + the_word)

def play_hangman(the_word, letters_guessed, misses_remaining):
    while(True): #beginning of round--each time through is a turn
        hidden_word = hide_the_word(the_word, letters_guessed)
        if hidden_word == the_word: #check for win
            winner(the_word)
            return #breaks out of the function play_hangman 
        print hidden_word
        guess = prompt_user().upper()
        if valid_guess(guess, letters_guessed):
            letters_guessed = letters_guessed + guess
            print("Letters guessed: " + letters_guessed)
            if guess not in the_word: #check for wrong guess
                misses_remaining -= 1
                wrong_guess(misses_remaining)
                if misses_remaining == 0: #check for loss
                    hanged(the_word)
                    return #breaks out of the function play_hangman 


print("Welcome to Hangman!")
while(True):
    the_word, letters_guessed, misses_remaining = new_game_setup()
    print (the_word) #take out when finished
    play_hangman(the_word, letters_guessed, misses_remaining)
    close_game = raw_input("Would you like to play again? (yes/no) ")
    if close_game.upper() == "NO":
        break













