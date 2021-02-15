from block_manager import BlockManager
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard, LevelLabel
from intersect import Intersect


class BreakoutGame:
    def __init__(self, initial_level, screen_dims):
        self.level = initial_level
        self.screen_dims = screen_dims
        self.block_manager = BlockManager(initial_level=self.level, screen_dims=screen_dims)
        self.paddle = Paddle()
        self.ball = Ball(starting_y=self.block_manager.get_ball_start_y())
        self.human_scoreboard = ScoreBoard(player="Human", screen_dims=screen_dims)
        self.computer_scoreboard = ScoreBoard(player="Computer", screen_dims=screen_dims)
        self.level_label = LevelLabel(initial_level=self.level, screen_dims=screen_dims)

    def reset_game(self):
        self.ball.reset_game()
        self.paddle.reset_game()

    def play_game(self):
        """move the ball, check for collisions against edges and objects"""
        blnCollision = False
        # Check if there are any blocks left | Increment level if all destroyed
        if len(self.block_manager.blocks) == 0:
            self.level += 1
            self.level_label.increment_level()
            self.block_manager.add_blocks(lvl=self.level)
        # Check if collided with gutter | Computer wins
        elif self.ball.location[1][0] <= self.screen_dims[1][0]:
            blnCollision = True
            self.computer_scoreboard.increment_score()  # Computer player gets a point
            self.reset_game()   # Reset Game
        # Check if collided with wall (Left/Right) | Invert Ball
        elif self.ball.location[0][0] - self.ball.move_increment < self.screen_dims[0][0] or self.ball.location[0][1] + self.ball.move_increment > self.screen_dims[0][1]:
            blnCollision = True
            self.ball.invert_ball(blnReverse=True)
            self.ball.move()
        # Check if collided with wall (Top) | Invert Ball & Change Direction
        elif self.ball.location[1][1] + self.ball.move_increment > self.screen_dims[1][1]:
            blnCollision = True
            self.ball.change_direction()
            self.ball.invert_ball(blnReverse=False)
            self.ball.move()
        # Check if collided with paddle | Invert Ball & Change Direction
        elif Intersect(self.ball.location, self.paddle.location):
            blnCollision = True
            self.ball.change_direction()
            self.ball.invert_ball(blnReverse=False)
            self.ball.move()
        # Check if collided with block | Human wins
        else:
            blocks_to_remove = []
            for key in self.block_manager.blocks:
                block_x = self.block_manager.blocks[key]
                if Intersect(self.ball.location, block_x.location):
                    blnCollision = True
                    block_x.destroy_block()     # Hide Block
                    blocks_to_remove.append(key)    # Mark for removal
                    # Invert Ball
                    self.ball.change_direction()
                    self.ball.invert_ball(blnReverse=False)
                    self.ball.move()
                    # Human player gets a point
                    self.human_scoreboard.increment_score()
                    break
            # Remove block from block manager
            for key in blocks_to_remove:
                self.block_manager.blocks.pop(key)
        # Otherwise just move the ball
        if not blnCollision:
            self.ball.move()
        return blnCollision
