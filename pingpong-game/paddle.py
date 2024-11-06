from turtle import Turtle

MOVE_INCREMENT = 20
YCOR_POS_LIMIT = 265
YCOR_NEG_LIMIT = -265

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid= 5 , stretch_len= 1)
        self.penup()
        self.speed("fast")
        self.goto(position)

    def up(self):
        if self.ycor() < YCOR_POS_LIMIT:
            self.sety(self.ycor() + 20)

    def down(self):
        if self.ycor() > YCOR_NEG_LIMIT:
            self.sety(self.ycor() - 20)


