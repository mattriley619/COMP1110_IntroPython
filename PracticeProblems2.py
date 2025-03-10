#Problem 1

age = input("Enter your age: ")
age = int(age)

if age < 0:
    print("Invalid age")
elif age < 1:
    print("You are a baby")
elif age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 100:
    print("You are an adult")
else:
    print("That is probably not right.")

#-------------------------------------------------------------------------------------------------------
#Problem 2

answer = input("Do you like pina coladas?")

if answer.lower() == "yes":
    answer = input("Do you like getting caught in the rain?")

    if answer.lower() == "yes":
        answer = input("Are you into yoga?")

        if answer.lower() == "no":
            answer = input("Do you have half a brain?")

            if answer.lower() == "yes":
                print("I'm the love you're looking for.")

            else:
                print("You are not the one.")

        else:
            print("You are not the one.")

    else:
        print("You are not the one.")

else:
    print("You are not the one.")

#----------------------------------------------------------------------
#Problem 3

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("fizzbuzz")
elif number % 3 == 0:
    print("fizz")
elif number % 5 == 0:
    print("buzz")

#--------------------------------------------------------------------------
#Problem 8

number = int(input("Enter a number: "))
if number % 3 == 0:
    print("fizz")
else:
    print("buzz")


#------------------------------------------------------------------------
#Problem 14

winRate = int(input("Enter your win rate as a percentage (without the percent sign): "))

if winRate < 25:
    print("You are fired.")
elif winRate < 50:
    print("You are bad.")
elif winRate < 65:
    print("You are average.")
elif winRate < 80:
    print("You are good.")
else:
    print("You are great.")

#------------------------------------------------------------------------
#Problem 21

answer = input("Do you like chocolate cake? ")
if answer.lower() == "yes":
    print("Me too!")

print("I think I see some on the table over there.")


#------------------------------------------------------------------------
#Problem 22

hero = input("Enter your superhero name: ")
if hero.lower() == "aquaman":
    print("What's your super power, talking to fish?")
else:
    print("It's good to see you", hero.title())

#----------------------------------------------------------------
#Problem 23

number = int(input("Enter a number: "))
if number > 9000:
    print("It is over 9000!!!")







