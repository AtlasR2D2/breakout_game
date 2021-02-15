from turtle import Turtle

FONT = {"Arial", 16, "Bold"}
ALIGNMENT = "Center"

class ScoreBoard(Turtle):
    def __init__(self, player, screen_dims):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.player = player
        if self.player == "Human":
            x_coord = (screen_dims[0][1] - screen_dims[0][0]) / 4 * -1
            y_coord = (screen_dims[1][1] - screen_dims[1][0]) * 2/5
        elif self.player == "Computer":
            x_coord = (screen_dims[0][1] - screen_dims[0][0]) / 4
            y_coord = (screen_dims[1][1] - screen_dims[1][0]) * 2/5
        self.goto(x_coord, y_coord)
        self.score = 0
        self.show_score()

    def increment_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(arg=f"{self.player}: {self.score}", align=ALIGNMENT, font=FONT)


class LevelLabel(Turtle):
    def __init__(self, initial_level, screen_dims):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        x_coord = 0
        y_coord = (screen_dims[1][1] - screen_dims[1][0]) * 2/5
        self.goto(x_coord, y_coord)
        self.level = initial_level
        self.show_level()

    def increment_level(self):
        self.level += 1
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)
