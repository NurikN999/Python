from turtle import Turtle,Screen

turtle_cherepaha = Turtle()
turtle_leo = Turtle()

def square(t):
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)



turtle_cherepaha.shape("turtle")
turtle_cherepaha.color("DarkOrchid4")

turtle_leo.shape("turtle")
turtle_leo.right(90)
turtle_leo.color("blue")

square(turtle_cherepaha)
square(turtle_leo)


screen = Screen()
screen.exitonclick()