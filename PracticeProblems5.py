
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
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

def printPaper():
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

def printScissors():
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

def player():
    choice = input("Pick rock, paper, or scissors.").lower()

    while choice.lower() not in ['rock', 'paper', 'scissors']:
        print("Invalid response.")
        choice = input("Pick rock, paper, or scissors.").lower()

    print("Player chose", choice.upper())
    if choice == 'rock':
        printRock()
    elif choice == 'paper':
        printPaper()
    elif choice == 'scissors':
        printScissors()

    return choice

def computer():
    import random
    choice = random.choice(['rock', 'paper', 'scissors'])

    print("Computer chose", choice.upper())
    if choice == 'rock':
        printRock()
    elif choice == 'paper':
        printPaper()
    elif choice == 'scissors':
        printScissors()

    return choice

def winnerLogic(playerChoice, computerChoice):
    if playerChoice == 'rock' and computerChoice == 'rock':
        return 'draw'
    if playerChoice == 'paper' and computerChoice == 'paper':
        return 'draw'
    if playerChoice == 'scissors' and computerChoice == 'scissors':
        return 'draw'
    if playerChoice == 'rock' and computerChoice == 'paper':
        return 'computer_win'
    if playerChoice == 'rock' and computerChoice == 'scissors':
        return 'player_win'
    if playerChoice == 'paper' and computerChoice == 'rock':
        return 'player_win'
    if playerChoice == 'paper' and computerChoice == 'scissors':
        return 'computer_win'
    if playerChoice == 'scissors' and computerChoice == 'rock':
        return 'computer_win'
    if playerChoice == 'scissors' and computerChoice == 'paper':
        return 'player_win'

def playGame():
    result = 'draw'

    while result == 'draw':
        playerChoice = player()
        computerChoice = computer()

        result = winnerLogic(playerChoice, computerChoice)

    if result == 'computer_win':
        print("You lost, better luck next time.")
    if result == 'player_win':
        print("You won! Congratulations!")

playGame()


print("-------------------------")
print("Problem 8")
print("-------------------------")

def printDoors(state):
    if state == 'all_closed':
        print("""
        +------+  +------+  +------+
        |      |  |      |  |      |
        |   1  |  |   2  |  |   3  |
        |      |  |      |  |      |
        |      |  |      |  |      |
        |      |  |      |  |      |
        +------+  +------+  +------+
        """)
    if state == 'first_goat':
        print("""
        +------+  +------+  +------+
        |  ((  |  |      |  |      |
        |  oo  |  |   2  |  |   3  |
        | /_/|_|  |      |  |      |
        |    | |  |      |  |      |
        |GOAT|||  |      |  |      |
        +------+  +------+  +------+
        """)
    if state == 'second_goat':
        print("""
        +------+  +------+  +------+
        |      |  |  ((  |  |      |
        |   1  |  |  oo  |  |   3  |
        |      |  | /_/|_|  |      |
        |      |  |    | |  |      |
        |      |  |GOAT|||  |      |
        +------+  +------+  +------+
        """)
    if state == 'third_goat':
        print("""
        +------+  +------+  +------+
        |      |  |      |  |  ((  |
        |   1  |  |   2  |  |  oo  |
        |      |  |      |  | /_/|_|
        |      |  |      |  |    | |
        |      |  |      |  |GOAT|||
        +------+  +------+  +------+
        """)
    if state == 'first_car':
        print("""
        +------+  +------+  +------+
        | CAR! |  |  ((  |  |  ((  |
        |    __|  |  oo  |  |  oo  |
        |  _/  |  | /_/|_|  | /_/|_|
        | /_ __|  |    | |  |    | |
        |   O  |  |GOAT|||  |GOAT|||
        +------+  +------+  +------+
        """)
    if state == 'second_car':
        print("""
        +------+  +------+  +------+
        |  ((  |  | CAR! |  |  ((  |
        |  oo  |  |    __|  |  oo  |
        | /_/|_|  |  _/  |  | /_/|_|
        |    | |  | /_ __|  |    | |
        |GOAT|||  |   O  |  |GOAT|||
        +------+  +------+  +------+
        """)
    if state == 'third_car':
        print("""
        +------+  +------+  +------+
        |  ((  |  |  ((  |  | CAR! |
        |  oo  |  |  oo  |  |    __|
        | /_/|_|  | /_/|_|  |  _/  |
        |    | |  |    | |  | /_ __|
        |GOAT|||  |GOAT|||  |   O  |
        +------+  +------+  +------+
        """)

