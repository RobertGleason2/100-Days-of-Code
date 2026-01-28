from turtle import Turtle

SCORE_LOCATION = (0, 280)
ALIGNMENT = "center"
FONT = ("arial", 14, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(SCORE_LOCATION)
        self.current_score = 0
        self.display_score()

    def increase_score(self):
        self.clear()
        self.current_score += 1
        self.display_score()

    def display_score(self):
        self.write(arg=f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)