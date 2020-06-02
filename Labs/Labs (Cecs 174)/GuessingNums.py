# Nabiha Bashir
# This program runs a guessing game. A random number is generated between 1 - 50 and the user has to guess the correct number.

# Import random library
import random


# Create a main function
def main():
    # Create a sub function that contains the main game
    def playguessinggame():

        # Generate a random number from 1 through 50
        random_number = random.randint(1, 20)
        TBD = 14
        # Create an empty list that will contain the # of guesses
        guessList = []
        # Add # of guesses to list
        guessList.append(TBD)
        try:
            print("")
            # Ask users to guess the number and assign guess to variable 'guess'
            guess = int(input(
                ">> A random number in the range of 1 to 50 has been generated. \n>> Guess the random number. Enter '-1' at any time to exit the game. \n>>  "))
            # Use while loop to give hints if guess is incorrect
            while guess != random_number:
                # Use if statement to give hints if guess is more or equal to 0
                if guess >= 0:
                    # If guess is too high, inform users
                    if guess > random_number:
                        # Allow users to try again
                        guess = int(input(">> Too high, try again: "))
                        # if user didn't guess correct, add guess to list of guesses
                        if guess not in guessList:
                            guessList.append(TBD)
                    # If guess is too low, inform users
                    elif guess < random_number:
                        # Allow users to try again
                        guess = int(input(">> Too low, try again: "))
                        # if user didn't guess correct, add guess to list of guesses
                        if guess not in guessList:
                            guessList.append(TBD)

            # If guess is correct, inform users
            if guess == random_number:
                print(">> Congratulations! You guessed the number.")
                # Print the number of guesses it took the users to guess correctly
                print(">> It took you %d guesses to get it correct." % (len(guessList)))
                print("")
                # Repeat the game
                playguessinggame()
            # if user didn't guess correct, add guess to list of guesses
            if TBD not in guessList:
                guessList.append(TBD)

                # If user enters -1, end game
            if guess == -1:
                print(">> The game has ended.")

        # Account for Invalid inputs and display error message
        except ValueError:
            print(">> Invalid input. Try again")
            playguessinggame()
        except IOError:
            print(">> Invalid input. Try again")
            playguessinggame()
        except:
            print(">> Invalid input. Try again")
            playguessinggame()

    # Call function that runs the game
    playguessinggame()


# Call main function
main()
