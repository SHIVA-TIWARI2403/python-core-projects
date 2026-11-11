import turtle
import math

screen =turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("SHIVA")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("red")
pen.penup()

message = "SHIVA"
font = ("arial", 15, "bold")

scale = 18
point = 500

for i in range(point + 1):

    t = math.pi * 2 * i / point

    x = 16 * math.sin(t) **3

    y = (
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(4 * t)
        -math.cos(4 * t)
    )

    x *= scale
    y *= scale

    pen.goto(x, y)

    pen.write(
        message,
        align="center",
        font=font
    )

turtle.done()
