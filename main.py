from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = ScoreBoard()

screen.listen()
screen.onkey(player.move,"Up")

is_game_on = True
count_to_generate_car = 0
while(is_game_on):
    time.sleep(0.1)
    screen.update()
    car_manager.move()
    
    if player.at_finish_line():
        score_board.increase_level()
        car_manager.move_increment *= 1.2
    elif player.check_collision(car_manager.cars):
        score_board.game_over()
        is_game_on = False
    
    car_manager.generate_car()
    
screen.exitonclick()
    