import turtle
import time
import math

screen = turtle.Screen()
screen.title("Analog Clock")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock():
    pen.penup()
    pen.goto(0, -200)
    pen.setheading(0)
    pen.pendown()
    pen.circle(200)

    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    for _ in range(12):
        pen.forward(160)
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.goto(0, 0)
        pen.right(30)

def draw_hands(hour, minute, second):
    pen.penup()
    pen.goto(0, 0)
    pen.color("black")
    pen.setheading(90)
    angle = (hour % 12) * 30 + minute / 2
    pen.right(angle)
    pen.pendown()
    pen.forward(100)

    pen.penup()
    pen.goto(0, 0)
    pen.color("blue")
    pen.setheading(90)
    angle = minute * 6 + second / 10
    pen.right(angle)
    pen.pendown()
    pen.forward(140)

    pen.penup()
    pen.goto(0, 0)
    pen.color("red")
    pen.setheading(90)
    angle = second * 6
    pen.right(angle)
    pen.pendown()
    pen.forward(160)

def update_clock():
    hour = int(time.strftime("%I"))
    minute = int(time.strftime("%M"))
    second = int(time.strftime("%S"))

    draw_clock()
    draw_hands(hour, minute, second)

    screen.update()
    pen.clear()

    time.sleep(1)
    update_clock()

if __name__ == "__main__":
    update_clock()

turtle.done()

