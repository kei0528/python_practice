import random
from turtle import Turtle, Screen, colormode

rgb_colors = [
    (170, 251, 168),
    (172, 44, 108),
    (250, 197, 212),
    (29, 3, 10),
    (195, 115, 151),
    (216, 248, 217),
    (51, 39, 180),
    (0, 18, 3),
    (242, 220, 207),
    (176, 56, 130),
]

distance = 80
dot_size = 20
x = -300
y = 300

turtle = Turtle()
colormode(255)
for _ in range(0, 5):
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(dot_size)
    turtle.pencolor(random.choice(rgb_colors))
    turtle.pendown()

    for _ in range(0, 5):
        turtle.penup()
        turtle.goto(x, y)
        turtle.dot(dot_size)
        turtle.pencolor(random.choice(rgb_colors))
        turtle.pendown()
        y -= distance

    x += distance
    y -= -distance * 5

screen = Screen()
screen.exitonclick()
