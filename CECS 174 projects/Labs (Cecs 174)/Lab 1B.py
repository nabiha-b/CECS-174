# Nabiha Bashir
# 018348835
# Lab Assignment #1
# Due: 2/8/19

import turtle


#1
for x in range(4):
    turtle.forward(100)
    turtle.right(90)

#2
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)


#3

for x in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.penup()
turtle.goto(50,-90)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()
turtle.hideturtle()







