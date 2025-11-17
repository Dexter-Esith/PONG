from turtle import Screen, Turtle

import paddle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from board import Board
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")

ball = Ball()
board = Board()

left_player = Scoreboard((80, 140))
right_player = Scoreboard((-80, 140))

right_paddle = Paddle((340, 0))
right_paddle.color("red")
left_paddle = Paddle((-340, 0))
left_paddle.color("blue")

countdown_turtle = Turtle()
countdown_turtle.hideturtle()
countdown_turtle.color("white")
countdown_turtle.penup()
countdown_turtle.goto(0, 0)

def countdown(n):
    if n > 0:
        if not game_is_on:  # <--- stop if game ended
            countdown_turtle.clear()
            return

        countdown_turtle.clear()
        countdown_turtle.write(n, align="center", font=("Courier", 60, "bold"))
        screen.update()
        screen.ontimer(lambda: countdown(n - 1), 1000)
    else:
        countdown_turtle.clear()



screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.down, "s")

game_is_on = True
WIN_SCORE = 11

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # wall collision
    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.bounce_y()

    # collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        ball.setx(320)

    # collision with left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.setx(-320)

    # left scores
    if ball.xcor() > 340:
        left_player.increase()
        ball.reset_position()
        left_paddle.reset_position((-340, 0))
        ball.frozen = True  # stop movement
        countdown(3)  # show countdown
        screen.ontimer(lambda: setattr(ball, "frozen", False), 3000)  # unfreeze after 3 sec

    # right scores
    if ball.xcor() < -340:
        right_player.increase()
        ball.reset_position()
        right_paddle.reset_position((340, 0))
        ball.frozen = True  # stop movement
        countdown(3)  # show countdown
        screen.ontimer(lambda: setattr(ball, "frozen", False), 3000)  # unfreeze after 3 sec

    # WIN CONDITION
    if right_player.score == WIN_SCORE or left_player.score == WIN_SCORE:
        game_is_on = False

# -----------------------------
# CLEAR EVERYTHING & SHOW WINNER
# -----------------------------
screen.clear()
screen.bgcolor("black")

winner = Turtle()
winner.hideturtle()

if right_player.score > left_player.score:
    text = f"RED PLAYER WON!\nScore: {left_player.score} - {right_player.score}"
    winner.color("red")

else:
    text = f"BLUE PLAYER WON!\nScore: {left_player.score} - {right_player.score}"
    winner.color("blue")

winner.write(text, align="center", font=("Lucida Console", 30, "bold"))

screen.mainloop()