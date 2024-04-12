from turtle import *
from Snake import *
from Food import *
from ScoreBoard import *
import time

# Use Class
snake = Snake()
food = Food()
score_on_board = ScoreBoard()

# Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by Tran Cong Hau")
screen.tracer(0)

# Screen event key
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# Game Play
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Check snake eat food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        score_on_board.increase_score()
        snake.update_snake()

    # Check snake collide wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score_on_board.reset()

    # Check snake collide tail
    for segement in snake.segements[1:]:
        if snake.head.distance(segement) < 10:
            score_on_board.reset()
            snake.reset()


screen.exitonclick()