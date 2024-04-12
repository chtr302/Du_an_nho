from turtle import *

STARTING_POSTITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.goto(STARTING_POSTITION)

    def come_back(self):
        self.goto(STARTING_POSTITION)

    def up(self):
        self.new_y = self.ycor() + 10
        self.goto(self.xcor(),self.new_y)