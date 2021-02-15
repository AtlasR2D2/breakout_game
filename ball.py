from turtle import Turtle
import random
import time

INITIAL_BALL_SIZE = 20
BALL_WIDTH = 10
BALL_HEIGHT = 10
INITIAL_POS_X = 0
# INITIAL_POS_Y = 0
MOVE_INCREMENT = 2
SLEEP_AMOUNT = 0.00002

class Ball(Turtle):
    def __init__(self, starting_y):
        super().__init__()
        self.starting_y = starting_y
        self.move_increment = MOVE_INCREMENT
        self.shape("circle")
        self.shapesize(stretch_wid=BALL_HEIGHT/INITIAL_BALL_SIZE, stretch_len=BALL_WIDTH/INITIAL_BALL_SIZE)
        self.fillcolor("white")
        self.penup()
        self.reset_game()
        self.new_heading = self.heading()
        self.speed("fastest")

    def rotate_ball(self, direction):
        # Rotate a random angle for the initial trajectory
        random.seed()
        random_heading = random.randint(-90, 90)
        # Determine new heading based on direction of travel
        # Think clockwise movement
        if direction == "Up":
            if random_heading > 0:
                random_heading = random_heading
            elif random_heading < 0:
                random_heading = 180 + random_heading
            else:
                random_heading = 90
        elif direction == "Down":
            if random_heading > 0:
                random_heading = 180 + random_heading
            elif random_heading < 0:
                random_heading = 360 + random_heading
            else:
                random_heading = 270
        # Set random heading
        self.setheading(random_heading)

    def change_direction(self):
        if self.direction == "Up":
            self.direction = "Down"
        elif self.direction == "Down":
            self.direction = "Up"

    def reset_game(self):
        self.goto(x=INITIAL_POS_X, y=self.starting_y)
        self.set_ball_ends()
        self.direction = "Down"
        self.rotate_ball(self.direction)

    def invert_ball(self, blnReverse):
        """will invert the ball if it hits a surface or edge: blnReserve = False if top/bottom, True if left/right"""
        # Determine new heading based on direction of travel
        # Think clockwise movement
        if 0 < self.heading() < 90:
            if blnReverse:
                self.new_heading = 180 - self.heading()
            else:
                self.new_heading = 360 - self.heading()
        elif 90 < self.heading() < 180:
            if blnReverse:
                self.new_heading = 90 - (self.heading() - 90)
            else:
                self.new_heading = 270 - (self.heading() - 90)
        elif 180 < self.heading() < 270:
            if blnReverse:
                self.new_heading = 360 - (self.heading() - 180)
            else:
                self.new_heading = 180 - (self.heading() - 180)
        elif 270 < self.heading() < 360:
            if blnReverse:
                self.new_heading = 270 - (self.heading() - 270)
            else:
                self.new_heading = 90 - (self.heading() - 270)
        else:
            pass
        # Set new heading
        self.setheading(self.new_heading)

    def set_ball_ends(self):
        self.ball_top_y = self.ycor() + self.shapesize()[0] * INITIAL_BALL_SIZE / 2
        self.ball_bottom_y = self.ycor() - self.shapesize()[0] * INITIAL_BALL_SIZE / 2
        self.ball_left_x = self.xcor() - self.shapesize()[0] * INITIAL_BALL_SIZE / 2
        self.ball_right_x = self.xcor() + self.shapesize()[0] * INITIAL_BALL_SIZE / 2
        self.ball_left_y = self.ycor()
        self.ball_right_y = self.ycor()
        self.location = [(self.ball_left_x, self.ball_right_x), (self.ball_bottom_y, self.ball_top_y)]

    def move(self):
        """function will move the ball if it doesn't hit a wall"""
        """returns true if was able to move, false otherwise"""
        #time.sleep(SLEEP_AMOUNT)  # Use if you want to slow it down
        self.forward(MOVE_INCREMENT)
        self.set_ball_ends()
        return True
