from turtle import Turtle, Screen

turtle_color = ["red", "blue", "yellow", "black"]

screen = Screen()
bet = screen.textinput(title="Who wins?", prompt="Enter color!")
print(bet)

for color in turtle_color:
    turtle = Turtle(shape="turtle")
    turtle.shape("turtle")
    turtle.penup()
    turtle.color(color)
    y_pos = turtle_color.index(color) * 50
    turtle.goto(x=-250, y=y_pos)


screen.setup(width=500, height=400)
screen.exitonclick()
