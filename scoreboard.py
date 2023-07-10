from turtle import Turtle
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}", align=ALIGNMENT)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align=ALIGNMENT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
