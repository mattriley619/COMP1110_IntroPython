name = "Matt Riley"
major = "Computer Science"
hobby1, hobby2 = "programming", "gaming"

print("---------")
print("Problem 1")
print("---------")

print("Hello, my name is", name, "and my major is", major)

print("Some of my hobbies include " + hobby1, "and " + hobby2)

#====================================================================================

print("---------")
print("Problem 2")
print("---------")

print(1, 2, 3, 4, sep=" Ah, Ah, Ah, ")

#====================================================================================

print("---------")
print("Problem 3")
print("---------")

a = float(input("Enter a value for a: "))
b = float(input("Enter a value for b: "))
c = float(input("Enter a value for c: "))

x = (-b + ((b * b - 4 * a * c)**(1/2)))/(2 * a)
y = (-b - ((b * b - 4 * a * c)**(1/2)))/(2 * a)

print(f'The solution is x = {x}, y = {y}, for the equation ax^2 + bx + c = 0')

#======================================================================================

print("---------")
print("Problem 4")
print("---------")

item1, item2, item3, item4, item5, item6, item7, item8, item9, item10 =\
    "Pizza", "Gold Bar", "Jellyfish", "Boat", "Water", "Shirt", "TV", "Vacuum", "Bag of Rocks", "Mystery Box"

price1, price2, price3, price4, price5, price6, price7, price8, price9, price10 =\
    16.99, 3059.99, 299.99, 1499.99, 1.29, 9.99, 499.99, 99.99, 5.99, 999.99

subtotal = price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8 + price9 + price10
salesTaxRate = .06
salesTaxTotal = subtotal * salesTaxRate
convenienceTaxRate = .05
convenienceTaxTotal = subtotal * convenienceTaxRate
grandTotal = subtotal + convenienceTaxTotal + salesTaxTotal


print("* " * 20)
print("*", " " * 35, "*")
print(f'* {"Welcome To": ^35} *')
print(f'* {"Matt's Various Things": ^35} *')
print("*", " " * 35, "*")
print("*", "-" * 35, "*")
print(f'* {"Itemized Receipt": ^35} *')
print("*", "-" * 35, "*")
print(f'* {item1: <26} {price1: >8} *')
print(f'* {item2: <26} {price2: >8} *')
print(f'* {item3: <26} {price3: >8} *')
print(f'* {item4: <26} {price4: >8} *')
print(f'* {item5: <26} {price5: >8} *')
print(f'* {item6: <26} {price6: >8} *')
print(f'* {item7: <26} {price7: >8} *')
print(f'* {item8: <26} {price8: >8} *')
print(f'* {item9: <26} {price9: >8} *')
print(f'* {item10: <26} {price10: >8} *')
print("*", "-" * 35, "*")
print(f'* {"Subtotal:": <26} {subtotal: >8.2f} *')
print(f'* {"Sales Tax Rate:": <26} {salesTaxRate: >8.3%} *')
print(f'* {"Sales Tax Total:": <26} {salesTaxTotal: >8.2f} *')
print(f'* {"Convenience Tax Rate": <26} {convenienceTaxRate: >8.3%} *')
print(f'* {"Convenience Tax Total:": <26} {convenienceTaxTotal: >8.2f} *')
print(f'* {"Grand Total:": <26} {grandTotal: >8.2f} *')
print("*", "-" * 35, "*")
print("*", " " * 35, "*")
print(f'* {"Thank you for shopping with us!": ^35} *')
print("*", " " * 35, "*")
print("* " * 20)







































