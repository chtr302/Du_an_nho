from turtle import *
from Player import *
from Car_manager import *
from ScoreBoard import *
import time


# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game by Tran Cong Hau")
screen.tracer(0)

# Class Setup
player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

# Screen Check Event
screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Car move
    car_manager.create_car()
    car_manager.move_cars()
    # Detect Car
    for car in car_manager.cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()
    # Check playe detect wall
    if player.ycor() > 280:
        player.come_back()
        car_manager.level_up()
        scoreboard.increase_score()

screen.exitonclick()