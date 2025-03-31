from random import randint


print("----------------------------------")
print("Problem 1")
print("----------------------------------")

die = {

    'one' : """
               ┍━━━━━━━━┑
               │        │
               │    @   │
               │        │
               ┕━━━━━━━━┙
                        """,

    'two' : """
               ┍━━━━━━━━┑
               │      @ │
               │        │
               │  @     │
               ┕━━━━━━━━┙
                        """,

    'three' : """
               ┍━━━━━━━━┑
               │      @ │
               │    @   │
               │  @     │
               ┕━━━━━━━━┙
                        """,

    'four' : """
               ┍━━━━━━━━┑
               │ @    @ │
               │        │
               │ @    @ │
               ┕━━━━━━━━┙
                        """,

    'five' : """
               ┍━━━━━━━━┑
               │ @    @ │
               │    @   │
               │ @    @ │
               ┕━━━━━━━━┙
                        """,

    'six' : """
               ┍━━━━━━━━┑
               │ @    @ │
               │ @    @ │
               │ @    @ │
               ┕━━━━━━━━┙
                        """,

    'ques1' : "How many polar bears are there?",
    'ans1' : "",

    'ques2' : "How many fish are there?",
    'ans2' : "",

    'ques3' : "Do the bears catch any fish?",
    'ans3' : ""
}

dieList = [die['one'], die['two'], die['three'], die['four'], die['five'], die['six']]
score = 0

for i in range(3):
    print("Polar bears come in pairs to sit and fish through holes in the ice.")
    num = randint(1,6)

    if num == 1:
        die['ans1'] = '0'
        die['ans2'] = '6'
        die['ans3'] = 'no'
    elif num == 2:
        die['ans1'] = '2'
        die['ans2'] = '5'
        die['ans3'] = 'no'
    elif num == 3:
        die['ans1'] = '2'
        die['ans2'] = '4'
        die['ans3'] = 'yes'
    elif num == 4:
        die['ans1'] = '4'
        die['ans2'] = '3'
        die['ans3'] = 'no'
    elif num == 5:
        die['ans1'] = '4'
        die['ans2'] = '2'
        die['ans3'] = 'yes'
    elif num == 6:
        die['ans1'] = '6'
        die['ans2'] = '1'
        die['ans3'] = 'no'

    print(dieList[num - 1])

    ans = input(die['ques1'])
    if ans == die['ans1']:
        score += 1

    ans = input(die['ques2'])
    if ans == die['ans2']:
        score += 1

    ans = input(die['ques3'])
    if ans == die['ans3']:
        score += 1

print("Your score:", score)


print("----------------------------------")
print("Problem 2")
print("----------------------------------")

speech = """

Miranda Priestly: Where are the belts for this dress? Why is no one ready?
Jocelyn: Here. It’s a tough call. They’re so different.
Andy Sachs: (snickers under her breath)
Miranda Priestly: Something funny?
Andy Sachs: No. No, no, nothing’s… you know, it’s just that… both those stupid
belts look exactly the same to me. Y’know, I’m still learning about this gosh darn
stuff, and uh… shoot
Miranda Priestly: This… “stuff”? Oh, okay. I see. You think this has nothing to do
with you.
You… go to your gosh darn closet, and you select… I don’t know, that stupid
lumpy blue sweater, for instance, because you’re trying to tell the world that you
take yourself too gosh darn seriously to care about what you put on your back, but
what you don’t know is that that sweater is not just blue, it’s not turquoise, it’s not
lapis, it’s actually cerulean.
You’re also blithely unaware of the fact that, in 2002, Oscar de la Renta did a
collection of cerulean gowns, and then I think it was Yves Saint Laurent, wasn’t
it?… who showed cerulean military jackets. Heck I think we need a jacket here.
Nigel: Hmm.
Miranda Priestly: And then gosh darn cerulean quickly showed up in the
collections of eight different designers. Shoot Then it filtered down through the
department stores and then trickled on down into some tragic casual corner where
you, no doubt, fished it out of some stupid clearance bin.
However, that blue represents millions of gosh darn dollars of countless gosh darn
jobs, and it’s sort of comical how you think that you’ve made a choice that
exempts you from the fashion industry when, in fact, you’re wearing a sweater that
was selected for you by the people in this room… from a pile of “stupid stuff.”"""

index = 0
while index != -1:
    index = speech.find("heck")
    if index != -1:
        speech = speech.replace("heck", "")
    index = speech.find("Heck")
    if index != -1:
        speech = speech.replace("Heck", "")
    index = speech.find("stupid")
    if index != -1:
        speech = speech.replace("stupid", "")
    index = speech.find("Stupid")
    if index != -1:
        speech = speech.replace("Stupid", "")
    index = speech.find("gosh darn")
    if index != -1:
        speech = speech.replace("gosh darn", "")
    index = speech.find("Gosh darn")
    if index != -1:
        speech = speech.replace("Gosh darn", "")
    index = speech.find("shoot")
    if index != -1:
        speech = speech.replace("shoot", "")
    index = speech.find("Shoot")
    if index != -1:
        speech = speech.replace("Shoot", "")





print(speech)

















