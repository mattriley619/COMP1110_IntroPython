
print("=================================================")
print("Problem 1")
print("=================================================")

letterPairs = {}

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

shift = int(input("Enter a value to shift by: "))

for letter in alphabet:
    originalIndex = alphabet.index(letter)
    shiftIndex = (originalIndex + shift) % 26
    letterPairs[letter] = alphabet[shiftIndex]

plaintext = input("Enter your message: ")

ciphertext = ''

for char in plaintext:
    if char in alphabet:
        ciphertext += letterPairs[char]
    else:
        ciphertext += char

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)



print("=================================================")
print("Problem 2")
print("=================================================")

from random import randint

dice = [4,6,8,10,12,20,100]

for die in dice:
    total = 0
    avg = 0
    for num in range(1,1001):
        total += randint(1, die)
        if num == 10 or num == 100 or num == 1000:
            avg = total / num
            print(f"Average roll for {num}d{die}: {avg}")
    print()





