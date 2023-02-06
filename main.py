# turtle class
# move to north and cant get back

# obstacle class
# generate random 20x40 object

# level class
# if user pass level, then the speed become faster

# if turtle hit finish, game level up
# if turtle get crash by car, then game over
from turtle import Turtle, Screen
from character import Character
from obstacle import Obstacle
import time

screen = Screen()
screen.screensize(600, 600)
screen.title("The Turtle Crossing")
screen.tracer(0)

turtle = Character()

obstacles = Obstacle()

screen._listen()
screen.onkey(turtle.go_forward, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # if turtle succeed crossing the roal, mission complate and reset postiion for next level
    if turtle.ycor() > 280:
        print("you go to the next level")
        turtle.reset_position()

    obstacles.create_obstacle()
    obstacles.move_forward()


screen.exitonclick()
