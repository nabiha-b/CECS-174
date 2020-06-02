# Nabiha Bashir
# This program returns the sum of a series of numbers inputted by the user.

x = int(input("Enter a series of positive numbers and press 'Enter' after each number. \nEnter a negative number to end series. \n: "))
my_nums = [x]
y = 0

while x>= 0:
    if x >= 0:
        x = int(input(": "))
        my_nums.append(x)

for i in my_nums:
    if i >=0:
        y += i
print("Total Sum: %d" %y)  




        
