"""
To do
Class for the Food
Method create Food
Method Check If Food Is Eaten

"""
x_positions=range(-380, 381, 20)
y_positions=range(-280, 281, 20)

# import modules
from turtle import Turtle
import random
# Make a class for Food
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.8, 0.8) 
        self.color('red')
        self.penup()
        self.appear()
        
    def appear(self):
        # Respawn the food in another coordinates
        self.goto(random.choice(x_positions), random.choice(y_positions))
        

