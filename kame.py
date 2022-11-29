import turtle
import random


def get_random_color():
    R = random.random()
    B = random.random()
    G = random.random()

    return (R, B, G)


kame = turtle.Turtle()
kame.shape("turtle")
kame.color("darksalmon")
kame.speed(0)
kame.pensize(2)
directions = [0, 90, 180, 270]

rotate = 0

for _ in range(0, 30):
    kame.color(get_random_color())
    kame.setheading(rotate)
    kame.circle(100)
    rotate += 10


screen = turtle.Screen()
screen.exitonclick()
