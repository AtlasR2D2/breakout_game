from turtle import Screen
from breakout_game import BreakoutGame

screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=900)
screen.title("Breakout")

screen.tracer(0)

# SET INITIAL LEVEL
INITIAL_LEVEL = 2

# Screen Dimension Variables
SCREEN_TOP = screen.window_height() / 2
SCREEN_BOTTOM = screen.window_height() / 2 * -1
SCREEN_LEFT = screen.window_width() / 2 * -1
SCREEN_RIGHT = screen.window_width() / 2
SCREEN_DIMS = [(SCREEN_LEFT, SCREEN_RIGHT), (SCREEN_BOTTOM, SCREEN_TOP)]

# Initialise Game
breakout_game = BreakoutGame(initial_level=INITIAL_LEVEL, screen_dims=SCREEN_DIMS)

# The game is watching your moves
screen.listen()
screen.onkey(fun=breakout_game.paddle.move_left, key="Left")
screen.onkey(fun=breakout_game.paddle.move_right, key="Right")

game_is_on = True
while game_is_on:
    # Update the screen
    screen.update()
    # Move the ball
    breakout_game.play_game()

screen.exitonclick()
