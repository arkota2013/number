import math
import random
import string

characters = string.ascii_letters
use_numbers = input("Include numbers? (yes/no): ").lower()
if use_numbers == "yes":
    characters += string.digits
    use_symbols = input("Include symbols? (yes/no): ").lower()
if use_symbols == "yes":
    characters += string.punctuation
while True:
    try:
        length = int(input("How long should your password be? "))
        if length > 0:
            break 
        print("Enter a number greater than 0!")
    except ValueError:
        print("Please enter a whole number!")
password = ""

for i in range(length):
    password += random.choice(characters)

print("Your password is:", password)
math.sqrt(16)