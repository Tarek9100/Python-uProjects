from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
score = Scoreboard()
ball = Ball()
dx = 10
dy = 10
screen.listen()
screen.onkeypress(key='w', fun=l_paddle.up)
screen.onkeypress(key='Up', fun=r_paddle.up)
screen.onkeypress(key='s', fun=l_paddle.down)
screen.onkeypress(key='Down', fun=r_paddle.down)
last_paddle_hit = None
game_is_on = True


while game_is_on:
    time.sleep(ball.velocity)
    screen.update()
    ball.move()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddel
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 and last_paddle_hit != r_paddle:
        ball.bounce_x()
        last_paddle_hit = r_paddle
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320 and last_paddle_hit != l_paddle:
        ball.bounce_x()
        last_paddle_hit = l_paddle
    # Detect when r_paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        score.increment_left()
        score.update_scoreboard()
        last_paddle_hit = None
    # Detect when l_paddle misses
    elif ball.xcor() < -390:
        ball.reset_position()
        score.increment_right()
        score.update_scoreboard()
        last_paddle_hit = None


screen.exitonclick()
