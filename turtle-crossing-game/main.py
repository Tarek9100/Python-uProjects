import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
#screen.colormode("white")
screen.tracer(0)
screen.listen()
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()
screen.onkey(fun=player.up,key="Up")
screen.onkey(fun=player.down,key="Down")
game_is_on = True
while game_is_on:
    car_manager.create_cars()
    car_manager.move_cars()
    time.sleep(0.1)
    screen.update()

    # Check if level passed
    if player.ycor() == 280:
        player.regenerate()
        scoreboard.update_scoreboard()
        car_manager.step += 10


    #Detect turtle collision with cars
    for car in car_manager.allcars:
        if player.distance(car) < 20:
            game_is_on = False

scoreboard.game_over()
screen.exitonclick()