
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)
game_is_on = True
paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))
scoreboard = Scoreboard()
ball = Ball()
velocity = 0.1

screen.onkeypress(fun=paddle1.up,key="Up")
screen.onkeypress(fun=paddle1.down,key="Down")

screen.onkeypress(fun=paddle2.up,key="w")
screen.onkeypress(fun=paddle2.down,key="s")

while game_is_on:
    screen.update()
    scoreboard.update_scoreboard()
    time.sleep(ball.velocity)

    ball.move()
    #Detect collision with paddles
    if paddle1.distance(ball) < 50 and ball.xcor() > 320 or paddle2.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.velocity = ball.velocity * 0.9

    #Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.lpoint()
        ball.velocity = 0.1

    #Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.rpoint()
        ball.velocity = 0.1

screen.exitonclick()