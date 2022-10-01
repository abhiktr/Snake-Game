from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.penup()
        self.goto(0,270)
        self.l_score=0
        self.r_score=0
        self.write(arg=f"{self.l_score} | {self.r_score}",move=False,align="center",font=('Arial', 20, 'normal'))
        self.hideturtle()

    def l_wins(self):
        self.l_score+=1
        self.clear()
        self.write(arg=f"{self.l_score} | {self.r_score}", move=False, align="center", font=('Arial', 20, 'normal'))

    def r_wins(self):
        self.r_score+=1
        self.clear()
        self.write(arg=f"{self.l_score} | {self.r_score}", move=False, align="center", font=('Arial', 20, 'normal'))