def setDoors():
    from random import randint, choice

    doorWithCar = randint(1,3)
    if doorWithCar == 1:
        doorWithGoat1 = 2
        doorWithGoat2 = 3
    if doorWithCar == 2:
        doorWithGoat1 = 1
        doorWithGoat2 = 3
    if doorWithCar == 3:
        doorWithGoat1 = 1
        doorWithGoat2 = 2

    goats = [doorWithGoat1, doorWithGoat2]
    doorRevealed = choice(goats)

    return [doorWithCar, doorWithGoat1, doorWithGoat2, doorRevealed]

def player():
    ans = int(input("Pick a door. (1-3): "))

    while ans not in (1,2,3):
        print("Invalid response.")
        ans = input("Pick a door. (1-3): ")

    return ans

def doSwap(doorPicked, doorRevealed):
    ans = input("Would you like to swap doors? ").lower()

    while ans not in ('yes', 'no', 'y', 'n'):
        print("Invalid response.")
        ans = input("Would you like to swap doors? ")

    if ans in ('yes', 'y'):
        for door in (1,2,3):
            if door != doorPicked and door != doorRevealed:
                doorPicked = door
                break

    return doorPicked

def playGame():
    print("Welcome to the door game! Behind one of these three doors is a brand new car! Behind the other two doors are goats. ")
    print("Once you pick a door, I will open up a door with a goat behind it. You will then be given the option to swap doors. Now let's begin!")

    printDoors('all_closed')
    doors = setDoors()

    doorPicked = player()

    print("You picked door", doorPicked)

    if doors[3] == doorPicked: #if the pre-picked door to reveal is the one the player chose
        if doors[1] == doorPicked:
            doors[3] = doors[2]
        elif doors[2] == doorPicked:
            doors[3] = doors[1]

    if doors[3] == 1:
        state = 'first_goat'
    elif doors[3] == 2:
        state = 'second_goat'
    elif doors[3] == 3:
        state = 'third_goat'

    print("Now I will pick a door to reveal.")
    printDoors(state)

    doorPicked = doSwap(doorPicked, doors[3])
    print("Your door is", doorPicked)

    if doors[0] == 1:
        state = 'first_car'
    elif doors[0] == 2:
        state = 'second_car'
    elif doors[0] == 3:
        state = 'third_car'

    print("Time to reveal all the doors.")
    printDoors(state)

    if doorPicked == doors[0]:
        print("Congratulations! You won a brand new car.")
    else:
        print("Sorry, better luck next time.")


playGame()

print("-------------------------")
print("Problem 9")
print("-------------------------")

def initialize():
    from random import randint, choice

    doorWithCar = randint(1, 3)
    if doorWithCar == 1:
        doorWithGoat1 = 2
        doorWithGoat2 = 3
    if doorWithCar == 2:
        doorWithGoat1 = 1
        doorWithGoat2 = 3
    if doorWithCar == 3:
        doorWithGoat1 = 1
        doorWithGoat2 = 2

    goats = [doorWithGoat1, doorWithGoat2]
    doorRevealed = choice(goats)

    doorPicked = randint(1,3)

    return [doorWithCar, doorWithGoat1, doorWithGoat2, doorRevealed, doorPicked]


def alwaysSwap(doorPicked, doorRevealed):

    for door in (1, 2, 3):
        if door != doorPicked and door != doorRevealed:
           doorPicked = door
           break

    return doorPicked




def simulateGames(num):
    wins = 0

    for simulations in range(num):
        doors = initialize()
        doorPicked = alwaysSwap(doors[4], doors[3])

        if doors[3] == doorPicked:  # if the pre-picked door to reveal is the one chosen
            if doors[1] == doorPicked:
                doors[3] = doors[2]
            elif doors[2] == doorPicked:
                doors[3] = doors[1]

        if doorPicked == doors[0]:
            wins += 1

    winPercentage = (wins / num) * 100

    print(f"You played {num} games always swapping and you won {wins} times. That's a win percentage of {winPercentage}%!")

    wins = 0

    for simulations in range(num):
        doors = initialize()
        doorPicked = doors[4]

        if doors[3] == doorPicked:  # if the pre-picked door to reveal is the one chosen
            if doors[1] == doorPicked:
                doors[3] = doors[2]
            elif doors[2] == doorPicked:
                doors[3] = doors[1]

        if doorPicked == doors[0]:
            wins += 1

    winPercentage = (wins / num) * 100

    print(
        f"You played {num} games never swapping and you won {wins} times. That's a win percentage of {winPercentage}%!")


simulateGames(1000)