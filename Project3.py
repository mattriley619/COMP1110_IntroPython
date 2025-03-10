print("------------------------------------------")
print("Problem 1")
print("------------------------------------------")

fruit = ["**apple**", "!g!r!a!p!e!", "egnaro", "yyyrrrrrreeehhhccc"]

slicedFruit = []

slicedFruit.append(fruit[0][2:7])
slicedFruit.append(fruit[1][1::2])
slicedFruit.append(fruit[2][::-1])
slicedFruit.append(fruit[3][::-3])

print(slicedFruit)

print("------------------------------------------")
print("Problem 2")
print("------------------------------------------")

name = "Lee Harvey Oswald"
split = name.split()

username = (split[0][0] + split[1][0] + split[2][0] +
            str(len(split[0])) + str(len(split[1])) + str(len(split[2])))

password = (split[0][-1].lower() + split[0][-2].upper() + str(abs(len(split[0]) - len(split[1]))) +
            split[1][-1].lower() + split[1][-2].upper() + str(abs(len(split[1]) - len(split[2]))) +
            split[2][-1].lower() + split[2][-2].upper())

print(username)
print(password)


print("------------------------------------------")
print("Problem 3")
print("------------------------------------------")

patrick = \
{
    'name' : 'Patrick Star',
    'street' : '120 Conch St.',
    'city' : 'Bikini Bottom',
    'sex' : 'Male',
    'hair' : 'Pink',
    'eyes' : 'Black',
    'height' : '0.06',
    'weight' : '2 oz',
    'expiration' : '12-14-03',
    'number' : 'A1376047',
    'class' : '5'
}
print(f' {"_" *61}')
print(f'| ------------------ {"Bikini Bottom".upper(): ^20} --------------------|')
print(f'|{"Driver License".upper(): >37} {"CLASS: " + patrick["class"]: >22} |')
print(f'|{"EXPIRES: " + patrick["expiration"]: <} {patrick["number"]: ^30} {"|": >13}')
print(f'|___________________ {"|": >42}')
print(f'|        W          |{patrick["name"]: ^20} {"|": >21}')
print(f'|       / \\         |{patrick["street"]: ^21} {"|": >20}')
print(f'|      /   \\        |{patrick["city"]: ^21} {"|": >20}')
print(f'|     / *  *\\       | {"|": >41}')
print(f'|    /  (__) \\      |{"SEX: " + patrick["sex"][0]: >10} {"HAIR: " + patrick["hair"].upper(): >14} {"EYES: " + patrick["eyes"].upper(): >14} |')
print(f'|   /         \\     |{"HT: " + patrick["height"]: >12} {"WT: " + patrick["weight"]: >10} {"|": >18}')
print(f' {"-" *61}')














