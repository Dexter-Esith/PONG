from turtle import Turtle
import random

BALL_COLOR = "gray"
BALL_SHAPE = "circle"

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.penup()
        self.x_move = random.choice([10, -10])
        self.y_move = random.choice([10, -10])
        self.ball_speed = 0.05
        self.frozen = False

    def move(self):
        if not self.frozen:
            new_y = self.ycor() + self.y_move
            new_x = self.xcor() + self.x_move
            self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.95

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.ball_speed = 0.05