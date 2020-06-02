# Nabiha Bashir
# This program calculates annual + monthly salary based on hours worked per week + year and hourly pay.


work_hours_per_week = int(input("Enter hours worked per week: "))
work_weeks_per_year = int(input("Enter hours worked per year: "))
hourly_pay = int(input("Enter your hourly pay: "))

yearly_salary= hourly_pay * (work_hours_per_week * work_weeks_per_year)

monthly_salary= hourly_pay * (work_hours_per_week * 4)

print("Your annual salary is: $", yearly_salary)
print("Your monthly salary is: $", monthly_salary)









