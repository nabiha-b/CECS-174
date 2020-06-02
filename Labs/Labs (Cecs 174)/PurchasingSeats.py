# Nabiha Bashir
# This program returns the income generated from the purchases of seats of different classes.

print("Enter the number of tickets for each class of seats that you wish to purchase.")

# Get user input on the number of seats purchased for each Class
Class_A = int(input("Class A: "))
Class_B = int(input("Class B: "))
Class_C = int(input("Class C: "))

# Declare and initiate variables for each Class' income
Class_A_income = 0
Class_B_income = 0
Class_C_income = 0


# Define a main function for the program
def main():
    # Define function to collect data for Class A
    def ClassA(Class_A):
        # Display the # of seats purchased for Class A
        print("Class A seats purchased: ", Class_A)
        # Calculate the income generated for Class A
        Class_A_income = Class_A * 50
        # Display the income generated for Class A
        print("Class A income generated: $", Class_A_income)

    # Define function to collect data for Class B
    def ClassB(Class_B):
        # Display the # of seats purchased for Class B
        print("Class B seats purchased: ", Class_B)
        # Calculate the income generated for Class B
        Class_B_income = Class_B * 25
        # Display the income generated for Class A
        print("Class B income generated: $", Class_B_income)

    # Define function to collect data for Class C
    def ClassC(Class_C):
        # Display the # of seats purchased for Class C
        print("Class C seats purchased: ", Class_C)
        # Calculate the income generated for Class C
        Class_C_income = Class_C * 10
        # Display the income generated for Class A
        print("Class C income generated: $", Class_C_income)

        # Calculate the total overall income generated
        total_income = Class_A_income + Class_B_income + Class_C_income
        # Display the total income generated
        print("Total income generated from all seats purchased: $", total_income)

    # Call the functions for the three classes
    ClassA(Class_A)
    ClassB(Class_B)
    ClassC(Class_C)


# Call the main function
main()


