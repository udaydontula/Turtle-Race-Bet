from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.color("black")
        self.level = 0
        self.penup()
        self.goto(-280, 280)
        self.write(f"Level : {self.level}", FONT)

    def level_up(self):
        self.clear()
        self.goto(-280, 280)
        self.level += 1
        self.write(f"Level : {self.level}", FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", FONT)
