from turtle import Turtle
import random as r

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.relocate()

    def relocate(self):
        x_cord = r.randint(-280, 280)
        y_cord = r.randint(-280, 280)
        if y_cord >= 270 or y_cord % 10 != 0 or x_cord % 10 != 0:
            self.relocate()
        self.goto(x=x_cord, y=y_cord)
