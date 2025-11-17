from turtle import Turtle
import time

FONT = ("Lucida console", 90, "bold")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self, score_address):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("gray")
        self.score = 0
        self.goto(score_address)
        self.update()


    def update(self):
        self.clear()
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.update()