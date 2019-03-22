#Get future value
future_value = float(input("Enter the desired future value: "))

#Get annual interest rate
annual_int_rate = float(input("Enter the annual interest rate percentage: "))
annual_int_rate = annual_int_rate/100

#Get number of years 
years = float(input("Enter the number of years the money will grow: "))

#Calculate deposit
deposit = (future_value)/((1+annual_int_rate)**years)
deposit= float(round(deposit, 2))

#Display results
print("The desired future value: $", future_value)
print("The annual interest rate:", annual_int_rate, "%")
print("The number of years the money will grow:", years, "years")
print("The amount needed to deposit: $", deposit)
