import turtle
import random

COLOR = [(0, 100, 0), (0, 128, 0), (34, 139, 34), (0, 255, 0), (50, 205, 50), (152, 251, 152), (143, 188, 143), (0, 250, 154), (0, 255, 127), (46, 139, 87), (102, 205, 170), (60, 179, 113), (32, 178, 170), (47, 79, 79), (0, 128, 128),
         (0, 139, 139), (0, 255, 255), (0, 255, 255), (224, 255, 255), (0, 206, 209), (64, 224, 208), (72, 209, 204), (175, 238, 238), (127, 255, 212), (176, 224, 230), (95, 158, 160), (70, 130, 180), (100, 149, 237), (0, 191, 255)]
MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
turtle.colormode(255)


class Obstacle:
    def __init__(self):
        self.all_cars = []

    def create_obstacle(self):
        random_change = random.randint(1, 6)
        if random_change == 1:
            new_car = turtle.Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLOR))
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_forward(self):
        for car in self.all_cars:
            car.backward(MOVE_DISTANCE)
