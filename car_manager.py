from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager ():
    def __init__ (self):
        super().__init__()
        self.cars = []
        self.carspeed = STARTING_MOVE_DISTANCE
    
    def create_cars (self):
        random_chance = random.randint(1,6)
        if random_chance == 1: # avoiding frequent car creation
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.cars.append(car)

    def move_cars (self):
        for i in self.cars:
            i.backward (STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.carspeed += MOVE_INCREMENT