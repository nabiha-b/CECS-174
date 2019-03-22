#import random buil-in library
import random

#Ask for user input of number of rolls to stimulate
number_of_rolls = int(input("Enter the number of times to roll the dice: "))

while True:

    #Declare and initiate possible sums of dice rolls
    num_twos = 0
    num_threes = 0
    num_fours = 0
    num_fives = 0
    num_sixes = 0
    num_sevens = 0
    num_eights = 0
    num_nines = 0
    num_tens = 0
    num_elevens = 0
    num_twelves = 0

    #Loop counter
    i=0

    #Display title for histogram
    print("Dice roll histograms:")

    #Continue program if number of rolls is greater than 1 
    if number_of_rolls >= 1:
        #Roll the dice number_of_rolls times
        while i in range (number_of_rolls):
            #Use randint fucnction to randomly roll dice
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            #Calculate sum of two dice rolled
            dice_total = die1 + die2

            #Count the sums rolled
            if dice_total == 2:
                num_twos += 1
            elif dice_total == 3:
                num_threes += 1
            elif dice_total == 4:
                num_fours += 1
            elif dice_total == 5:
                num_fives += 1
            elif dice_total == 6:
                num_sixes += 1
            elif dice_total == 7:
                num_sevens += 1
            elif dice_total == 8:
                num_eights += 1
            elif dice_total == 9:
                num_nines += 1
            elif dice_total == 10:
                num_tens += 1
            elif dice_total == 11:
                num_elevens += 1
            elif dice_total == 12:
                num_twelves += 1
            i += 1
        #Display histogram of possible values of sums rolled using asterisks
        print("2s: "+"*"*num_twos)
        print("3s: "+"*"*num_threes)
        print("4s: "+"*"*num_fours)
        print("5s: "+"*"*num_fives)
        print("6s: "+"*"*num_sixes)
        print("7s: "+"*"*num_sevens)
        print("8s: "+"*"*num_eights)
        print("9s: "+"*"*num_nines)
        print("10s: "+"*"*num_tens)
        print("11s: "+"*"*num_elevens)
        print("12s: "+"*"*num_twelves)
    #If number_of_rolls entered was less than 1, ask users to try again.
    else:
        print("Invalid rolls. Try again.")
    #Repeatedly ask users for number of rolls and quit if number of rolls
    #entered is less than 1
    number_of_rolls = int(input("Enter the number of times to roll the dice: "))
    if (number_of_rolls > 1):
        continue
    else:
        break

#End of Program
