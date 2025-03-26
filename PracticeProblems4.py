import random


# print("-----------------------------")
# print("Problem 3")
# print("-----------------------------")
#
#
# ans = input("Would you like fries with that? ")
# if ans.lower() != "yes":
#     print("I thought so.")
# while ans.lower() != "yes":
#     ans = input("Would you like fries with that? ")
#
# print("-----------------------------")
# print("Problem 5")
# print("-----------------------------")
#
# deck = ["2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH",
#         "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD",
#         "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS",
#         "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC"
#         ]
#
# hand = [random.choice(deck)]
# ans = "yes"
#
# while ans.lower() == "yes":
#     hand.append(random.choice(deck))
#     print(hand)
#     ans = input("Would you like another card?")

# print("-----------------------------")
# print("Problem 6")
# print("-----------------------------")
#
#
#
#
# print("You find yourself in an eerie forest...")
# print()
# print("    |   |    ")
# print("    |   |    ")
# print("____|   |____") # ↑
# print("      ?      ") # ↓
# print("____     ____") # ←
# print("    |   |    ") # →
# print("    |   |    ")
# print("    |   |    ")
#
# direction = input("What direction would you like to go? (north, east, south, or west?)") #correct sequence - N E S E
# first = False
# second = False
# third = False
# fourth = False
#
# while not fourth:
#     if direction.lower() == "north":
#         print("You find yourself in the same forest...")
#         print()
#         print("    |   |    ")
#         print("    |   |    ")
#         print("____|   |____")  # ↑
#         print("      ↑      ")  # ↓
#         print("____     ____")  # ←
#         print("    |   |    ")  # →
#         print("    |   |    ")
#         print("    |   |    ")
#
#         if not first:
#             first = True
#         else:
#             first = False
#
#         direction = input(
#             "What direction would you like to go? (north, east, south, or west?)")  # correct sequence - N E S E
#
#     elif direction.lower() == "south":
#         print("You find yourself in the same forest...")
#         print()
#         print("    |   |    ")
#         print("    |   |    ")
#         print("____|   |____")  # ↑
#         print("      ↓      ")  # ↓
#         print("____     ____")  # ←
#         print("    |   |    ")  # →
#         print("    |   |    ")
#         print("    |   |    ")
#
#         if first and second and not third:
#             third = True
#         else:
#             third = False
#             second = False
#             first = False
#
#         direction = input(
#             "What direction would you like to go? (north, east, south, or west?)")  # correct sequence - N E S E
#
#     elif direction.lower() == "east":
#         print("You find yourself in the same forest...")
#         print()
#         print("    |   |    ")
#         print("    |   |    ")
#         print("____|   |____")  # ↑
#         print("      →      ")  # ↓
#         print("____     ____")  # ←
#         print("    |   |    ")  # →
#         print("    |   |    ")
#         print("    |   |    ")
#
#         if first and not second:
#             second = True
#         elif first and second and third:
#             fourth = True
#             break
#         else:
#             third = False
#             second = False
#             first = False
#
#         direction = input(
#             "What direction would you like to go? (north, east, south, or west?)")  # correct sequence - N E S E
#
#     elif direction.lower() == "west":
#         print("You find yourself in the same forest...")
#         print()
#         print("    |   |    ")
#         print("    |   |    ")
#         print("____|   |____")  # ↑
#         print("      ←      ")  # ↓
#         print("____     ____")  # ←
#         print("    |   |    ")  # →
#         print("    |   |    ")
#         print("    |   |    ")
#
#         first = False
#         second = False
#         third = False
#
#         direction = input(
#             "What direction would you like to go? (north, east, south, or west?)")  # correct sequence - N E S E
#
#
# print("You made it out of the forest! Congratulations!")

# print("-----------------------------")
# print("Problem 7")
# print("-----------------------------")
#
# ans = input("Hello? ")
# num = 0
#
# while ans.lower() != "is this patrick?":
#     if ans.lower() == "is this the krusty krab?":
#         if num >= 3:
#             print("NO THIS IS PATRICK" + ("!" * num))
#         else:
#             print("No this is Patrick" + ("!" * num))
#         num += 1
#         ans = input("Hello? ")
#     else:
#         ans = input("I'm sorry, I didn't hear you... Could you repeat that? ")

# print("Yes, this is Patrick.")

# print("-----------------------------")
# print("Problem 8")
# print("-----------------------------")
#
# num = random.randint(1,100)
# ans = int(input("Guess the number: "))
# correct = False
#
# while not correct:
#     if num == ans:
#         print("That's correct! Congratulations!")
#         correct = True
#     elif max(num, ans) - min(num, ans) >= 25:
#         print("Cold")
#         ans = int(input("Guess again: "))
#     elif max(num, ans) - min(num, ans) >= 15:
#         print("Cool")
#         ans = int(input("Guess again: "))
#     elif max(num, ans) - min(num, ans) >= 5:
#         print("Warm")
#         ans = int(input("Guess again: "))
#     elif max(num, ans) - min(num, ans) > 0:
#         print("Hot")
#         ans = int(input("Guess again: "))

# print("-----------------------------")
# print("Problem 9")                            NEEDS FINISHED
# print("-----------------------------")
#
# num = int(input("How many numbers are in your safe combination?"))
# combination = []
# attempt = []
# i = 0
# j = 0
#
# for num in range(0, num):
#     combination.append(random.randint(0,99))
#
# for i in combination:
#     while j != combination[i]:
#         j += 1
#
#     attempt.append(j)
#
# print("Safe combination:", combination)
# print("Combination we found:", attempt)


print("-----------------------------")
print("Problem 10")
print("-----------------------------")

print("Pattern 1")
for i in range(5,0,-1):
    print("#" * i)
print()

print("Pattern 2")
for i in range(1,6):
    print("#" * i)
print()

print("Pattern 3")
for i in range(5,0,-1):
    print(" " * (i - 1), "#" * (i - (5 - i)))

























