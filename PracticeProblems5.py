from idlelib.editor import darwin

print("-------------------------")
print("Problem 1")
print("-------------------------")

def getArea(length, width):
    return length * width

length = 12
width = 5

area = getArea(length, width)
print(length, "*", width, "=", area)

print("-------------------------")
print("Problem 2")
print("-------------------------")

def hungryCat(hunger):
    for num in range(hunger):
        print("meow")

hungryCat(10)

print("-------------------------")
print("Problem 4")
print("-------------------------")

def getSandwich(bread, toppings):
    pass

print("-------------------------")
print("Problem 5")
print("-------------------------")

def whatDoesTheFoxSay():
    return "A ring-ding-ding"

print(whatDoesTheFoxSay())

print("-------------------------")
print("Problem 6")
print("-------------------------")

def getAlphabet():
    return [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

def getIndex(letter):
    alphabet = getAlphabet()
    return alphabet.index(letter)

def shiftLetter(letter, shift):
    alphabet = getAlphabet()
    return alphabet[(getIndex(letter) + shift) % 26]

def encrypt(message, shift):
    alphabet = getAlphabet()
    ciphertext = ''
    for char in str(message).lower():
        if char in alphabet:
            ciphertext += shiftLetter(char, shift)
        else:
            ciphertext += char
    return ciphertext

message = "Hello World!"
shift = 7

print(encrypt(message, shift))


print("-------------------------")
print("Problem 7")
print("-------------------------")

def printRock():
    pass

def printPaper():
    pass

def printScissors():
    pass

def player():
    choice = input("Pick rock, paper, or scissors.").lower()

    while choice.lower() not in ['rock', 'paper', 'scissors']:
        print("Invalid response.")
        choice = input("Pick rock, paper, or scissors.").lower()

    print("Player chose", choice.upper())
    if choice is 'rock':
        printRock()
    elif choice is 'paper':
        printPaper()
    elif choice is 'scissors':
        printScissors()

    return choice

def computer():
    import random
    choice = random.choice(['rock', 'paper', 'scissors'])

    print("Computer chose", choice.upper())
    if choice is 'rock':
        printRock()
    elif choice is 'paper':
        printPaper()
    elif choice is 'scissors':
        printScissors()

    return choice

def winnerLogic(playerChoice, computerChoice):
    if playerChoice is 'rock' and computerChoice is 'rock':
        return 'draw'
    if playerChoice is 'paper' and computerChoice is 'paper':
        return 'draw'
    if playerChoice is 'scissors' and computerChoice is 'scissors':
        return 'draw'
    if playerChoice is 'rock' and computerChoice is 'paper':
        return 'computer_win'
    if playerChoice is 'rock' and computerChoice is 'scissors':
        return 'player_win'
    if playerChoice is 'paper' and computerChoice is 'rock':
        return 'player_win'
    if playerChoice is 'paper' and computerChoice is 'scissors':
        return 'computer_win'
    if playerChoice is 'scissors' and computerChoice is 'rock':
        return 'computer_win'
    if playerChoice is 'scissors' and computerChoice is 'paper':
        return 'player_win'

def playGame():
    result = 'draw'

    while result is 'draw':
        playerChoice = player()
        computerChoice = computer()

        result = winnerLogic(playerChoice, computerChoice)






















