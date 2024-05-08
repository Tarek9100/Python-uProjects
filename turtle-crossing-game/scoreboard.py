from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-200, 260)
        self.write(f"Level {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "bold"))

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level {self.level}", align="center", font=FONT)
