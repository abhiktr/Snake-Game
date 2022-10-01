from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_cor = 10
        self.y_cor =10

    def start(self):
        new_x= self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x,new_y)

    def reflect_s(self):
        self.y_cor *= -1

    def reflect_p(self):
        self.x_cor *= -1