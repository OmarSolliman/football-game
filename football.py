import turtle

# --------------------------------------------------------------------------------------

game = turtle.Screen()
game.title("football game")
game.bgcolor("#000")
game.setup(width=800, height=600)
game.tracer(0)

# --------------------------------------------------------------------------------------

# player 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_wid=4, stretch_len=0.5)
player1.color("red")
player1.penup()
player1.goto(350, 0)
player1.dx = 0
player1.dy = 0

# player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_wid=4, stretch_len=0.5)
player2.color("blue")
player2.penup()
player2.goto(-350, 0)
player2.dx = 0
player2.dy = 0

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.40
ball.dy = 0.40

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("0 : 0", align="center", font=("courier",24,"normal"))

# --------------------------------------------------------------------------------------

# functions


def player1_up():
    y = player1.ycor()
    y += 20
    player1.sety(y)


def player1_down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)


def player2_up():
    y = player2.ycor()
    y += 20
    player2.sety(y)


def player2_down():
    y = player2.ycor()
    y -= 20
    player2.sety(y)


# --------------------------------------------------------------------------------------

# control
game.listen()
game.onkeypress(player1_up, "Up")
game.onkeypress(player1_down, "Down")

game.onkeypress(player2_up, "w")
game.onkeypress(player2_down, "s")

# --------------------------------------------------------------------------------------

while True:
    game.update()

# --------------------------------------------------------------------------------------

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# --------------------------------------------------------------------------------------

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if player1.ycor() > 260:
        player1.sety(260)
        player1.dy *= -1
    if player1.ycor() < -260:
        player1.sety(-260)
        player1.dy *= -1

    if player2.ycor() > 260:
        player2.sety(260)
        player2.dy *= -1
    if player2.ycor() < -260:
        player2.sety(-260)
        player2.dy *= -1

# --------------------------------------------------------------------------------------

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= 1
        score1 += 1
        score.clear()
        score.write("{} : {}".format(score1, score2), align="center", font=("courier",24,"normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= 1
        score2 += 1
        score.clear()
        score.write("{} : {}".format(score1, score2), align="center", font=("courier",24,"normal"))

# --------------------------------------------------------------------------------------

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

# --------------------------------------------------------------------------------------