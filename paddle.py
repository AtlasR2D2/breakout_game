from turtle import Turtle

INITIAL_PADDLE_SIZE = 20
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
X_POS = 0
Y_POS = -410
MOVE_INCREMENT = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_HEIGHT/INITIAL_PADDLE_SIZE, stretch_len=PADDLE_WIDTH/INITIAL_PADDLE_SIZE)
        self.fillcolor("white")
        self.penup()
        # Position Paddle
        self.goto(x=X_POS, y=Y_POS)
        self.set_paddle_ends()

    def set_paddle_ends(self):
        self.paddle_left_x = self.xcor() - self.shapesize()[1] * INITIAL_PADDLE_SIZE / 2
        self.paddle_right_x = self.xcor() + self.shapesize()[1] * INITIAL_PADDLE_SIZE / 2
        self.paddle_inside_y = self.ycor() + self.shapesize()[0] * INITIAL_PADDLE_SIZE / 2
        self.paddle_outside_y = self.ycor() - self.shapesize()[0] * INITIAL_PADDLE_SIZE / 2
        self.location = [(self.paddle_left_x, self.paddle_right_x), (self.paddle_outside_y, self.paddle_inside_y)]

        # print(f"Player: {self.player} inside paddle edge {self.paddle_inside_x}")
    def move_left(self):
        if not self.paddle_left_x - MOVE_INCREMENT < self.getscreen().window_width() / 2 * -1:
            self.goto(x=self.xcor() - MOVE_INCREMENT, y=self.ycor())
            self.set_paddle_ends()

    def move_right(self):
        if not self.paddle_right_x + MOVE_INCREMENT > self.getscreen().window_width() / 2:
            self.goto(x=self.xcor() + MOVE_INCREMENT, y=self.ycor())
            self.set_paddle_ends()

    def reset_game(self):
        # Position Paddle
        self.goto(x=X_POS, y=Y_POS)
        self.set_paddle_ends()