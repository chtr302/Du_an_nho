from turtle import *
from Paddle import *
from Ball import *
from ScoreBoard import *
import time

# Class OB
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = ScoreBoard()

# Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Arcade Game by Tran Cong Hau")
screen.tracer(0)

# Screen Event
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# Game Play
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

    # Detect wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R and L Paddle
    if ball.xcor() > 395:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -395:
        ball.reset_position()
        scoreboard.r_point()

    
screen.exitonclick()
