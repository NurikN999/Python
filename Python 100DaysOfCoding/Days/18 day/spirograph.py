import turtle as t
from turtle import Turtle,Screen
import random as rand


naruto = t.Turtle()
t.colormode(255)
naruto.speed("fastest")
directions = []
for i in range(360):
    directions.append(i*10)

print(directions)


def random_color():
    r = rand.randint(0, 255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)
    colour = (r, g, b)
    return colour


def draw_spirograph():
    naruto.circle(50)


for _ in range(200):
    draw_spirograph()
    naruto.setheading(directions[_])
    naruto.color(random_color())


screen = Screen()
screen.exitonclick()