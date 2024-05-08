from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.dx = 10
        self.dy = 10
        self.velocity = 0.1

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1
        self.velocity *= 0.8

    def reset_position(self):
        self.goto(0, 0)
        self.velocity = 0.1
        self.bounce_x()
