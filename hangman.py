# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    userGuess = ''
    for le in secret_word:
        for letter in letters_guessed:
            if le == letter:
                userGuess =  userGuess + letter
    return userGuess == secret_word
#Test code to see if method works
#print(is_word_guessed('brrick', ['k','r','d','i','c','b']))

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    userGuess = []
    for char in secret_word:
        userGuess.append(('_ '))
    for x in range(len(secret_word)):
        for guess in letters_guessed:
            if guess == str(secret_word[x]):
                userGuess[x] = guess + ' '
    return ''.join(userGuess)
#Test code to see if method works
#print(get_guessed_word('geek', ['v','g','z','v','h','k']))


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    lettersLeft = []
    import string
    alphabet = string.ascii_lowercase
    lettersLeft[:0] = alphabet
    for l in letters_guessed:
        for alpha in lettersLeft:
            if l == alpha:
                del  lettersLeft[lettersLeft.index(alpha)]
    return ''.join(lettersLeft)
#print(get_available_letters(['c', 'b', 'a','z', 'd', 'k']))

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # guessesLeft = 6
    # warnings = 4
    # guessedLetters = []
    # vowels = ['a','e','i','o','u']
    # playerWins = False
    #
    # def show_turns():
    #     if warnings < 4:
    #         print('You have ' + str(warnings) + ' warnings left.')
    #     print('You have ' + str(guessesLeft) + ' guesses remaining.')
    #     print('Available letters: ' + get_available_letters(guessedLetters))
    #
    #
    #
    # print('Lets play a game of Hangman!\n'
    #       'I\'m thinking of a word that\'s ' + str(len(secret_word)) + ' letters long.\n'
    #       'Vowels count as 2 guesses and consonants count as 1. Good luck!')
    # show_turns()
    #
    # while guessesLeft > 0 and playerWins == False:
    #     guess = input('Please guess a letter: ')
    #     if str(guess) in guessedLetters:
    #         if warnings > 0:
    #             warnings -= 1
    #         else:
    #             guessesLeft -= 1
    #         print(
    #             'Oops! You already guessed that letter. You have ' + str(warnings) + '  warnings left: ' + get_guessed_word(
    #                 secret_word, guessedLetters))
    #         show_turns()
    #     elif secret_word.find(guess) >=  0:
    #         guessedLetters.append(guess)
    #         print('Good guess: ' + get_guessed_word(secret_word,guessedLetters))
    #         show_turns()
    #         playerWins = is_word_guessed(secret_word,guessedLetters)
    #     elif len(guess) != 1 or not guess.isalpha():
    #         if warnings > 0:
    #             warnings -= 1
    #             print('Oops! That is not a valid letter. You have ' + str(
    #                 warnings) + '  warnings left: ' + get_guessed_word(secret_word, guessedLetters))
    #         else:
    #             guessesLeft -= 1
    #             print('Oops! That is not a valid letter. You have no warnings left, so you lose a guess: ' + get_guessed_word(secret_word, guessedLetters))
    #         show_turns()
    #     else:
    #         guessedLetters.append(guess)
    #         if str(guess) in vowels:
    #             guessesLeft -= 2
    #         else:
    #             guessesLeft -= 1
    #         print('Oops, that letter isn\'t correct: ' + get_guessed_word(secret_word,guessedLetters))
    #         show_turns()
    #     print('----------')
    #
    #
    # if playerWins:
    #     print('Congratulations, you won!\nYour total score is: ' + str(guessesLeft * len(secret_word)))
    # elif guessesLeft == 0:
    #     print('Sorry, you\'re all out of guesses. The word was "' + secret_word + '".')
#hangman('sspidder')


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, secret_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    gappedWord = ''

    noSpaces = my_word.replace(' ','')
    isMatched = False

    for letter in my_word:
        if letter.isalpha():
            gappedWord = gappedWord + letter
            isMatched = True

    for letter in str(gappedWord):
        if secret_word.find(letter) <  0 or len(noSpaces) != len(secret_word):
            isMatched = False
        else:
            for x in range(len(noSpaces)):
                if noSpaces[x].isalpha() and noSpaces[x] != secret_word[x]:
                    isMatched = False

    return isMatched

#print(match_with_gaps('p _ _ r', 'pree'))

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possibleWords = []

    for word in wordlist:
        if match_with_gaps(my_word, word):
            possibleWords.append(word)

    if len(possibleWords) > 0:r
        return ' '.join(possibleWords)
    else:
        return('No matches found.')

#print(show_possible_matches('p _ _ r'))


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    usedHint = False
    guessesLeft = 6
    warnings = 4
    guessedLetters = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    playerWins = False


    def show_turns():
        if warnings < 4:
            print('You have ' + str(warnings) + ' warnings left.')
        print('You have ' + str(guessesLeft) + ' guesses remaining.')
        print('Available letters: ' + get_available_letters(guessedLetters))

    print('Lets play a game of Hangman!\n'
          'I\'m thinking of a word that\'s ' + str(len(secret_word)) + ' letters long.\n'
                                                                       'Vowels count as 2 guesses and consonants count as 1.\n'
                                                                       'If you get stuck, you can have 1 hint by entering "*" instead of a letter.')
    show_turns()

    while guessesLeft > 0 and playerWins == False:
        guess = input('Please guess a letter: ').lower()
        if guess == '*' and not usedHint:
            if len(guessedLetters) > 0:
                usedHint = True
            print('Possible word matches are:\n' + show_possible_matches(get_guessed_word(secret_word, guessedLetters)))
            show_turns()
        elif guess == '*' and usedHint:
            print('Sorry, you used your hint already.')
            show_turns()
        elif str(guess) in guessedLetters:
            if warnings > 0:
                warnings -= 1
            else:
                guessesLeft -= 1
            print(
                'Oops! You already guessed that letter. You have ' + str(
                    warnings) + '  warnings left: ' + get_guessed_word(
                    secret_word, guessedLetters))
            show_turns()
        elif secret_word.find(guess) >= 0:
            guessedLetters.append(guess)
            print('Good guess: ' + get_guessed_word(secret_word, guessedLetters))
            show_turns()
            playerWins = is_word_guessed(secret_word, guessedLetters)
        elif len(guess) != 1 or not guess.isalpha():
            if warnings > 0:
                warnings -= 1
                print('Oops! That is not a valid letter. You have ' + str(
                    warnings) + '  warnings left: ' + get_guessed_word(secret_word, guessedLetters))
            else:
                guessesLeft -= 1
                print(
                    'Oops! That is not a valid letter. You have no warnings left, so you lose a guess: ' + get_guessed_word(
                        secret_word, guessedLetters))
            show_turns()
        else:
            guessedLetters.append(guess)
            if str(guess) in vowels and guessesLeft >= 2:
                guessesLeft -= 2
            else:
                guessesLeft -= 1
            print('Oops, that letter isn\'t correct: ' + get_guessed_word(secret_word, guessedLetters))
            show_turns()
        print('----------')

    if playerWins:
        print('Congratulations, you won!\nYour total score is: ' + str(guessesLeft * len(secret_word)))
    elif guessesLeft <= 0:
        print('Sorry, you\'re all out of guesses. The word was "' + secret_word + '".')



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
