from turtle import Turtle


YCOR_POS_LIMIT = 280
YCOR_NEG_LIMIT = -280

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 0
        self.y = 0
        self.velocity = 0.1
        self.y_increment = 10
        self.x_increment = 10
        self.goto(self.x,self.y)

    def move(self):
        if self.y > YCOR_POS_LIMIT or self.y < YCOR_NEG_LIMIT:
            self.y_increment = self.y_increment * -1
        self.x += self.x_increment
        self.y += self.y_increment
        self.goto(self.x,self.y)

    def bounce_x(self):
        self.x_increment = self.x_increment * -1

    def reset_position(self):
        self.x = 0
        self.y = 0
        self.goto(0,0)
        self.x_increment *= -1