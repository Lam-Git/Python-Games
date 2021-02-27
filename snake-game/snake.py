import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Creating a window screen

wn = turtle.Screen()
wn.title("Snake Game by Lam Nguyen")
wn.bgcolor("black")

# the width and height can be put as user's choice.
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Head of the snake
head = turtle.Turtle()
head.shape("turtle")  # The snake can be change
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Food in the game
food = turtle.Turtle()
colors = random.choice(["red", "blue", "green"])
shapes = random.choice(["square", "triangle", "circle"])
food.speed(0)
food.shape("triangle")  # this can be change
food.color("red")
food.penup()
food.goto(0, 100)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score : 0", align="center", font=("Courier", 24, "bold"))

# Function
# assigning key directions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Event handlers
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

segments = []


# Main Gameplay
while True:
    wn.update()

    # Check for a collision with the border
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(["red", "blue", "green"])
        shapes = random.choice(["square", "circle"])

        # High the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()
        # Reset the score
        score = 0
        # Resent the delay
        delay = 0.1
        pen.clear()
        pen.write(
            "Score : {} High Score : {} ".format(score, high_score),
            align="center",
            font=("Courier", 24, "bold"),
        )
    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")  # tail shape
        new_segment.color("gray")  # tail color
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score & content for the score board.
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(
            "Score : {} High Score : {} ".format(score, high_score),
            align="center",
            font=("candara", 24, "bold"),
        )
    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(["red", "blue", "green"])
            shapes = random.choice(["square", "circle"])

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segment.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write(
                "Score : {} High Score : {} ".format(score, high_score),
                align="center",
                font=("Courier", 24, "bold"),
            )
    time.sleep(delay)

wn.mainloop()

