import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
car_manager = CarManager()

player = Player()
score = Scoreboard()

screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    car_manager.create_car()
    car_manager.move_cars()
    time.sleep(0.1)
    screen.update()

    # Check if level passed
    if player.ycor() == 280:
        player.regenerate()
        score.update_scoreboard()

    # Check for collision
    for i in car_manager.all_cars:
        if player.distance(i) < 20:
            game_is_on = False
score.game_over()
screen.exitonclick()
