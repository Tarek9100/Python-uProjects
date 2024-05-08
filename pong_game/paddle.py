from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y) -> None:
        super().__init__(shape="square")
        self.penup()
        self.left(90)
        self.shapesize(stretch_len=5)
        self.goto(x, y)
        self.color("white")

    def up(self):
        if self.ycor() != 280:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() != -280:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
