import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Frogger")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Allows user to move turtle with up arrow
screen.listen()
screen.onkey(player.move, "Up")

# Updates screen every 0.1 s
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # Detect successful crossing
    if player.ycor() > 280:
        player.goto(0, -280)
        scoreboard.score += 1
        scoreboard.update_scoreboard()
        car_manager.move_distance += 10

screen.exitonclick()
