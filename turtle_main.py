import random
from turtle import Turtle, Screen
from random import *
from colors import COLORS


tinker = Turtle()
tinker.shape("turtle")
tinker.color("DarkOliveGreen")

def start_position():
    tinker.penup()
    tinker.goto(-300,250)

def dot_forward():
    for _ in range (30):
        tinker.dot(10, choice(COLORS))
        tinker.penup()
        tinker.forward(20)
        tinker.dot(10, choice(COLORS))

def dot_right():
    tinker.right(90)
    tinker.forward(20)
    tinker.dot(10, choice(COLORS))
    tinker.right(90)

def dot_left():
    tinker.left(90)
    tinker.forward(20)
    tinker.dot(10, choice(COLORS))
    tinker.left(90)

start_position()

for _ in range (28):
    tinker.speed(10)
    dot_forward()
    dot_right()
    dot_forward()
    dot_left()

tinker.hideturtle()

