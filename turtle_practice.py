from turtle import Turtle, Screen

turtle = Turtle()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def turn_right():
    turtle.right(10)


def turn_left():
    turtle.left(10)


def pen_down():
    turtle.pendown()


def pen_up():
    turtle.penup()


pensize = 1


def size_up():
    global pensize
    if pensize < 10:
        pensize += 1
        turtle.pensize(pensize)


def size_down():
    global pensize
    if pensize > 1:
        pensize -= 1
        turtle.pensize(pensize)


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key=",", fun=pen_down)
screen.onkey(key=".", fun=pen_up)
screen.onkey(key="+", fun=size_up)
screen.onkey(key="-", fun=size_down)

screen.exitonclick()
