# Nabiha Bashir
# This program rewards users with points based on how many books they purchased.

books = int(input("Enter the number of books purchased this month: "))
points_earned = 0

if books == 0:
    points_earned = 0
elif books >= 2 and books < 4:
    points_earned = 5
elif books >= 4 and books < 6:
    points_earned = 15
elif books >= 6 and books < 8:
    points_earned = 30
elif books >= 8:
    points_earned = 60

print("Number of points awarded: ", points_earned)
