#!/bin/python3
import turtle

nael = turtle.Turtle()
nael.speed(6)
myscreen = turtle.Screen()

myscreen.bgcolor("orange")


# base rectangle
nael.color("grey")

# first function
def draw(x,y):
    nael.penup()
    nael.goto(x,y)
    nael.pendown()
    
# second function
def move(length1,angle1,length2,angle2):
    nael.forward(length1)
    nael.right(angle1)
    nael.forward(length2)
    nael.left(angle2)
    

draw(-200,-110)
nael.begin_fill()
nael.forward(410)
nael.right(90)
nael.forward(100)
nael.right(90)
nael.forward(410)
nael.right(90)
nael.forward(100)
nael.end_fill()
nael.penup

#first building(left)
nael.color("black")
nael.begin_fill()
move(40,90,10,90)
nael.forward(20)
nael.right(90)
move(30,90,10,90)
move(10,90,10,90)
nael.forward(10)

# second building
nael.left(90)
nael.forward(20)
nael.right(90)
move(20,90,20,90)
nael.forward(10)
nael.left(90)

# third building
nael.forward(30)
nael.right(90)
nael.forward(4)
nael.circle(3)
move(4,90,4,90)



# 4th building
move(5,90,2,90)
nael.forward(5)
nael.left(90)
move(7,90,10,90)
move(10,90,6,90)
move(20,90,3,90)
move(10,90,3,90)
nael.forward(5)
nael.right(90)
move(10,90,5,90)
move(3,90,10,90)
move(3,90,20,90)
move(6,90,20,90)
move(3,90,5,90)
move(4,90,8,90)

#between 4th building and Empire state building

nael.forward(7)
nael.left(90)
move(9,90,10,90)


#Empire State Building

move(10,90,10,90)
move(100,90,5,90)
move(20,90,5,90)
move(15,90,2,90)
move(10,90,10,90)


# top of ESB

move(10,90,20,95)
move(90,190,89,95)
move(20,90,10,90)
move(10,90,10,90)
move(2,90,15,90)
move(5,90,20,90)
move(5,90,142,90)

#between Empire and Chrysler
nael.forward(4)
nael.left(90)
nael.forward(90)
nael.right(90)
move(50,90,4,90)
nael.forward(6)
nael.right(90)
nael.goto(125,-20)

#Chrysler
nael.left(90)
nael.forward(20)
nael.left(90)
move(12,90,4,90)
nael.forward(12)
nael.right(90)
nael.forward(4)
nael.goto(160,30)
nael.left(88)
nael.forward(20)
nael.left(183)
nael.forward(20)
nael.goto(160,30)
nael.left(0)
nael.forward(25)
nael.left(90)
move(4,90,12,90)
move(4,90,15,90)
move(4,90,60,90)
nael.forward(4)
nael.left(90)
nael.forward(40)
nael.right(90)
move(10,90,10,90)
nael.forward(15)
nael.right(90)
nael.forward(60)
nael.end_fill()

#I love Ny

draw(-180,140)
nael.color("red")
def write():
    print("")
write()
nael.write("",None,"16pt bold")
