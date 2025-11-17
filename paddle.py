from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("gray")
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)

    def up(self):
        if self.ycor() < 220:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -220:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

    def reset_position(self, position):
        self.goto(position)
