from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
TIME_TO_GEN_CAR = 2
STARTING_RANGE_X = (300, 350)
STARTING_RANGE_Y = (-240,240)

class CarManager():
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_increment = MOVE_INCREMENT
        self.count_to_generate_car = 0
        self.generate_car()
    
    def generate_car(self):
        if self.count_to_generate_car >= TIME_TO_GEN_CAR:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setposition(random.randint(STARTING_RANGE_X[0],STARTING_RANGE_X[1]),random.randint(STARTING_RANGE_Y[0],STARTING_RANGE_Y[1]))
            new_car.setheading(180)
            self.cars.append(new_car)
            self.count_to_generate_car = 0
        else:
            self.count_to_generate_car += 1
            
    def move(self):
        for car in self.cars:
            car.forward(self.move_increment)
            