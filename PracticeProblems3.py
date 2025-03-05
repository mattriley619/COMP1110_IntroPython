print("-----------------------------")
print("Problem 1")
print("-----------------------------")

name = "Matthew Daniel Riley"
initials = name[0] + name[8] + name[15]
first = name[:8]
middle = name[8:15]
last = name[15:]

print(initials)
print(first, middle, last)


print("-----------------------------")
print("Problem 2")
print("-----------------------------")

favoriteThings = ["raindrops on roses", "whiskers on kittens", "bright copper kettles", "warm wool mittens",
                  "brown paper packages tied up with strings", "cream colored ponies", "crisp apple strudels"]

print(favoriteThings[0].upper())
print(favoriteThings[1].lower())
print(favoriteThings[len(favoriteThings)-1])
print(favoriteThings[-1])

favoriteThings.pop()
favoriteThings.append("Comp 1110")
favoriteThings.remove("Comp 1110")
favoriteThings.insert(0, "Comp 1110".title())

print(favoriteThings)


print("-----------------------------")
print("Problem 3")
print("-----------------------------")

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odds = nums[1::2]
countdown = nums[5:0:-1]

print("Odds:", odds)
print("Countdown:", countdown)


print("-----------------------------")
print("Problem 4")
print("-----------------------------")

friends = ["Rachel", "Phoebe", "Chandler", "Ross", "Monica", "Joey"]
print(friends)

friends.remove("Joey")
friends.insert(len(friends) // 2, "Joey")
print(friends)

friends.remove("Rachel")
friends.remove("Monica")
friends.insert(5, "Rachel")
friends.insert(0, "Monica")
print(friends)

friends.remove("Monica")
friends.remove("Phoebe")
friends.remove("Chandler")
friends.insert(1, "Phoebe")
friends.insert(0, "Monica")
friends.insert(0, "Chandler")
print(friends)

friends.insert(2, "Mike")
print(friends)


print("-----------------------------")
print("Problem 5")
print("-----------------------------")

items = ["milk", "bread", "sugar", "chips", "hamburger"]
print(items[2])


print("-----------------------------")
print("Problem 6")
print("-----------------------------")

quote = "War... war never changes"
misquote = quote[:3] + quote[16:]
print(misquote)


print("-----------------------------")
print("Problem 8")
print("-----------------------------")

import random
from random import randint

quote = "Hey, you. You're finally awake."
print(quote[randint(0, len(quote) - 1)])
print(quote[randint(0,len(quote) - 1):randint(0,len(quote) - 1)])


print("-----------------------------")
print("Problem 9")
print("-----------------------------")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

random.shuffle(alphabet)
print(random.choice(alphabet))


print("-----------------------------")
print("Problem 10")
print("-----------------------------")

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

print(list1 + list2)
print(list1 * 3)
#I didn't expect either of these to work. I love this language.

print("-----------------------------")
print("Problem 11")
print("-----------------------------")

games = ["Elden Ring", "Super Mario 3", "Skyrim", "Stardew Valley", "Baldur's Gate 3"]

print(random.choice(games))
print(games[randint(0, len(games) - 1): randint(0, len(games) - 1)])

print("-----------------------------")
print("Problem 13")
print("-----------------------------")

lotteryNumbers = []
lotteryNumbers.append(randint(1, 100))
lotteryNumbers.append(randint(1, 100))
lotteryNumbers.append(randint(1, 100))
lotteryNumbers.append(randint(1, 100))
lotteryNumbers.append(randint(1, 100))
print(lotteryNumbers)






