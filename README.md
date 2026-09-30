# Password Generator
 
A simple command-line password generator written in Python. You choose the length and which types of characters to include, and it generates a random password for you.
 
This was my first Python project.
 
## Features
 
- Choose any password length
- Optionally include:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Symbols (`!@#$%^&*` and more)
- Warns you if you don't select any character set
## Requirements
 
- Python 3.6 or newer
- No external libraries needed (uses only the built-in `random` and `string` modules)
## How to Run
 
1. Clone the repository:
```
   git clone https://github.com/rezk12345/password-generator.git
   cd password-generator
```
 
2. Run the script:
```
   python "Password Generator (First Project).py"
```
 
## Example
 
```
Password Generator
Enter desired password length: 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): n
Generated Password:  aK7mP2xQv9Lz
```
 
## How It Works
 
1. The program asks for the password length and which character types to include.
2. It builds a pool of characters from the selected types using Python's `string` module.
3. It picks one random character from the pool for each position in the password.
4. If no character type is selected, it shows an error message instead.
## Possible Improvements
 
- Use the `secrets` module instead of `random` for cryptographically secure passwords
- Validate input (for example, handle non-numeric length)
- Guarantee at least one character from each selected type
- Add an option to copy the password to the clipboard
- Add a graphical interface
## Author
 
Created by [Mohamed Rezk](https://github.com/rezk12345)
 
