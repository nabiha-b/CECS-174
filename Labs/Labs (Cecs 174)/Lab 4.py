
import math


height = float(input("Enter the wall's height: "))
width = float(input("Enter the wall's width: "))
area = height * width
print("The area of the wall is %f square feet" %area)


paint_needed = area/400

print("The amount of paint needed to cover the wall is %f gallons" %paint_needed)


cans = math.ceil(paint_needed)

print("Cans needed to paint the wall: %f" %cans)


color = input("What color do you want to paint the wall?: ")

paintcolors = {"red": 25,"blue" : 30,"green" : 27}


print("The total cost of the paint cans for", color,"paint: $", str(cans*paintcolors[color]))
