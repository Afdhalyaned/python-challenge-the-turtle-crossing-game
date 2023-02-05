from turtle import Turtle


class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -250)

    def go_forward(self):
        y_position = self.ycor() + 10
        self.goto(0, y_position)

    def reset_position(self):
        self.goto(0, -250)
