from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import math
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
scoreboard = Scoreboard()
game_is_on = True
screen.onkey(fun = snake.up,key = "Up")
screen.onkey(fun = snake.down,key = "Down")
screen.onkey(fun = snake.left,key = "Left")
screen.onkey(fun = snake.right, key = "Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Detect collision with wall
    if abs(snake.segments[0].xcor()) > 280 or abs(snake.segments[0].ycor()) > 280:
        #game_is_on = False
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            #game_is_on = False
            scoreboard.reset()
            snake.reset()

screen.exitonclick()