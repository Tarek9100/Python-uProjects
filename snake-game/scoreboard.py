from turtle import Turtle

SCORE_POSITION = 260
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as hs:
            self.highscore = int(hs.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.sety(SCORE_POSITION)
        self.update_scoreboard()
    def update_scoreboard(self):
            self.clear()
            self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align="center", font=('Courier', 24, 'normal'))
    def increase_score(self):
            self.score += 1
            self.update_scoreboard()
    def reset_score(self):
            self.score = 0
            self.update_scoreboard()
    #def game_over(self):
            #self.goto(0,0)
           #self.write("Game Over!", move=False, align="center", font=('Courier', 36, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt",mode="w") as hs:
                hs.write(str(self.score))
        self.reset_score()
