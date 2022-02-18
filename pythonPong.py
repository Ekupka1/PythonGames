#Pong Game - Basic
#BY: Ethan Kupka 2/217/2022

import turtle

#screen setup
wn = turtle.Screen()
wn.title("Pong BY ELK")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

mid_circle = turtle.Turtle()
mid_circle.pencolor("gray")
mid_circle.pensize(2)
mid_circle.circle(20)
mid_circle.penup()
mid_circle.hideturtle()

mid_line = turtle.Turtle()
mid_line.shape("square")
mid_line.color("gray")
mid_line.shapesize(stretch_wid = 50, stretch_len = .05)
mid_line.penup()

#score
score_a = 0
score_b = 0

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")

paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")

paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,-260)
pen.write("Player 1: 0   Player 2: 0", align = "center", font = ("Courier", 15, "normal"))

#functions of paddles
def paddle_a_up():
    y = paddle_a.ycor() #from turlte mod and returns y location
    y += 50
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #from turlte mod and returns y location
    y -= 50
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #from turlte mod and returns y location
    y += 50
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() #from turlte mod and returns y location
    y -= 50
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#main
while True:
    wn.update() #updates screen

    #moving te ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #boarder check paddles
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    #boarder check ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player 1: {}   Player 2: {}".format(score_a, score_b), align = "center", font = ("Courier", 15, "normal"))

    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player 1: {}   Player 2: {}".format(score_a, score_b), align = "center", font = ("Courier", 15, "normal"))

    #paddle bounce
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
