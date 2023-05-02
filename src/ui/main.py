from turtle import Screen

from src.model.divider import Divider
from src.model.paddle import Paddle
from src.model.ball import Ball
from src.model.scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350, 0, "red")
left_paddle = Paddle(-350, 0, "blue")
ball = Ball()
scoreboard = Scoreboard()
divider = Divider()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(screen.bye, "Escape")

game_is_on = True
while game_is_on:

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()
        scoreboard.update_scoreboard()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()
        scoreboard.update_scoreboard()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

screen.exitonclick()
