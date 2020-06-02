# Nabiha Bashir
# This program helps users create a strong password based on strict guidelines.


def getPassword():
    print("Password guidelines:\n"
          "- At least 1 letter between [a-z] and 1 letter between [A-Z].\n"
          "- At least 1 number between [0-9].\n"
          "- At least 1 character from [$#@].\n"
          "- Minimum length 6 characters.\n"
          "- Maximum length 16 characters.")
    print()
    return input("Enter password: ")


def countDigits(password):
    return sum(character.isdigit() for character in password)

def countLowerLetters(password):
    return sum(character.islower() for character in password)

def countUpperLetters(password):
    return sum(character.isupper() for character in password)

def countSpecialChar(password):
    special_char = []
    counter = 0
    for character in password:
        if character == 'S' or character == '#' or character == '@':
            special_char.append(character)
    return len(special_char)


def validPassword(password):
    if len(password) >= 6 and len(password) <= 16 and countDigits(password) >= 1 and countLowerLetters(
            password) >= 1 and countUpperLetters(password) >= 1 and countSpecialChar(password) >= 1:
        return True
    return False


def main():
    password = getPassword()
    if validPassword(password):
        print()
        print('Your password is valid.')
    else:
        print()
        print('Your password is invalid. Please try again.')
        print()
        print()
        main()

main()
