"""
To do
# Class Snake 
# Method create snake 
# Method move snake 

"""
# Import the modules
from turtle import Turtle

# A class for the snake
class Snake:
    # Initialize the snake and give him a list of turtles (his body) and their positions
    def __init__(self):
        self.turtles=[]
        self.positions=((-40, 0), (-20, 0), (0, 0))
        # Make the init method call the create method automatically
        self.create()
        # Make an attribute for the head (last turtle in turtles list)
        self.head=self.turtles[-1]
    # A method to create the snake's body
    def create(self):
        for i in range(len(self.positions)):
            new_turtle=Turtle('square')
            new_turtle.color('white')
            new_turtle.penup()
            new_turtle.goto(self.positions[i])
            
            # Add every turtle to the turtles list as an object
            self.turtles.append(new_turtle)
        


    def move(self):
        # Make every turtle from the index 0 follow the turtle after her 
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos()) # pos returns the turtle positions as a tuple (x, y)
        # After that move the snake forward 
        self.head.forward(20) 
    
    # Define some methods to turn the snake right, left, up, and down
    # There's one condition you don't have to be in the opposite direction to turn
    # for example you can't turn to the left and you're facing into the right

    # The heading method returns the turtle's facing 
    # 0: right
    # 90: up
    # 180: left
    # 270: down
    
    # The setheading method redirect the turtle's facing into what you want
    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
    
    # Define a method that check if the snake get out of the window
    def check_get_out(self):
        if self.head.xcor()<-380 or self.head.xcor()>380 or self.head.ycor()<-280 or self.head.ycor()>280:
            return True
        return False
    
    # Define a method to increase the snake tall
    def increase_tall(self):
        new_turtle=Turtle('square')
        new_turtle.color('white')
        new_turtle.penup()
        self.turtles.insert(0, new_turtle)

    # Define a method to check if the snake touch himself (the distance between him and any turtle from his body less or equal to 10)
    def check_touch_himself(self):
        for i in range(len(self.turtles)-1):
            if self.head.distance(self.turtles[i])<=10:
                return True
        return False

    