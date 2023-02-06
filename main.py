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
from scoreboard import Scoreboard
import time

screen = Screen()
screen.screensize(600, 600)
screen.title("The Turtle Crossing")
screen.tracer(0)

turtle = Character()
obstacles = Obstacle()
scoreboard = Scoreboard()

screen._listen()
screen.onkey(turtle.go_forward, "space")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # if turtle succeed crossing the road, mission complate and reset postiion for next level
    if turtle.ycor() > 280:
        turtle.reset_position()
        obstacles.level_up()
        scoreboard.increase_level()

    obstacles.create_obstacle()
    obstacles.move_forward()

    # detect collision with obstacle
    for obstacle in obstacles.all_obstacle:
        if obstacle.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
