import random

#----------------------------------------------------------------------------------------
print("---------")
print("Problem 1: Improved Quadratic Formula")
print("---------")
#-----------------------------------------------------------------------------------------

a = float(input("Enter a value for a: "))
b = float(input("Enter a value for b: "))
c = float(input("Enter a value for c: "))

disc = float(b * b - 4 * a * c)

x = (-b + ((b * b - 4 * a * c)**(1/2)))/(2 * a)
y = (-b - ((b * b - 4 * a * c)**(1/2)))/(2 * a)

if disc < 0:
    print("The equation has no real solutions.")
    print(f'The imaginary solution is x = {x}, y = {y}, for the equation ax^2 + bx + c = 0')
elif disc == 0:
    print("The equation has the same 2 solutions.")
    print(f'The solution is x = {x}, y = {y}, for the equation ax^2 + bx + c = 0')
else:
    print(f'The solution is x = {x}, y = {y}, for the equation ax^2 + bx + c = 0')

#----------------------------------------------------------------------------------------
print("---------")
print("Problem 2: Lunch")
print("---------")
#-----------------------------------------------------------------------------------------

vegan = False
lactose = False
gluten = False

vRest = "Vegans Only"
lRest = "Burger Central"
gRest = "Milk HQ"
vlRest = "Bland Buffet"
vgRest = "Big Jim's"
lgRest = "EGG®"
allRest = "Salad Bowl"
noneRest = "Meat, Milk, and Bread (MMB)"

ans = input("Are you vegan?")
if ans.lower() == "yes":
    vegan = True

ans = input("Are you lactose intolerant?")
if ans.lower() == "yes":
    lactose = True

ans = input("Are you gluten intolerant?")
if ans.lower() == "yes":
    gluten = True

if vegan and lactose and gluten: #vlg
    print(allRest, sep='\n')
if vegan and lactose and not gluten: #vl
    print(allRest, vlRest, sep='\n')
if vegan and not lactose and gluten: #vg
    print(allRest, vgRest, sep='\n')
if vegan and not lactose and not gluten: #v
    print(allRest, vRest, vlRest, vgRest, sep='\n')
if not vegan and lactose and gluten: #lg
    print(allRest, lgRest, sep='\n')
if not vegan and lactose and not gluten: #l
    print(allRest, lRest, lgRest, vlRest, sep='\n')
if not vegan and not lactose and gluten: # g
    print(allRest, gRest, lgRest, vgRest, sep='\n')
if not vegan and not lactose and not gluten: #
    print(allRest, vlRest, vgRest, lgRest, vRest, lRest, gRest, noneRest, sep='\n')


#----------------------------------------------------------------------------------------
print("---------")
print("Problem 3: Ouija Board")
print("---------")
#-----------------------------------------------------------------------------------------

question = input("Ask the spirits a question: ")
num = random.randint(0, 9)
answers = ["yes", "no", "maybe", "perhaps", "probably not",
           "absolutely", "of course not", "I don't know", "stop asking me questions"]

print("You asked:", question, "and the spirits answer:", answers[num], sep='\n')




