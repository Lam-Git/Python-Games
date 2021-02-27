# Simple Pong in Python3 for Beginner

import turtle
import os

# Create Screen for the Game:
wn = turtle.Screen()
wn.title("Pong by Lam Nguyen")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Right paddle_a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Left paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("turtle")  # can be any shape.
ball.color("red")  # color of shape
ball.penup()
ball.goto(0, 0)
ball.dx = 1  # the ball will move 2 mag pix
ball.dy = -1

# Pen - score board
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


# Initialize the score
score_a = 0
score_b = 0

# Function  to move Left paddle_a
def paddle_a_up():
    y = paddle_a.ycor()  # get y-coordinate
    y += 20  # add 20 to y-coordinate
    paddle_a.sety(y)  # set new y-coordinate


def paddle_a_down():
    y = paddle_a.ycor()  # get y-coordinate
    y -= 20  # subtract 20 from y-coordinate
    paddle_a.sety(y)  # set new y-coordinate


# Function to move Right paddle_b
def paddle_b_up():
    y = paddle_b.ycor()  # get y-coordinate
    y += 20  # add 20 to y-coordinate
    paddle_b.sety(y)  # set new y-coordinate


def paddle_b_down():
    y = paddle_b.ycor()  # get y-coordinate
    y -= 20  # subtract 20 from y-coordinate
    paddle_b.sety(y)  # set new y-coordinate


# Keyboard Binding
wn.listen()  # tells the program to listen to keyboard into
wn.onkeypress(paddle_a_up, "w")  # when the user press "w" paddle a will go up
wn.onkeypress(paddle_a_down, "s")  # when the user press "w" paddle a will go down
wn.onkeypress(paddle_b_up, "Up")  # when the user press "w" paddle a will go up
wn.onkeypress(paddle_b_down, "Down")  # when the user press "w" paddle a will go down


# Main Game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    # Top Borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Bottom Borders
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Left and right Boarders
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write(
            "Player A: {}  Player B: {}".format(score_a, score_b),
            align="center",
            font=("Courier", 24, "normal"),
        )
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write(
            "Player A: {}  Player B: {}".format(score_a, score_b),
            align="center",
            font=("Courier", 24, "normal"),
        )
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if (
        ball.xcor() < -340
        and ball.ycor() < paddle_a.ycor() + 50
        and ball.ycor() > paddle_a.ycor() - 50
    ):
        ball.dx *= -1
        os.system("afplay bounce.wav&")
    elif (
        ball.xcor() > 340
        and ball.ycor() < paddle_b.ycor() + 50
        and ball.ycor() > paddle_b.ycor() - 50
    ):
        ball.dx *= -1
        os.system("afplay bounce.wav&")
