from turtle import Turtle

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(360, 270)
        self.pensize(3)
        self.color("gray")
        self.setheading(0)

        for lines in range(2):
            self.right(90)
            self.forward(540)
            self.right(90)
            self.forward(720)

        self.penup()
        self.goto(0, 265)
        self.pendown()
        self.pensize(3)
        self.setheading(270)
        for _ in range(30):
            self.forward(9)
            self.penup()
            self.forward(9)
            self.pendown()

