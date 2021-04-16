from turtle import Turtle, Screen


nur_turtle = Turtle()

def dashed_line():
    for i in range(10):
        nur_turtle.color("red")
        nur_turtle.forward(10)
        nur_turtle.color("white")
        nur_turtle.forward(10)




dashed_line()
nur_turtle.color("red")

screen = Screen()
screen.exitonclick()