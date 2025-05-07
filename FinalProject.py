from random import shuffle



def initializePuzzle():
    names = ['Mario', 'Luigi', 'Bowser', 'Peach', 'Toad']
    colors = ['red', 'green', 'black', 'pink', 'yellow']
    cities = ['Mushroom Kingdom', 'Bowser\'s Kingdom', 'New Donk City', 'Yoshi Valley', 'Space' ]
    drinks = ['water', 'coffee', 'tea', 'soda', 'beer']
    heirlooms = ['Super Mushroom', 'Fire Flower', 'Super Star', 'POW Block', 'Coin']

    shuffle(names)
    shuffle(colors)
    shuffle(cities)
    shuffle(drinks)
    shuffle(heirlooms)

    return [names, colors, cities, drinks, heirlooms]



def printStory(names, colors, cities, drinks, heirlooms):
    print(f"""
            At the dinner party were Mario, Luigi, Bowser, Princess Peach, and Toad.
            
            The guests sat in a row. They all wore different colors and {names[0]} wore a jaunty {colors[0]} hat. {names[1]}
            was at the far left, next to the guest wearing a {colors[1]} jacket. The guest in {colors[2]} sat left of someone in {colors[3]}. I
            remember that {colors[2]} outfit because the guest spilled their {drinks[0]} all over it. The traveler from {cities[0]} was
            dressed entirely in {colors[4]}. When one of the dinner guests bragged about their {heirlooms[0]}, the person next to them
            said they were finer in {cities[0]}, where they lived.

            So {names[2]} showed off a prized {heirlooms[1]}, at which the guest from {cities[1]} scoffed, saying it was no match for
            their {heirlooms[2]}. Someone else carried a valuable {heirlooms[3]} and when they saw it, the visitor from {cities[2]} next to
            them almost spilled their neighbor's {drinks[1]}. {names[3]} raised their {drinks[2]} in toast. The guest from {cities[3]}, full of
            {drinks[3]}, jumped up onto the table falling onto the guest in the center seat, spilling the poor person's {drinks[4]}.
            Then {names[4]} captivated them all with a story about their wild youth in {cities[4]}.

            In the morning there were four heirlooms under the table: {heirlooms[2]}, {heirlooms[3]}, {heirlooms[0]}, and {heirlooms[4]}.

            But who owned each?
        """)

def initializeKnown():
    known = [
        ['?','?','?','?','?'],
        ['?','?','?','?','?'],
        ['?','?','?','?','?'],
        ['?','?','?','?','?'],
        ['?','?','?','?','?']
    ]

    return known

def printKnown(known):
    print(f"""
        +------------------+------------------+------------------+------------------+------------------+------------------+
        | Seating Order -> |        1         |        2         |        3         |        4         |        5         |
        +------------------+------------------+------------------+------------------+------------------+------------------+
        | Name             | {known[0][0]:<17}| {known[0][1]:<17}| {known[0][2]:<17}| {known[0][3]:<17}| {known[0][4]:<17}|
        | Color            | {known[1][0]:<17}| {known[1][1]:<17}| {known[1][2]:<17}| {known[1][3]:<17}| {known[1][4]:<17}|
        | Drink            | {known[2][0]:<17}| {known[2][1]:<17}| {known[2][2]:<17}| {known[2][3]:<17}| {known[2][4]:<17}|
        | City             | {known[3][0]:<17}| {known[3][1]:<17}| {known[3][2]:<17}| {known[3][3]:<17}| {known[3][4]:<17}|
        | Heirloom         | {known[4][0]:<17}| {known[4][1]:<17}| {known[4][2]:<17}| {known[4][3]:<17}| {known[4][4]:<17}|
        +------------------+------------------+------------------+------------------+------------------+------------------+
        """)


def updateKnown(known):
    print("""Enter your guess in the format of: '(number/position) (is/wears/drinks/is from/has) (name/color/drink/city/heirloom)' 
                For example: '2 wears red' , 'center is from Mushroom Kingdom' , etc.
                Note: Acceptable positions include: far left, center, far right. To make a guess for the 2nd and 4th position, use 2 or 4.""")


    valid = False

    while not valid:
        column = -1
        row = -1
        value = ''

        guess = input("Enter your guess: ").lower()
        firstWord = guess.split()[0]
        twoWords = False

        if firstWord == 'far':
            twoWords = True
            if guess.split()[1] == 'left':
                column = 0
            elif guess.split()[1] == 'right':
                column = 4
            else:
                print("Invalid response format.")
                continue
        elif firstWord == 'center' or firstWord == '3':
            column = 2
        elif firstWord == '1':
            column = 0
        elif firstWord == '2':
            column = 1
        elif firstWord == '4':
            column = 3
        elif firstWord == '5':
            column = 4
        else:
            print("Invalid position.")
            continue

        words = guess.split()
        if twoWords:
            guess2 = " ".join(words[2:])
        else:
            guess2 = " ".join(words[1:])

        twoWords = False

        firstWord = guess2.split()[0]

        if firstWord == 'is':
            if guess2.split()[1] == 'from':
                twoWords = True
                row = 3
            else:
                row = 0
        elif firstWord == 'wears':
            row = 1
        elif firstWord == 'drinks':
            row = 2
        elif firstWord == 'has':
            row = 4
        else:
            print("Invalid verb.")
            continue

        words = guess2.split()
        if twoWords:
            guess3 = " ".join(words[2:])
        else:
            guess3 = " ".join(words[1:])

        value = guess3
        valid = True

    known[row][column] = value

    return known


def checkSolved(known, correctOrder):
    for i in range(5):
        if known[4][i] != correctOrder[i]:
            return False

    return True

def solveRiddle():


    known = initializeKnown()
    info = initializePuzzle()
    names = info[0]
    colors = info[1]
    cities = info[2]
    drinks = info[3]
    heirlooms = info[4]

    correctOrder = [heirlooms[3].lower(), heirlooms[0].lower(), heirlooms[2].lower(), heirlooms[4].lower(),
                    heirlooms[1].lower()]



    while not checkSolved(known, correctOrder):
        printStory(names, colors, cities, drinks, heirlooms)
        printKnown(known)
        known = updateKnown(known)


    printKnown(known)
    print("You solved it! Congratulations!")


solveRiddle()















