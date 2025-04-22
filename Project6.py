

def printHangman(incorrectGuesses):


    if incorrectGuesses == 0:
        print('''
              +---+
                  |
                  |
                  |
                  |
                  |
            =========''')
    elif incorrectGuesses == 1:
        print('''
              +---+
              |   |
                  |
                  |
                  |
                  |
            =========''')
    elif incorrectGuesses == 2:
        print('''
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =========''')
    elif incorrectGuesses == 3:
        print('''
              +---+
              |   |
              O   |
              |   |
                  |
                  |
            =========''')
    elif incorrectGuesses == 4:
        print('''
              +---+
              |   |
              O   |
             /|   |
                  |
                  |
            =========''')
    elif incorrectGuesses == 5:
        print('''
              +---+
              |   |
              O   |
             /|\  |
                  |
                  |
            =========''')
    elif incorrectGuesses == 6:
        print('''
              +---+
              |   |
              O   |
             /|\  |
             /    |
                  |
            =========''')
    elif incorrectGuesses == 7:
        print('''
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
            =========''')


def getPhrase():
    from random import choice

    phrases = [
        "hello world",
        "good luck",
        "game over",
        "stay sharp",
        "hang tight",
        "well played",
        "high score",
        "no mercy",
        "try again",
        "level up",
        "take aim",
        "go fast",
        "just chill",
        "play fair",
        "on fire",
        "keep going",
        "final round",
        "great job",
        "watch out",
        "you win"
    ]

    return choice(phrases)


def getGuess(acceptableGuessList):
    guess = input("Enter your guess: ").lower()
    while guess not in acceptableGuessList:
        print("Invalid guess or letter was already used.")
        guess = input("Enter your guess: ").lower()

    return guess

def printPhrase(phrase, guesses):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    phraseToPrint = ""

    for letter in phrase:
        if letter in guesses or letter not in alphabet:
            phraseToPrint += letter
        else:
            phraseToPrint += '_'

    print(phraseToPrint)


def checkWin(phrase, guesses):
    for letter in phrase:
        if letter not in guesses and letter != ' ':
            return False

    return True


def playGame():
    phrase = getPhrase()
    incorrectGuesses = 0
    guesses = []

    acceptableGuessList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    print("Welcome to Hangman!")
    printHangman(incorrectGuesses)
    printPhrase(phrase, guesses)

    while not checkWin(phrase, guesses) and incorrectGuesses < 7:
        guess = getGuess(acceptableGuessList)
        guesses.append(guess)

        if guess not in phrase:
            incorrectGuesses += 1
        else:
            acceptableGuessList.remove(guess)

        printHangman(incorrectGuesses)
        printPhrase(phrase, guesses)


    if checkWin(phrase, guesses):
        print("Congratulations! You win!")
    elif incorrectGuesses == 7:
        print("You lost...")
        print(f"The phrase was '{phrase}'.")


playGame()









