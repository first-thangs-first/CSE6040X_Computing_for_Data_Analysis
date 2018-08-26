import hanglib.draw as draw
from hanglib import words
from random import choice


def drawBlank(randomWord):
    for c in range(len(randomWord)):
        print("_", end=' ')


def ishangmanComplete(numOfGuesses):
    """Determine if drawing of hangman is complete.

    Parameters:
    numberOfGuesses: int -- number of guesses player has made

    Return:
    bool: True if its 6 or more guesses

    Usage examples:
    >>> ishangmanComplete(1)
    False
    >>> ishangmanComplete(6)
    True
    """
    return numOfGuesses >= 6


def didUserGuessed(randomWord, guesses):
    """Determined if user correctly guessed the word

    Parameters:
    randomWord: str -- the word player is trying to guess
    guesses: list -- the letters player has guessed so far

    Return:
    bool: True if all the unique letters in randomWord is in guesses

    Usage examples:
    >>> didUserGuessed('cat', [])
    False
    >>> didUserGuessed('cat', ['a','t','c'])
    True
    """
    a = set(randomWord)
    b = set(guesses)
    return len(a - b) == 0


def guess_is_a_number(guess):
    """Determine if guess is a number

    Parameters:
    guess: str

    Return:
    bool: True if guess can be casted into int

    Usage examples:
    >>> guess_is_a_number('0')
    True
    >>> guess_is_a_number('t')
    False
    """
    try:
        int(guess)
        return True
    except ValueError:
        return False


def repeated_guess(guess, guesses):
    """Determine if guess is already in guesses

    Parameters:
    guess: str -- current guess
    guesses: list -- list of previous guesses

    Return:
    bool: True if guess is in list of guesses

    Usage examples:
    >>> repeated_guess('a', [])
    False
    >>> repeated_guess('b', ['a','b'])
    True
    """
    return guess in guesses


def prompt(message, guesses):
    """Keep prompting user until proper letter is entered
    """
    guess = input(message)
    while(guess_is_a_number(guess) or repeated_guess(guess, guesses)):
        guess = input(message)
    return guess


def guess_is_good(playersGuess, randomWord):
    """Determine if player's guess is in word

    Parameters:
    playersGuess: str -- player's guess
    randomWord: str -- word player is trying to guess

    Return:
    bool -- True if playersGuess is in randomWord

    Usage examples:
    >>> guess_is_good('a', 'apple')
    True
    >>> guess_is_good('a', 'book')
    False
    """
    return (playersGuess in randomWord)


def drawBoard(randomWord, guesses):
    """Draw the board, _ for letters in word not in guess, the character otherwise [_A_]
    """
    for c in list(randomWord):
        if (c in guesses):
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()


def drawNext(numOfGuesses):
    """Draw the next handman frame
    """
    options = {
        0: draw.stand,
        1: draw.head,
        2: draw.body,
        3: draw.leftarm,
        4: draw.rightarm,
        5: draw.leftleg,
        6: draw.rightleg
    }
    options[numOfGuesses + 1]()


def playHangman(randomWord, guesses, numOfGuesses):
    while((not ishangmanComplete(numOfGuesses)) and not didUserGuessed(randomWord, guesses)):
        print()
        playersGuess = prompt("Guess a letter: ", guesses)
        guesses.append(playersGuess)
        if guess_is_good(playersGuess, randomWord):
            drawBoard(randomWord, guesses)
        else:
            drawNext(numOfGuesses)
            numOfGuesses = numOfGuesses + 1
    input("Enter any key to exit: ")


def main():
    difficulty = input("What kind of words would you like to guess: ")
    randomWord = choice(words.category[difficulty])
    drawBlank(randomWord)
    draw.stand()
    print(randomWord)
    playHangman(randomWord, [], 0)

if __name__ == "__main__":
    main()