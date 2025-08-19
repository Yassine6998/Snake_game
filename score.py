"""
To do
Class for the score
Define a method to write the score at the top of the window (game screen)
"""
# Import modules
from turtle import Turtle
# A class for the score
class Score(Turtle):
    def __init__(self):
        super().__init__()
        # Define a turtle to writer the score
        self.result=0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 250)

    def write_score(self):
        # Clear before writer (clear only what the turlte wrote not all the window)
        self.clear()
        self.write(f"Score {self.result}", align='center', font=('arial', 18, 'normal'))

