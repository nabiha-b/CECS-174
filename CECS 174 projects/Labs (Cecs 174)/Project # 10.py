
import random


    
def main():
    def playguessinggame():
        random_number = random.randint(1,50)
        print(random_number)
        guess = int(input("A random number in the range of 1 to 50 has been generated. \nGuess the random number. Enter '-1' at any time to exit the game. \n: "))
        while True:
            if guess >= 0:
                if guess > random_number:
                    print("Too high, try again.")
                if guess < random_number:
                    print("Too low, try again.")
            
                if guess == random_number:
                    print("Congratulations! You guessed the number.")
                    print("It took you %d guesses to get it correct", %TBD)
                             
           guess = int(input("Guess the random number: "))
            elif guess >= 0:
                continue
            else:
                break

            
            elif guess == -1:
                print("The game will now end. Thank you for your time."))
                
            
                    
            

                   
    playguessinggame()

main()
