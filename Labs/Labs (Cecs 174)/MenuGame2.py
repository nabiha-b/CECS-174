# Nabiha Bashir
# This program contains a menu with various different mini programs/games.

# create function that contains menu
def menu():
    print("-----MENU-----")
    print("1 : Upper Case/Lower Case")
    print("2 : Max Numbers")
    print("3 : Palindrome Test")
    print("4 : Odd/Evern Counter")
    print("5 : Math Quiz")
    print("6: To Quit")
    print("")


# create function for Upper/Lower Case game
def upper_lower_case():
    # Initate and define variables for upper and lower case numbers
    upper_case = 0
    lower_case = 0
    # Display name of game and instructions
    print("** Upper Case/Lower Case detector **")
    print("Enter a series of alphabetical letters.")
    # Get string from user input
    string = input("")
    # For loops to iterate over string and detect upper/lower case letters
    for i in string:
        # Count lower case letters in string
        if (i.islower()) == True:
            lower_case += 1
        # Count upper case letters in string
        elif (i.isupper()) == True:
            upper_case += 1
    # Display number of upper/lower case letters
    print("Number of lower case letters:", lower_case)
    print("Number of upper case letters:", upper_case)


# Create a function for Max Number game
def max_numbers():
    # Create an empty list
    num_list = []
    print("** Max Number detector from a series of 4 numbers **" )
    # use for loop to allow user to enter number 4 times
    for i in range(4):
        x = int(input("Enter a number: "))
        # Add each entered number into list
        num_list.append(x)
    print(num_list)
    # Calculate max number if user entered maximum of 4 numbers
    if len(num_list) <= 4:
        # locate and display maximum number
        print("Maximum number:", max(num_list))
    else:
        # If user entered more than four numbers, display error and repeat game
        print("Invalid number of numbers entered. Enter a maximum of four numbers (i.e. 1234)")
        print("Try again.")
        max_numbers()


# Create function for the Palindrome Test game
def palindrome_test():
    # Display name and instructions for game
    print("** The Palindrome Test **")
    print("Enter a word, phrase, or sequence.")
    # Get user inputted letters
    letters = input("")
    # Reverse the letter entered and assign output to variable
    letters_rev = letters[::-1]
    # If reversed letters match original letters, letters are palindrome
    if letters == letters_rev:
        print("Yes, it is a palindrome.")
    # If reversed letters don't match original letters, letters are not palindrome
    else:
        print("No, it is not a palindrome.")


# Create function for Odd/Even Counter game
def odd_even_counter():
    # Import random module
    import random
    print(" ** Even/Odd Detector for 10 random numbers **")
    # Create empty list
    random_num_list = []
    # Create and initiate variable for odd and even numbers
    odds = 0
    evens = 0
    # Use for loops to create 10 random integers
    for x in range(10):
        random_num = random.randint(1, 50)
        random_num_list.append(random_num)
        # Identify even and odd numbers
        if (random_num % 2) == 0:
            evens += 1
        else:
            odds += 1
    # Display results
    print(random_num_list)
    print("Number of Even numbers: ", evens)
    print("Number of Odd numbers: ", odds)


# Create function for Math Quiz game
def math_quiz():
    # import random module
    import random
    print("** Math Addition Quiz **")
    # Create 2 random 3 digit numbers
    num_1 = random.randint(100, 999)
    num_2 = random.randint(100, 999)
    # Ask users to enter sum of numbers
    print(num_1, "+", num_2, "is:")
    user_answer = int(input(""))
    # Calculate sum of the two numbers
    answer = num_1 + num_2
    # If user answer is correct, congratulate users
    if user_answer == answer:
        print("Congratulations! Your answer is correct.")
    # If user answer is incorrect, display correct answer
    else:
        print("Your answer is incorrect. The answer is ", (num_1 + num_2))


# Create main function
def main():
    # Call menu function to display menu
    menu()
    try:
        # Get user input on menu selection
        option = int(input("Enter menu selection: "))
        # Call the game function which corresponds with user menu selection
        if option == 1:
            upper_lower_case()
            main()
        elif option == 2:
            max_numbers()
            main()
        elif option == 3:
            palindrome_test()
            main()
        elif option == 4:
            odd_even_counter()
            main()
        elif option == 5:
            math_quiz()
            main()
        elif option == 6:
            print("You have chosen to quit. Goodbye!")
        else:
            print("Invalid Input, Try Again.")
            main()
    # Identify and display errors for invalid inputs
    except:
        print("Invalid input")
        # repeat menu
        main()


# Call main function
main()
