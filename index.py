#SpaceWar from Christian Thomson channel

import os
import random

#Import the Turtle module
import turtle
#Set the animation speed to the maximum
turtle.speed(0)
#Change the background color
turtle.bgcolor("black")
#Hide  the defoult turtle
turtle.ht()
#This saves memory
turtle.setundobuffer(1)
#This speeds up drawing
turtle.tracer(1)


class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1


#Create my sprites
player = Sprite("triangle", "white", 0, 0)





delay = input("Press enter to close program. >")

