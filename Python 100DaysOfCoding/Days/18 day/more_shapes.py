from turtle import Turtle, Screen
import random as r


cherepaha = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(sides):
    angle =  360 / sides
    for i in range(sides):
        cherepaha.forward(50)
        cherepaha.right(angle)


for i in range(3,10):
    draw_shape(i)
    cherepaha.color(r.choice(colours))

screen = Screen()
screen.exitonclick()