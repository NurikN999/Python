from turtle import Turtle, Screen
import random as r

cherepaha = Turtle()
directions = [0,90,180,270]
cherepaha.pensize(15)
cherepaha.speed("fastest")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


for i in range(500):
    cherepaha.color(r.choice(colours))
    cherepaha.forward(50)
    cherepaha.setheading(r.choice(directions))

screen = Screen()
screen.exitonclick()