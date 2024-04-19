from turtle import Turtle

ALIGN = "center"
FONT = ("Gadugi", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("data.txt") as data:
                self.highscore = int(data.read())
        except FileNotFoundError:
            self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.highscore}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
