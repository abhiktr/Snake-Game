from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.shape('square')
        self.setheading(90)
        self.shapesize(1, 5)
        self.penup()
        self.goto(cor, 0)
        self.color('white')

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
