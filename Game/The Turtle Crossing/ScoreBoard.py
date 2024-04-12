from turtle import *

ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-400,200)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.level}",align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.",align = "center", font = FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_score()