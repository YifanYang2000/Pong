import turtle
import os

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
a = turtle.Turtle()
a.speed(0)
a.shape("square")
a.color("white")
a.shapesize(stretch_wid=5, stretch_len=1)
a.penup()
a.goto(-350, 0)

# Paddle B
b = turtle.Turtle()
b.speed(0)
b.shape("square")
b.color("white")
b.shapesize(stretch_wid=5, stretch_len=1)
b.penup()
b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(3)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = 2.5


# Scoreboard
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player A: 0             Player B: 0", align="center", font=("Courier", 24, "normal"))

# Score
score_a = 0
score_b = 0

# Paddle movement
def a_up():
    y = a.ycor()
    y += 20
    a.sety(y)
    if y > 248:
        a.sety(248)

def a_down():
    y = a.ycor()
    y -= 20
    a.sety(y)
    if y < -248:
        a.sety(-248)

def b_up():
    y = b.ycor()
    y += 20
    b.sety(y)
    if y > 248:
        b.sety(248)

def b_down():
    y = b.ycor()
    y -= 20
    b.sety(y)
    if y < -248:
        b.sety(-248)

# Keyboard binding
wn.listen()
wn.onkeypress(a_up, "w")
wn.onkeypress(a_down, "s")
wn.onkeypress(b_up, "Up")
wn.onkeypress(b_down, "Down")



# Main game loop
while True:
    wn.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border limits
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay wall.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay wall.wav&")

    # Scoring
    if ball.xcor() > 390:
        os.system("afplay fail.wav")
        ball.goto(0, 0)
        ball.dy *= -1
        a.goto(-350, 0)
        b.goto(350, 0)
        score_a += 1
        score.clear()
        score.write("Player A: {}             Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        os.system("afplay fail.wav")
        ball.goto(0, 0)
        ball.dy *= -1
        a.goto(-350, 0)
        b.goto(350, 0)
        score_b += 1
        score.clear()
        score.write("Player A: {}             Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    # Paddle collision
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < a.ycor() + 50) and (ball.ycor() > a.ycor() -50):
        ball.dx *= -1
        os.system("afplay bounce.wav&")
    
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < b.ycor() + 50) and (ball.ycor() > b.ycor() -50):
        ball.dx *= -1
        os.system("afplay bounce.wav&")
