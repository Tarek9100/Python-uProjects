from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level {self.level}",align= "center",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!",align= "center",font=FONT)
