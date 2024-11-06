from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVING_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create()
    def create(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color("white")
        self.segments.append(new_segment)

    def move(self):
        for s in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[s - 1].xcor()
            new_y = self.segments[s - 1].ycor()
            self.segments[s].goto((new_x, new_y))
        self.segments[0].forward(MOVING_DISTANCE)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
       if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create()