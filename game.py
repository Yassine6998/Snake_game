"""
To do
# Window management
# Game loop

"""
# import modules 
from turtle import Turtle, Screen
from food import Food
from score import Score
from snake import Snake 
import time
# Initialize the window
window=Screen()
window.setup(width=800, height=600)
window.bgcolor('black')
window.title('Snake Game')
window.tracer(0)

# Create a turtle to write the score and the losing message
turtle_writer=Turtle()
turtle_writer.hideturtle()
turtle_writer.penup()
turtle_writer.color('white')

# Create the snake
snake=Snake()
window.update()

# Create the food
food=Food()

# Create the score
score=Score()

# Make the window listen to the player's keyboard
window.listen()
# Give the player keys to move the snake
window.onkey(snake.right, "Right")
window.onkey(snake.left, "Left")
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")


game_on=True
# The snake will move forward until the player turn it
while game_on:
    # While the loop is no the turtle will print the score on the top
    score.write_score()
    snake.move()
    # After moving the window will update the screen
    window.update()
    # Sleep less than a second to make the snake a little slow
    time.sleep(0.1)
    # If the distance between the snake's head and the food equal or less than 5 pixels
    if snake.head.distance(food)<=5:
    # respawn the food in another place and add 1 to the score
        food.appear()
        snake.increase_tall()
        score.result+=1

    # Check if the snake get out of the window
    if snake.check_get_out():
        game_on=False

    # Check if the snake touches himself
    if snake.check_touch_himself():
        game_on=False

# Write the message and the final score
turtle_writer.write('You lose!', align='center', font=('arial', 18, 'normal'))
turtle_writer.goto(0, -30)
turtle_writer.write(f'Final Score {score.result}', align='center', font=('arial', 18, 'normal'))
time.sleep(0.1)
window.update()



# Freeze the window after finishing the code until press to exit 
window.exitonclick()


