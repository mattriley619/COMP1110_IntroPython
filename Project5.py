
print("=================================================")
print("Problem 1")
print("=================================================")

letterPairs = {}

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

shift = input("Enter a value to shift by: ")

for letter in alphabet:
    letterPairs[alphabet[letter]] = alphabet[(letter + shift) % 26]

plaintext = input("Enter your message: ")

ciphertext = ''

for char in plaintext:
    if char in alphabet:
        ciphertext = ciphertext + letterPairs[char]
    else:
        ciphertext = ciphertext + char

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)






