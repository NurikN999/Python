from turtle import Turtle, Screen
import turtle as t
import random as rand


naruto = Turtle()
t.colormode(255)


def random_colour():
    r = rand.randint(0, 255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)
    colour = (r, g, b)
    return colour


naruto.pensize(10)
naruto.speed("fastest")
directions = [0, 90, 180, 270]


for i in range(200):
    naruto.color(random_colour())
    naruto.forward(50)
    naruto.setheading(rand.choice(directions))

screen = Screen()
screen.exitonclick()