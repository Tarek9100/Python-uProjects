from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__(visible=False)
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.display()

    def display(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score: {self.highscore}",
                   align=ALIGNMENT, font=FONT)

    def increment(self):
        self.score += 1

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.display()
