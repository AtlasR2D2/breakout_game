from turtle import Turtle
import random

INITIAL_SHAPE_SIZE = 20
BLOCK_WIDTH = 40
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_LINE_Y = -280
FINISH_LINE_Y = 280
BOTTOM_OF_SCOREBOARD_Y = 250
WEST_HEADING = 180
START_OF_ROAD = 300
END_OF_ROAD = -300
BLOCK_GAP = 5
BALL_GAP = 50
LEVEL_1_ROWS = 8
LEVEL_INC_ROWS = 2


class BlockManager:
    def __init__(self, initial_level, screen_dims):
        self.screen_dims = screen_dims
        self.initial_level = initial_level
        self.blocks = {}    # Dictionary to hold blocks
        self.next_ord = 0
        self.blocks_per_row = int(round((self.screen_dims[0][1] - self.screen_dims[0][0] - BLOCK_GAP) / (BLOCK_WIDTH + BLOCK_GAP),0))
        self.add_start_gap = (self.screen_dims[0][1] - self.screen_dims[0][0] - self.blocks_per_row * (BLOCK_WIDTH + BLOCK_GAP) - BLOCK_GAP) / 2
        self.end_gap = BLOCK_GAP + self.add_start_gap
        self.add_blocks(lvl=initial_level)

    def add_blocks(self, lvl):
        self.row_count = LEVEL_1_ROWS + LEVEL_INC_ROWS * (lvl - 1)    # SET number of rows of blocks
        # For each row and each column: add a block
        for i in range(self.row_count):
            for j in range(self.blocks_per_row):
                self.blocks[self.next_ord] = Block(i, j, self.end_gap)
                self.next_ord += 1

    def clear_blocks(self):
        for key in self.blocks:
            block_x = self.block[key]
            block_x.destroy_block()
        self.blocks = {}
        self.next_ord = 0

    def get_ball_start_y(self):
        return self.blocks[self.next_ord-1].location[1][0] - BALL_GAP


class Block(Turtle):
    def __init__(self, block_row, block_column, end_gap_size):
        super().__init__()
        self.left_edge = -250
        self.top_edge = 340
        self.block_row = block_row
        self.block_column = block_column
        self.end_gap_size = end_gap_size
        self.penup()
        self.build_block()
        self.block_left = 0
        self.position_block(block_row, block_column)

    def destroy_block(self):
        self.hideturtle()

    def Identify_Car(self):
        self.color("black")

    def position_block(self, row_pos, col_pos):
        x_coor = self.left_edge + self.end_gap_size + (self.shapesize()[1] * INITIAL_SHAPE_SIZE + BLOCK_GAP) * col_pos + (
                    self.shapesize()[1] * INITIAL_SHAPE_SIZE / 2)
        y_coor = self.top_edge - (self.shapesize()[0] * INITIAL_SHAPE_SIZE + BLOCK_GAP) * row_pos
        self.goto(x=x_coor, y=y_coor)
        self.set_location()

    def build_block(self):
        # TODO: Different coloured blocks change speed differently
        # random.seed()
        # random_color = random.choice(COLORS)
        # self.color(random_color)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=BLOCK_WIDTH/INITIAL_SHAPE_SIZE)

    def set_location(self):
        """contains a nested list of the block location left edge to right edge, bottom edge to top edge"""
        self.block_left = self.xcor() - (self.shapesize()[1] * INITIAL_SHAPE_SIZE / 2)
        self.block_right = self.xcor() + (self.shapesize()[1] * INITIAL_SHAPE_SIZE / 2)
        self.block_bottom = self.ycor() - (self.shapesize()[0] * INITIAL_SHAPE_SIZE / 2)
        self.block_top = self.ycor() + (self.shapesize()[0] * INITIAL_SHAPE_SIZE / 2)
        self.location = [(self.block_left, self.block_right), (self.block_bottom, self.block_top)]
