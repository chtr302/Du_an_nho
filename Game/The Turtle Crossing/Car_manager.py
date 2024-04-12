from turtle import *
import random

COLORS = ["red","orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(x=400, y=random.randint(-200, 200))
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):
        self.backward(self.speed)

class CarManager:
    def __init__(self) -> None:
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1,6) == 1:
            new_car = Car()
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.move()

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        for car in self.cars:
            car.speed  = self.car_speed
