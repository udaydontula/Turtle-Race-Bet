from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.penup()
            car.shape("square")
            x = 260
            y = random.randint(-250, 250)
            car.goto(x, y)
            car.shapesize(stretch_len=2, stretch_wid=0.7)
            self.all_cars.append(car)

    def move(self):

        for cars in self.all_cars:
            cars.bk(self.move_speed)

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT
