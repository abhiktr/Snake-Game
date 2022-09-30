from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.penup()
        self.goto(0,270)
        self.cscore=0
        self.hscore=0
        self.write(arg=f'Score ={self.cscore} high score = {self.hscore}', move=False, align='center', font=('Arial', 20, 'normal'))
        self.hideturtle()

    def reset(self):
        if self.cscore>self.hscore:
            self.hscore = self.cscore
        self.cscore=0



    def score(self):
        self.cscore+=1
        self.clear()
        self.write(arg=f'Score ={self.cscore} ',move=False,align='center',font=('Arial', 20,'normal'))

