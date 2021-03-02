import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()
player_1 = Player()
score = Scoreboard()
car = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player_1.up, "Up")
    screen.onkey(player_1.down, "Down")
    car.cars()
    car.move()

    if player_1.ycor() > 290:
        score.level_up()
        player_1.starting()
        car.speed_up()

    for cars in car.all_cars:
        if player_1.distance(cars) < 15:
            score.game_over()
            game_is_on = False

screen.exitonclick()
