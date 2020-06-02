# Nabiha Bashir
# This program returns the sum of a list of randomly generated numbers and duplicates if they exist.

#import randint function from random library
from random import randint
#Create empty list 'list_nums'
list_nums = []
#Assisgn a variable to total sum
total_sum = 0

#Use for loops to add 10 random numbers to list 'list_nums'
print("Random numbers generated:")
for i in range (10):
    x = randint(1, 26)
    list_nums.append(x)
    print(x, end=' ')

#Display the random generated list
print("\nList of random numbers generated:", list_nums)

#Use for loops to calculate sum of the list
for i in list_nums:
    total_sum += i
#Display total sum
print("Total Sum:", total_sum)

#Use for loop to identify unique numbers in list and remove them
for x in set(list_nums):
    list_nums.remove(x)
duplicates = list(set(list_nums))
#Display the duplicates
print("Duplicates in list: ", duplicates)
