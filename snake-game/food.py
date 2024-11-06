from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.65,stretch_wid=0.65)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.random_x = random.randint(-280,280)
        self.random_y = random.randint(-280, 265)
        self.goto(self.random_x,self.random_y)