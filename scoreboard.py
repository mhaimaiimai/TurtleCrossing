from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-230,270)
GAME_OVER_POSITION = (0, 0)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 1
        self.display() 
    
    def display(self):
        self.clear()
        self.setposition(POSITION)
        self.write(f"Level: {self.level}", False, align="center", font=FONT)

    def increase_level(self):
        self.level+=1   
        self.display() 
        
    def game_over(self):
        self.setposition(GAME_OVER_POSITION)
        self.write("GAME OVER", False, align="center", font=FONT)