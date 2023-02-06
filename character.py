from turtle import Turtle

START_POSITION = (0, -250)
MOVE_DISTANCE = 10


class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(START_POSITION)

    def go_forward(self):
        y_position = self.ycor() + MOVE_DISTANCE
        self.goto(0, y_position)

    def reset_position(self):
        self.goto(0, -250)
