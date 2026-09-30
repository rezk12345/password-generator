import random
import string

print("Password Generator")
length = int(input("Enter desired password length: "))

include_upper = input("Include uppercase letters? (y/n): ")
include_lower = input("Include lowercase letters? (y/n): ")
include_digits = input("Include numbers? (y/n): ")
include_symbols = input("Include symbols? (y/n): ")

characters = ""

if include_upper.lower() == 'y':
    characters += string.ascii_uppercase

if include_lower.lower() == 'y':
    characters += string.ascii_lowercase

if include_digits.lower() == 'y':
    characters += string.digits

if include_symbols.lower() == 'y':
    characters += string.punctuation

if characters == "":
    print("You must choose at least one character set!")
else:
    password = "".join(random.choice(characters) for _ in range(length))
    print("Generated Password: ", password)
