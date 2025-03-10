#------------------------------------
#Problem 1
#------------------------------------

fruit = ["**apple**", "!g!r!a!p!e!", "egnaro", "yyyrrrrrreeehhhccc"]

slicedFruit = []

slicedFruit.append(fruit[0][2:7])
slicedFruit.append(fruit[1][1::2])
slicedFruit.append(fruit[2][::-1])
slicedFruit.append(fruit[3][::-3])

print(slicedFruit)

#------------------------------------
#Problem 2
#------------------------------------

name = "Lee Harvey Oswald"
split = name.split()

username = (split[0][0] + split[1][0] + split[2][0] +
            str(len(split[0])) + str(len(split[1])) + str(len(split[2])))

password = (split[0][-1].lower() + split[0][-2].upper() + str(abs(len(split[0]) - len(split[1]))) +
            split[1][-1].lower() + split[1][-2].upper() + str(abs(len(split[1]) - len(split[2]))) +
            split[2][-1].lower() + split[2][-2].upper())

print(username)
print(password)


#------------------------------------
#Problem 3
#------------------------------------

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

print(f'----------Bikini Bottom----------')
print(f'--------Driver\'s License----------')













