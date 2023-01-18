from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COLLISION_RANGE = 20

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_position()
    
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def reset_position(self):
        self.setposition(STARTING_POSITION)
        
    def at_finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            self.reset_position()
            return True
        else:
            return False
    
    def check_collision(self, cars):
        player_pos = self.position()
        for car in cars:
            if (car.distance(player_pos) < COLLISION_RANGE and
                abs(car.xcor()-player_pos[0]) < 30):
                return True
        return False