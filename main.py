import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    # detect collision with the cars
    for i in cars.cars: # cars array in cars object
        if i.distance (player) < 20:
            game_is_on = False

        # detect successful crossing
        if player.is_at_finish_line():
            player.go_to_start()
            cars.level_up()
    


screen.exitonclick()